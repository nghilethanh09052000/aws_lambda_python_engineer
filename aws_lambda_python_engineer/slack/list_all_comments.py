from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from typing import List, Dict
import json



def get_all_messages_thread(
        client: WebClient, 
        slack_owner: str, 
        channel_ids: List[str]
    ) -> List[Dict[str,str]]:
    """
        Get all messages from Slack Owner Account first
    """
    data = []
    try:
        for channel_id in channel_ids:
            messages = client.conversations_history(
                channel=channel_id
            )['messages']
            for message in messages:
                if 'client_msg_id' in message \
                    and 'reply_users' in message \
                        and slack_owner in message.get('reply_users'):
                    data.append({
                        'channel_id': channel_id,
                        'ts' : message.get('ts')
                    })

    except SlackApiError as e:
        error_response = {
            'statusCode': e.response['status'] or 400,
            'body': {
                'error': str(e),
                'slack_error': e.response['error']
            }
        }
        return error_response
    
    return data

def get_parent_message(
        messages: List[Dict[str,str]] ,
        thread_ts: str
) -> Dict[str,str]:
    return next((msg for msg in messages if msg['ts'] == thread_ts), {})

def lambda_handler(event, context):

    token = event['token']
    start_time = event['start']
    end_time = event['end']
    channel_ids = event.get('channel_ids', [])
    slack_owner = 'U06HFV74YLE'

    client = WebClient(token=token)
     
    thread_messages: List[Dict[str,str]] = get_all_messages_thread(
        client=client,
        slack_owner=slack_owner, 
        channel_ids=channel_ids
    )
        
    data = []
    try:
        """
            Retrieve all messages and then find owner's comments based on
            specific date time in event
        """
        for thread_message in thread_messages:
            replies = client.conversations_replies(
                channel=thread_message['channel_id'],
                ts=thread_message['ts'],
                # oldest=start_time,
                # latest=end_time
            )['messages']

            parent_messages = [reply for reply in replies if 'reply_users' in reply and slack_owner in reply['reply_users']]

            for reply in replies:
                if reply.get('user') == slack_owner and 'reply_users' not in reply:
                    parent_message = get_parent_message(
                            messages=parent_messages, 
                            thread_ts=reply.get('thread_ts')
                        )
                    data.append({
                        **reply,
                        'channel_id': thread_message['channel_id'],
                        'parent_message': parent_message
                    })
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }

    except SlackApiError as e:
        error_response = {
            'statusCode': e.response['status'] or 400,
            'body': {
                'error': str(e),
                'slack_error': e.response['error']
            }
        }
        return error_response

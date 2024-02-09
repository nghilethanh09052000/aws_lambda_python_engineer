from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

def lambda_handler(event, context):

    slack_owner = 'U06HFV74YLE'
    token = event['token']
    start_time = event['start']
    end_time = event['end']
    channel_ids = event.get('channel_ids', [])

    client = WebClient(
        token=token
    )
    try:
        data = []
        for channel_id in channel_ids:

            messages = client.conversations_history(
                channel=channel_id, 
                oldest=start_time, 
                latest=end_time
            )['messages']

            slack_owner_message = [
                message for message in messages 
                    if message.get('user') == slack_owner \
                    and 'client_msg_id' in message
            ] 

            data.extend(slack_owner_message)

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




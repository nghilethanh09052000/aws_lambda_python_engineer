from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import json

def lambda_handler(event, context):
    client = WebClient(token=os.getenv("SLACK_ACCESS_TOKEN"))
    start_time = event['start']
    end_time = event['end']
    channel_ids = event.get('channel_ids', [])
    try:
        messages = []
        for channel_id in channel_ids:
            history = client.conversations_history(
                channel=channel_id, 
                oldest=start_time, 
                latest=end_time
            )
            messages.extend(history['messages'])
        return {
            'statusCode': 200,
            'body': json.dumps(messages)
        }
    except SlackApiError as e:
        return {
            'statusCode': e.response['status'],
            'body': json.dumps(e.response['body'])
        }

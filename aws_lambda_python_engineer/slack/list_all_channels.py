from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import json

def lambda_handler(event, context):
    
    client = WebClient(
        token=os.getenv("SLACK_ACCESS_TOKEN")
    )
    try:
        channels = client.conversations_list()['channels']

        return {
            'statusCode': 200,
            'body': json.dumps(channels)
        }
    except SlackApiError as e:
        return {
            'statusCode': e.response['status'],
            'body': json.dumps(e.response['body'])
        }

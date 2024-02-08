from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

def lambda_handler(event, context):
    token = event['token']

    client = WebClient(
        token=token
    )
    try:
        channels = client.conversations_list()['channels']

        return {
            'statusCode': 200,
            'body': json.dumps(channels)
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

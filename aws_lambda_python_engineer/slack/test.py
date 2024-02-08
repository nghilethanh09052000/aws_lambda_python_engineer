import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

event = {
    'start': '',
    'end': '',
    # 'channel_ids' : ['C06HKLYUDAR']
}
client = WebClient(token=os.getenv("SLACK_ACCESS_TOKEN"))
print(os.getenv("SLACK_ACCESS_TOKEN"))
# start_time = event['start']
# end_time = event['end']
# channel_ids = event.get('channel_ids', ['C06HKLYUDAR'])
# try:
#     messages = []
#     for channel_id in channel_ids:
#         history = client.conversations_history(
#             channel=channel_id, 
#             # oldest=start_time, 
#             # latest=end_time
#         )
#         messages.extend(history['messages'])
#         print(history)
# except SlackApiError as e:
#     print(e.response['body'])


"""
    CREATE MESSAGE
"""

client.chat_postMessage(
    channel='C06HKLYUDAR',
    text='Bot Nghi Test 1'

)

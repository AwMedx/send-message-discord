import requests

user_token = 'XXXXXXXXX' # Find Discord token: https://www.androidauthority.com/get-discord-token-3149920/

message = input("Enter Message: ")
channelID = input("Enter Channel ID: ") # Right Click and Copy Channel ID, PASTE HERE

def send_message(msg, channel_id):
    headers = {
        'Authorization': user_token
    }

    payload = {
        'content': msg
    }

    path = f'https://discord.com/api/v9/channels/{channel_id}/messages'

    requests.post(path, json=payload, headers=headers)

send_message(message, channelID)

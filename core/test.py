import requests
import json


def importFromImgur(albumID):
    # Imports images from imgur and saves them to the cards folder
    # Replace YOUR_CLIENT_ID with your Imgur API client ID
    client_id = '072f9e376a0dc20'

    # Replace ALBUM_ID with the ID of the album you want to get images from
    album_id = albumID

    # Make a GET request to the Imgur API to get information about the album
    response = requests.get(f'https://api.imgur.com/3/album/{album_id}',
                            headers={'Authorization': f'Client-ID {client_id}'})

    # Convert the response to a JSON object
    data = json.loads(response.text)

    # Get the list of images from the JSON object
    images = data['data']['images']

    # Print the URLs for all images on the album
    for image in images:
        print(image['link'])



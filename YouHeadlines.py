from googleapiclient.discovery import build
from Constants import API_KEY


def GetTitle(video_url):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    video_id = video_url.split("=")[1]
    try:
        # Use the videos().list method to retrieve video details
        video_response = youtube.videos().list(
            part='snippet',
            id=video_id
        ).execute()

        # Extract the title from the response
        video_title = video_response['items'][0]['snippet']['title']

        return video_title

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

# print(GetTitle("https://www.youtube.com/watch?v=88SX_Ihx_d0"))
import datetime
from googleapiclient.discovery import build
from datetime import timedelta
from Constants import API_KEY


def search_channel(query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    try:
        search_response = youtube.search().list(
            q=query,
            part='id',
            type='channel',
            maxResults=1
        ).execute()

        if 'items' in search_response and search_response['items']:
            channel_id = search_response['items'][0]['id']['channelId']
            return channel_id
        else:
            print("No channels found.")
            return None
        
    except Exception as e:
        print(f"An error occurred during channel search: {e}")
        return None
    

        
def get_channel_videos(Channel_name):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    channel_id = search_channel(Channel_name)
    try:
        # Get the playlist items from the channel's uploads playlist
        uploads_playlist = youtube.channels().list(part='contentDetails', id=channel_id).execute()

        if 'items' not in uploads_playlist or not uploads_playlist['items']:
            print("No uploads playlist found.")
            return []

        playlist_id = uploads_playlist['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Get all the videos from the uploads playlist
        playlist_items = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50  # You can adjust this based on your needs
        ).execute()

        video_links = []
        for item in playlist_items.get('items', []):
            video_id = item['contentDetails']['videoId']

            # Get the video details to check the publicatdateion date
            video_details = youtube.videos().list(
                part='snippet',
                id=video_id
            ).execute()

            video_published_at = video_details['items'][0]['snippet']['publishedAt']
            # video_published_date = datetime.datetime.strptime(video_published_at, '%Y-%m-%dT%H:%M:%SZ').date()
            video_published_date = datetime.datetime.strptime(video_published_at, '%Y-%m-%dT%H:%M:%SZ').date()
            video_links.append(f'https://www.youtube.com/watch?v={video_id}')

        return video_links

    except Exception as e:
        print(f"An error occurred during video retrieval: {e}")
        return [] 
    
def GetCompletedLives(channel_name):
    youtube = build('youtube', 'v3', developerKey=API_KEY)  
    # channels = youtube.channels().list(forUsername=channel, part='id').execute()
    channel_id = search_channel(channel_name)
    
    today_date = (datetime.datetime.utcnow() - timedelta(hours=datetime.datetime.utcnow().hour)).strftime('%Y-%m-%dT00:00:00Z')
    videos = youtube.search().list(
        part='id,snippet',
        channelId=channel_id,
        eventType='completed',
        type='video',
        maxResults=100,  
        order='date',
        publishedAfter=today_date
    ).execute()

    video_links = []
    for item in videos['items']:
        video_id = item['id']['videoId']
        video_link = f'https://www.youtube.com/watch?v={video_id}'
        video_links.append(video_link)
    return video_links

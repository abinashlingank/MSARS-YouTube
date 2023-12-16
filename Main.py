from YouTubeLinks import GetCompletedLives, get_channel_videos
from Transcript import GetTranscript
import psycopg2
from psycopg2.extras import Json



Channel = "theHindu"

links = GetCompletedLives(Channel)

links += get_channel_videos(Channel)

for link in links:
    GetTranscript(link)
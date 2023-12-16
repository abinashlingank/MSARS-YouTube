from youtube_transcript_api import YouTubeTranscriptApi
from langdetect import detect

def GetCaption(video_url):
    try:
        video_id=video_url.split("=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        if not transcript:
            # No captions available
            return False

        # Combine the text from each entry into a single string
        transcript_text = ' '.join(entry['text'] for entry in transcript)

        return transcript_text, detect(transcript_text)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


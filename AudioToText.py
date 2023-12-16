import os
import whisper
from langdetect import detect
from pytube import YouTube

def AudToText(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_path = "Audios"
    filename = "audio.mp3"
    audio_stream.download(output_path=output_path, filename=filename)

    print(f"Audio downloaded to {output_path}/{filename}")

    model = whisper.load_model("base")
    result = model.transcribe(f"{output_path}/{filename}")
    transcribed_text = result["text"]

    language = detect(transcribed_text)
    return transcribed_text, language
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from groq import Groq
from dotenv import load_dotenv
import re
import os
import whisper
import yt_dlp

load_dotenv()

# Create temp directory if it doesn't exist
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

def download_audio(video_url, output_path="temp/audio.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'noplaylist': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return output_path
    except Exception as e:
        return f"Error downloading audio: {e}"

def transcribe_audio(file_path):
    """Transcribes audio using Whisper and removes the file afterward."""
    try:
        model = whisper.load_model("base")  # Load the Whisper model
        # model = whisper.load_model("tiny")  # Load the Whisper model
        if not os.path.exists(file_path):
            return "Error: Audio file not found"
        result = model.transcribe(audio=file_path, language="en")
        transcript_text = result["text"]
    except Exception as e:
        transcript_text = f"Error transcribing audio: {e}"
    
    # Remove the file after processing
    os.remove(file_path)
    return transcript_text

def get_transcript(video_url):
    """Fetches transcript from YouTube API or uses Whisper if unavailable."""
    try:
        regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
        match = re.search(regex, video_url)
        if not match:
            return "Error: Invalid YouTube URL"

        video_id = match.group(1)

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
            return " ".join([line["text"] for line in transcript])
        except (TranscriptsDisabled, NoTranscriptFound):
            audio_file = download_audio(video_url)
            if audio_file:
                return transcribe_audio(audio_file)
            return "Error: No transcript available, and audio processing failed."
    except Exception as e:
        return f"Error extracting video ID: {e}"

def summarize_text(text):
    """Uses Groq LLM to summarize text."""
    try:
        client = Groq()
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Summarize the given transcript in English."},
                {"role": "user", "content": text}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error summarizing text: {e}"
    
if __name__ == "__main__":
    video_url = ""
    transcript = get_transcript(video_url)
    print("Transcript:", transcript)
    print("Summarize Text:", summarize_text(transcript))
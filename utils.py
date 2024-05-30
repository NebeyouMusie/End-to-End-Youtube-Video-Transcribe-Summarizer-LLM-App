import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from config import load_config, get_google_api_key

# load configuration
load_config()

genai.configure(api_key=get_google_api_key())

# setup prompt
prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """


# getting the transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split('=')[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript = ''
        for i in transcript_text:
            transcript += ' ' + i['text']
        
        return transcript

    except Exception as e:
        raise e

# getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + transcript_text)
    return response.text

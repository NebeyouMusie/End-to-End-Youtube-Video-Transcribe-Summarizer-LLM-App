import streamlit as st
from utils import extract_transcript_details, generate_gemini_content, prompt

st.set_page_config(page_title="YouTube Video Summarizer")

st.title('YouTube Video Summarizer')
youtube_link = st.text_input('Enter YouTube Video Link:')

if youtube_link:
    video_id = youtube_link.split('=')[1].split('&')[0]
    st.image(f'http://img.youtube.com/vi/{video_id}/0.jpg')

if st.button('Get Summary'):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown('Here is the video summary')
        st.write(summary)
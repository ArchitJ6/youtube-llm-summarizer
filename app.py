import streamlit as st
from summarizer import get_transcript, summarize_text

st.title("🎥 YouTube Video Summarizer")
video_url = st.text_input("Enter YouTube Video URL")

if st.button("Summarize"):
    with st.spinner("Fetching transcript..."):
        transcript = get_transcript(video_url)

    if "Error" not in transcript:
        with st.spinner("Summarizing..."):
            summary = summarize_text(transcript)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.error(transcript)
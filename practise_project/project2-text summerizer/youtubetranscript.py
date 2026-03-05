import re
import os
import torch
import gradio as gr
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

# Set cache directory BEFORE loading model
os.environ['HF_HOME'] = 'E:\\dataScience and ai -Quest innovative\\.cache'

# Load summarization model
text_summary = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    torch_dtype=torch.bfloat16
)

def summary(input_text):
    max_chunk = 500
    chunks = [input_text[i:i+max_chunk] 
              for i in range(0, len(input_text), max_chunk)]
    
    result = ""
    for chunk in chunks:
        if len(chunk.strip()) > 50:
            # ✅ Fixed: dynamically set max_length based on chunk length
            input_length = len(chunk.split())
            max_len = min(130, input_length // 2)
            min_len = min(30, max_len - 1)

            output = text_summary(
                chunk,
                max_length=max_len,
                min_length=min_len,
                do_sample=False,
                truncation=True
            )
            result += output[0]['summary_text'] + " "
    
    return result.strip()


def extract_video_id(url):
    regex = r"(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return None


def get_youtube_transcript(video_url):
    # Validate input
    if not video_url or video_url.strip() == "":
        return "Please enter a valid YouTube URL."

    video_id = extract_video_id(video_url)
    if not video_id:
        return "Video ID could not be extracted. Please check the URL."

    try:
        # Fetch transcript
        transcript = YouTubeTranscriptApi().fetch(video_id)

        # Convert to plain text
        text_transcript = " ".join([t.text for t in transcript])

        if not text_transcript.strip():
            return "Transcript is empty or unavailable."

        # Summarize
        summary_text = summary(text_transcript)
        return summary_text

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Launch Gradio app
gr.close_all()

demo = gr.Interface(
    fn=get_youtube_transcript,
    inputs=[
        gr.Textbox(
            label="Enter YouTube URL",
            placeholder="https://www.youtube.com/watch?v=...",
            lines=1
        )
    ],
    outputs=[
        gr.Textbox(
            label="Summarized Text",
            lines=6
        )
    ],
    title="YouTube Video Summarizer",
    description="Enter a YouTube URL to get a summarized version of the video transcript."
)

demo.launch(debug=True)
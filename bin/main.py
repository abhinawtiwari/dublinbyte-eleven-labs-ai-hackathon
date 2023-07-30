import streamlit as st
from bin._elevenlabs import with_custom_voice, with_premade_voice, get_voices
from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History
import os
import dotenv

dotenv.load_dotenv()

ELEVENLABS_SECRET_KEY = os.environ.get("ELEVENLABS_SECRET_KEY")
if not ELEVENLABS_SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable not set")

set_api_key(ELEVENLABS_SECRET_KEY)

st.set_page_config(page_title="iPodcast", page_icon="🎧")

st.title("ReactTok")
# Give a description to the app
st.markdown(
    "This is a demo of the ReactTok using Eleven Labs APIs."
)

audio = generate(text="Some very long text to be read by the voice", voice='Charlotte')

play(audio)

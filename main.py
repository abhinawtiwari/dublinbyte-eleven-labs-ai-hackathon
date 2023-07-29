import streamlit as st
from _elevenlabs import with_custom_voice, with_premade_voice, get_voices
from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("a3ff8207c8b63c33e9d35d26a6977118")

st.set_page_config(page_title="iPodcast", page_icon="🎧")

st.title("ReactTok")
# Give a description to the app
st.markdown(
    "This is a demo of the ReactTok using Eleven Labs APIs."
)

audio = generate(text="Some very long text to be read by the voice", voice='Charlotte')

play(audio)

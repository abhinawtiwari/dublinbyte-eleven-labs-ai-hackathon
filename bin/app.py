# Import from standard library
import os
import logging

# Import from 3rd party libraries
import streamlit as st

# Import modules from the local package
from _langchain import get_response
from _elevenlabs import with_custom_voice, with_premade_voice, get_voices

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)
# Configure Streamlit page and state
st.set_page_config(page_title="iPodcast", page_icon="🎧")

# Store the initial value of widgets in session state
if "podcast_generate" not in st.session_state:
    st.session_state.podcast_generate = ""

if "output_file_path" not in st.session_state:
    st.session_state.output_file_path = ""

if "input_file_path" not in st.session_state:
    st.session_state.input_file_path = ""

if "text_error" not in st.session_state:
    st.session_state.text_error = ""

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"

# Force responsive layout for columns also on mobile
st.write(
    """
    <style>
    [data-testid="column"] {
        width: calc(50% - 1rem);
        flex: 1 1 calc(50% - 1rem);
        min-width: calc(50% - 1rem);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Give a title to the app
st.title("Eleven Labs + Langchain Tutorial")
# Give a description to the app
st.markdown(
    "This is a demo of the Eleven Labs + Langchain Tutorial."
)


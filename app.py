import streamlit as st
import random
import time
from chat_bot_API import chat
from voicelab import play_custom_audio
from utils.userId_generator import generate_random_string

st.set_page_config(page_title="ReacTok", page_icon="🎧")
st.title("ReacTok")
st.markdown(
    "TikTok fan engagement"
)

userId = 'test100000'
# userId = 'test' + generate_random_string(5)
# print("new user: " + userId)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


# Display assistant response in chat message container
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    audio_placeholder = st.empty()
    full_response = ""
    if prompt:
        assistant_response = chat({
        'query' : prompt,
        'userID' : userId
        })
        print("Stage: ", assistant_response['response']['conversation_stage'])
        if assistant_response['status'] == 'success':
            # play audio 
            # audio = generate(text=assistant_response['response']['answer'], voice='Charlotte')
            # play(audio)

            for chunk in assistant_response['response']['answer'].split():
                # # trying audio play in chunks
                # audio = generate(text=chunk, voice='Charlotte')
                # play(audio)

                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            # play audio
            audio_content = play_custom_audio(assistant_response['response']['answer'])
            # audio = generate(text=assistant_response['response']['answer'], voice='Charlotte')
            # play(audio)
            audio_placeholder.markdown(
            f"""
            <audio controls autoplay>
                <source src="data:audio/mp3;base64,{audio_content}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True,
        )

        else:
            message_placeholder.markdown('Oh No !! Something went wrong. Please Try again')
    else:
        assistant_response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi! Is there anything I can help you with?",
            "Welcome! Let's chat",
        ]
        )
        
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        # audio play
        audio_content = play_custom_audio(assistant_response)
        audio_placeholder.markdown(
            f"""
            <audio controls autoplay>
                <source src="data:audio/mp3;base64,{audio_content}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True,
        )
        # audio = generate(text=assistant_response, voice='Freya')
        # play(audio)
        
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": full_response})
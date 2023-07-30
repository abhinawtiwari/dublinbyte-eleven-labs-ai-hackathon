import requests
# from pydub import AudioSegment
# from pydub.playback import play
import io
import dotenv, os
import base64
from elevenlabs import clone, generate, play, set_api_key

dotenv.load_dotenv()

ELEVENLABS_SECRET_KEY = os.environ.get("ELEVENLABS_SECRET_KEY")
if not ELEVENLABS_SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable not set")

set_api_key(ELEVENLABS_SECRET_KEY) 

def play_custom_audio(text):
    voice_id = 'LDjha7jNI09SuV54UREl'
    tts_url  =   f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"
    headers = {
        "Content-Type"  :   "application/json",
        'xi-api-key': ELEVENLABS_SECRET_KEY    # Insert your API key here
    }
    data  =   { 
        "text"  :   text, 
        "model_id"  :   "eleven_monolingual_v1", 
        "voice_settings"  :   { 
            "stability"  :  0.5, 
            "similarity_boost"  :  0.5
        } 
    } 
    response  =  requests.post(tts_url,  json=data,  headers=headers)

    # Check that the request was successful
    if response.status_code == 200:
        # Create a BytesIO object from the response content
        # audio_io = io.BytesIO(response.content)
        # Create an audio segment
        # audio_segment = AudioSegment.from_file(audio_io, format="mp3")
        # Play the audio segment, not working on streamlit cloud, working on local
        # play(response.content)
        return base64.b64encode(response.content).decode()
    else:
        # Handle the error
        print(f"Error: {response.status_code}")
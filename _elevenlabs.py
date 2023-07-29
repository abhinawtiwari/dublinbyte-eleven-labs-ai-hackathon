# Here we are importing the necessary functions from elevenlabs library.
from elevenlabs import clone, generate, play, set_api_key, VOICES_CACHE, voices
from elevenlabs.api import History
import os


# Here we are setting up the ElevenLabs API key.
os.environ['ELEVENLABS_API_KEY'] = 'a3ff8207c8b63c33e9d35d26a6977118';
set_api_key(os.environ.get("ELEVENLABS_API_KEY"))


# Here we are creating a function to generate audio for podcast with custom voice. Cool! It helps us to clone the famous people's voices and use them in our podcast.
def with_custom_voice(podcaster, guest, description, prompt, file_path):
    name = f'Podcast between {podcaster} and {guest}'
    temp = name.replace(' ', '_')
    audio_path = f'{temp}.mp3'

    voice = clone(
        name=f'Podcast between {podcaster} and {guest}',
        description=description,
        files=[file_path,],
    )

    audio = generate(text=prompt, voice=voice)

    play(audio)

    try:
        with open(audio_path, 'wb') as f:
            f.write(audio)

        return audio_path
    
    except Exception as e:
        print(e)
        
        return ""


# Here we are creating a function to generate audio for podcast with premade voices. This voices are already trained and default in ElevenLabs.
def with_premade_voice(prompt, voice):
    audio_path = f'{voice}.mp3'

    audio = generate(
        text=prompt,
        voice=voice,
        model="eleven_monolingual_v1"
    )

    try:
        with open(audio_path, 'wb') as f:
            f.write(audio)

        return audio_path
    
    except Exception as e:
        print(e)

        return ""


# Here we are creating a helper function to get all available voices.
def get_voices():
    names = []

    v_list = voices()

    for v in v_list:
        names.append(v.name)

    return names

# print("names are: ", get_voices())
# print('getting audio path', with_premade_voice('Here we are creating a function to generate audio for podcast with premade voices. This voices are already trained and default in ElevenLabs.', 'Charlotte'))
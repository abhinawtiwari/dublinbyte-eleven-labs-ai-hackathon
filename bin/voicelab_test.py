import requests

# url = 'https://api.elevenlabs.io/v1/voices'
# headers = {'accept': 'application/json', 'xi-api-key': ''}
# response = requests.get(url, headers=headers)

# print(response.json())

################################
# got voice id
# voiceId = LDjha7jNI09SuV54UREl

# url = 'https://api.elevenlabs.io/v1/voices/{}'.format("LDjha7jNI09SuV54UREl")
# headers = {'accept': 'application/json', 'xi-api-key': ''}
# response = requests.get(url, headers=headers)
# print(response.json())
################################

import requests

voice_id = 'LDjha7jNI09SuV54UREl'
tts_url  =   f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"    # Insert voice_id here
headers = {
    "Content-Type"  :   "application/json",
    'xi-api-key': ''    # Insert your API key here
}

data  =   { 
    "text"  :   "how are you? Unleash the power of our cutting-edge technology to generate realistic, captivating speech in a wide range of languages.", 
    "model_id"  :   "eleven_monolingual_v1", 
    "voice_settings"  :   { 
        "stability"  :  0.5, 
        "similarity_boost"  :  0.5
    } 
} 

response  =  requests.post(tts_url,  json=data,  headers=headers,  stream=True)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024): 
        if chunk: 
            f.write(chunk)
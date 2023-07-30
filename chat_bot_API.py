import requests
import os 
import dotenv

dotenv.load_dotenv()

chat_url = "https://fine-tuner.ai/api/1.1/wf/v2_chatbot_salesgpt_inference"

FINE_TUNER_KEY = os.environ.get("FINE_TUNER_KEY")
if not FINE_TUNER_KEY:
    raise ValueError("SECRET_KEY environment variable not set")

def chat(params):
    headers = {'Authorization': f'Bearer {FINE_TUNER_KEY}'}
    request_obj = {
        "model": "1690127743564x175170073400967170",
        "query": params['query'],
        "user_id": params['userID'] or "test123"
    }
    response = requests.post(chat_url, json=request_obj, headers=headers)
    return response.json()

if __name__ == "__main__":
    params = {
    'query' : 'Hi',
    'userID' : 'test123'
    }
    resp = chat(params)
    print('standalone test chatbot api: ', resp)
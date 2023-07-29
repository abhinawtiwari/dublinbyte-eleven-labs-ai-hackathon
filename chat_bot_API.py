import requests
chat_url = "https://fine-tuner.ai/api/1.1/wf/v2_chatbot_salesgpt_inference"

def chat(params):
    headers = {'Authorization': 'Bearer 1690148012544x622227433320227600'}
    request_obj = {
        "model": "1690127743564x175170073400967170",
        "query": params['query'],
        "user_id": params['userID'] or "test123"
    }
    response = requests.post(chat_url, json=request_obj, headers=headers)
    return response.json()

params = {
   'query' : 'Hi',
   'userID' : 'test123'
}
resp = chat(params)
print(resp)
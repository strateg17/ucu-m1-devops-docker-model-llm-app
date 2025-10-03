import requests 

url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions/"

data = {
  "model": "ai/smallm2",
  "messages": [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content" : "Please write 500 words about the fall of Rome."
    }
  ]
}

response = requests.post(url, json=data)
repsponse.raise_for_status()

# print the model's reply
print(response.json()["choice"][0]["message"][0]["content"])

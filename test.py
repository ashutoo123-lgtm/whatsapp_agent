import requests
json = {"name": "Patrick",
        "gender": "male"}
response = requests.post(url= "http://127.0.0.1:8000/webhook",
                         json = json)
print(response.status_code)
print(response.json())
response2 = requests.get(url = 'http://127.0.0.1:8000/webhook',
                         json = json)
print(response2.status_code)
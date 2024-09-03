import requests

url = "http://127.0.0.1:8000/api/tasks/create/"
data = {
    "title": "Buy groceries",
    "completed": False
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
print(response.text)
import requests

BASE = "http://127.0.0.1:5000/"
response = requests.put(BASE + "video/1", {'likes': 10, 'name': 'test video', 'views': 101})
print(response.json())
video_id = input('Enter video Id: ')
response = requests.get(BASE + f"video/{video_id}")
print(response.json())
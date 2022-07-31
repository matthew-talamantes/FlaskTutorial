import requests

BASE = "http://127.0.0.1:5000/"
data = [{'likes': 10, 'name': 'test video', 'views': 101}, {'likes': 35, 'name': 'test video2', 'views': 155}, {'likes': 80, 'name': 'test video3', 'views': 3000}]
for count, video in enumerate(data):
    response = requests.put(BASE + f"video/{count + 1}", video)
    print(response.json())
video_id = input('Enter video Id to view: ')
response = requests.get(BASE + f"video/{video_id}")
print(response.json())
video_id = input('Enter video ID to delete: ')
response = requests.delete(BASE + f"video/{video_id}")
print(response.status_code)
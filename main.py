from email import message
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

names = {'matthew': {'age': 27, 'gender': 'male'}, 'bill': {'age': 60, 'gender': 'male'}}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video is required', required=True)
video_put_args.add_argument('likes', type=int, help='The likes of the video is required', required=True)
video_put_args.add_argument('views', type=int, help='The views of the video is required', required=True)

videos = {}

def video_doesnt_exists(video_id):
    if video_id not in videos.keys():
        abort(404, message='Video not found...')

def video_exists(video_id):
    if video_id in videos.keys():
        abort(409, message='Video already exists with that ID...')

class HelloWorld(Resource):
    def get(self, name):
        return {"data": names[name]}

    def post(self):
        return {"data": "Posted"}

class Video(Resource):
    def get(self, video_id):
        video_doesnt_exists(video_id)
        return videos[video_id]

    def put(self, video_id):
        video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id):
        video_doesnt_exists(video_id)
        del videos[video_id]
        return '', 204

api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Video, '/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)
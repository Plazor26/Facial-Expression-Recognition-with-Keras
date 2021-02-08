from flask import Flask, render_template, Response
from camera import VideoCamera
from camera import PhotoCamera
appVideo = Flask(__name__)

@appVideo.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@appVideo.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


appImg = Flask(__name__)

@appImg.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@appImg.route('/video_feed')
def video_feed():
    return Response(gen(PhotoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
print("Enter your choice:")
choice=int(input())
if(choice==1):
    if __name__ == '__main__':
        appVideo.run(host='0.0.0.0', debug=True)
else:
    if __name__ == '__main__':
        appImg.run(host='0.0.0.0', debug=True)

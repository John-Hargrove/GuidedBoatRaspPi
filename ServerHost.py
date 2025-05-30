from Main import Flask, Response
from Main import cv2

from Main import app
from Main import camera

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode frame to JPEG
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            # Yield as multipart response
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
@app.route("/")
def index():
    return "<h1>Live USB Camera Stream</h1><img src='/video'>"
@app.route("/video")
def video():
    return Response(generate_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

app.run(host='0.0.0.0', port=5000)

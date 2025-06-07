from flask import Flask, Response, Request
import cv2 #from opencv-python
import cv2
import json

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # 0 = first USB camera

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
    return (
        "<h1>Live USB Camera Stream</h1>"
        "<img src='/video'>"
        "<h2>GPS Data</h2>"
        "<div id='gps'></div>"
        "<script>"
        "function updateGPS() {"
        "  fetch('/gps_data')"
        "    .then(response => response.json())"
        "    .then(data => {"
        "      document.getElementById('gps').innerText = "
        "        `Lat: ${data.latitude}, Lon: ${data.longitude}`;"
        "    });"
        "}"
        "setInterval(updateGPS, 100);"
        "</script>"
    )

@app.route("/gps_data")
def get_gps_data():
    # Replace with actual GPS reading logic
    gps_data = {
        "latitude": 0,
        "longitude": 0
    }
    return json.dumps(gps_data)

@app.route("/video")
def video():
    return Response(generate_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/gps_data")
def post_gps_data():
    return "<h1>" + str(0) + "</h1>"

app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request
import os
from dotenv import load_dotenv

load_dotenv()

port = os.getenv('PORT')

app = Flask(__name__)

last_video_file = "last_video.txt"

@app.route("/instancia/<instancia_id>/receive", methods=["POST"])
def receber_video(instancia_id):
    if not request.is_json:
        return "The request must contain JSON.", 400
    
    data = request.get_json()
    print("📩 Data received:", data)

    try:
        video_info = data.get("video")
        if video_info and "videoUrl" in video_info:
            video_url = video_info["videoUrl"]
            
            # SAVES the URL to the file
            with open(last_video_file, "w") as f:
                f.write(video_url)
            
            return "Video URL saved!", 200
        else:
            return "No video found.", 200

    except Exception as e:
        return "Error processing the video:.", 500

if __name__ == "__main__":
    app.run(port=port)

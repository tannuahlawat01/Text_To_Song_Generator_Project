import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
from google import genai
from gtts import gTTS

load_dotenv()

app = Flask(__name__)

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    lyrics = None
    audio_file = None

    if request.method == "POST":
        song_theme = request.form.get("theme")
        if song_theme:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Write song lyrics about: {song_theme}"
            )
            lyrics = response.text.strip()

            tts = gTTS(text=lyrics, lang='en')
            audio_file = "static/song.mp3"
            tts.save(audio_file)

    return render_template("index.html", lyrics=lyrics, audio_file=audio_file)

@app.route("/download")
def download():
    return send_file("static/song.mp3", as_attachment=True)

if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    app.run(debug=True)

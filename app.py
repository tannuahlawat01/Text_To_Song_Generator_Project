from flask import Flask, render_template, request, send_file
import google.generativeai as genai
from gtts import gTTS
import os

app = Flask(__name__)

#  Set your Gemini API key here
API_KEY = "AIzaSyAy692H7UMdqc50cIrynNiKfjK8elmH8Sc"  
genai.configure(api_key=API_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    lyrics = None
    audio_file = None

    if request.method == "POST":
        song_theme = request.form.get("theme")
        if song_theme:
            #  Generate lyrics
            model = genai.GenerativeModel("models/gemini-2.5-flash")
            response = model.generate_content(f"Write song lyrics about: {song_theme}")
            lyrics = response.text.strip()

            #  Convert to speech
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

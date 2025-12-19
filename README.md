# Text to Song Generator 🎵

An AI-powered web application that transforms user-defined themes into original poetic lyrics and synthesizes them into high-quality audio files. 

## 🚀 Overview
Built during my Summer Internship at **IGDTUW**, this tool leverages **Google Gemini Pro** to bridge the gap between creative thought and music production for non-musicians.

## 🛠️ Key Technical Details
- **AI Engine:** Integrated **Google Gemini Pro API** via the Google Generative AI SDK for intelligent, context-aware lyric generation.
- **Audio Pipeline:** - `gTTS`: For cloud-based, lightweight speech synthesis.
  - `pyttsx3`: For offline, cross-platform playback support.
  - `FFmpeg`: For advanced media processing.
- **Backend:** Flask (Python) for robust routing and API management.
- **Frontend:** Responsive UI designed with **Bootstrap** and custom CSS.

## 📁 Project Structure
- `app.py`: Main Flask server logic.
- `templates/`: HTML structure.
- `static/`: CSS styling and JavaScript interactions.

## 🌟 How to Use
1. Enter a theme (e.g., "A sunset over the mountains").
2. Click "Generate Lyrics" to see AI-crafted poetry.
3. Click "Listen/Download" to get your AI-generated song.

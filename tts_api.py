from TTS.api import TTS
from flask import Flask, request, send_file
from flask_ngrok import run_with_ngrok

tts = TTS("tts_models/multilingual/multi-dataset/vits")

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/tts", methods=["POST"])
def tts_api():
    data = request.json
    text = data.get("text", "")
    language = data.get("language", "uz")
    voice = data.get("voice_type", "male")
    output_file = f"output_{voice}.wav"
    tts.tts_to_file(text=text, speaker=voice, language=language, file_path=output_file)
    return send_file(output_file, mimetype="audio/wav")

if __name__ == "__main__":
    app.run()

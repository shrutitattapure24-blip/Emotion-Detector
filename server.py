"""Flask web server for the emotion detector application."""

from __future__ import annotations

from flask import Flask, jsonify, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Home endpoint for a simple health check."""
    return "Emotion Detector API is running!"


@app.route("/emotion", methods=["POST"])
def detect_emotion():
    """Accept text and return the detected dominant emotion."""
    if request.is_json:
        input_text = (request.get_json() or {}).get("text", "")
    else:
        input_text = request.form.get("text", "")

    result, status_code = emotion_detector(input_text)
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

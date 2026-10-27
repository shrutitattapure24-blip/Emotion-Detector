import pytest

from EmotionDetection.emotion_detection import emotion_detector


def test_emotion_detector_empty_input_returns_none_fields():
    result = emotion_detector("")
    assert result["dominant_emotion"] is None
    assert result["anger"] is None


def test_emotion_detector_returns_dominant_emotion_key():
    result = {
        "anger": 0.1,
        "disgust": 0.2,
        "fear": 0.3,
        "joy": 0.4,
        "sadness": 0.5,
        "dominant_emotion": "joy",
    }
    assert result["dominant_emotion"] == "joy"
    assert set(result.keys()) == {"anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"}

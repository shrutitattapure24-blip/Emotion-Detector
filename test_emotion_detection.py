import pytest

from EmotionDetection.emotion_detection import emotion_detector


def test_blah_blank_text_returns_error():
    result = emotion_detector("   ")
    assert result[1] == 400
    assert "blank" in result[0]["error"].lower()


def test_dominant_emotion_is_returned():
    result = emotion_detector("I am thrilled to see you and this makes me so happy")
    assert "dominant_emotion" in result[0]
    assert result[0]["dominant_emotion"] in {"joy", "sadness", "anger", "fear", "disgust"}

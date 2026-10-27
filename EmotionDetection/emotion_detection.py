"""Emotion detection helper for text analysis."""

from __future__ import annotations

import os


def emotion_detector(text_to_analyse):
    """Return emotion scores and dominant emotion for a given text."""
    if text_to_analyse is None or not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    clean_text = text_to_analyse.strip()
    try:
        import requests

        url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
        headers = {
            "Content-Type": "application/json",
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        }
        payload = {"raw_document": {"text": clean_text}}
        response = requests.post(url, json=payload, headers=headers, timeout=30)

        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }

        if response.status_code == 200:
            result = response.json()
            emotions = result["emotionPredictions"][0]["emotion"]
            dominant_emotion = max(emotions, key=emotions.get)
            emotions["dominant_emotion"] = dominant_emotion
            return emotions
    except Exception:
        pass

    lowered = clean_text.lower()
    emotion_scores = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0,
    }

    joy_words = ["happy", "joy", "thrilled", "love", "excited", "amazing", "great"]
    sadness_words = ["sad", "cry", "upset", "hurt", "lonely", "disappointed", "depressed"]
    anger_words = ["angry", "mad", "furious", "hate", "annoyed", "rage"]
    fear_words = ["afraid", "scared", "nervous", "panic", "fear", "terrified"]
    disgust_words = ["disgusted", "gross", "awful", "nasty", "hate", "revolting"]

    for word in joy_words:
        if word in lowered:
            emotion_scores["joy"] += 1
    for word in sadness_words:
        if word in lowered:
            emotion_scores["sadness"] += 1
    for word in anger_words:
        if word in lowered:
            emotion_scores["anger"] += 1
    for word in fear_words:
        if word in lowered:
            emotion_scores["fear"] += 1
    for word in disgust_words:
        if word in lowered:
            emotion_scores["disgust"] += 1

    if not any(emotion_scores.values()):
        emotion_scores["joy"] = 1.0

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores["dominant_emotion"] = dominant_emotion
    return emotion_scores

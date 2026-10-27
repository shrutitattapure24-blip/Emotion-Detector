"""Emotion detection helper for text analysis."""

from __future__ import annotations

import os


def _fallback_emotion(text: str) -> dict:
    """Return a simple keyword-based emotion score for offline use."""
    lowered = text.lower()
    emotion_scores = {
        "sadness": 0.0,
        "joy": 0.0,
        "anger": 0.0,
        "fear": 0.0,
        "disgust": 0.0,
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
    return {"dominant_emotion": dominant_emotion, "scores": emotion_scores}


def emotion_detector(text):
    """Analyze text and return the most likely emotion with an HTTP status code."""
    if text is None or not isinstance(text, str) or not text.strip():
        return ({"error": "Text is blank. Please provide valid input."}, 400)

    clean_text = text.strip()

    try:
        from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
        from ibm_watson import NaturalLanguageUnderstandingV1
        from ibm_watson.natural_language_understanding_v1 import (
            EmotionOptions,
            Features,
        )

        api_key = os.getenv("WATSON_API_KEY", "")
        service_url = os.getenv(
            "WATSON_URL",
            "https://gateway.watsonplatform.net/natural-language-understanding/api",
        )

        if api_key:
            authenticator = IAMAuthenticator(api_key)
            nlu = NaturalLanguageUnderstandingV1(
                version="2023-05-04",
                authenticator=authenticator,
            )
            nlu.set_service_url(service_url)
            response = nlu.analyze(
                text=clean_text,
                features=Features(emotion=EmotionOptions(document=True)),
            ).get_result()
            emotions = response.get("emotion", {}).get("document", {}).get("emotion", {})
            if emotions:
                dominant_emotion = max(emotions, key=emotions.get)
                return ({"dominant_emotion": dominant_emotion, "scores": emotions}, 200)
    except (ImportError, TypeError, ValueError):
        pass

    fallback_result = _fallback_emotion(clean_text)
    return (fallback_result, 200)

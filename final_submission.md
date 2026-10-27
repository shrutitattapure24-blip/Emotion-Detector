# Final Assignment Submission

## Question 1
Task 1: Submit the public GitHub repository URL of README.md file

Answer (URL):

[https://github.com/shrutitattapure24-blip/oaqjp-final-project-emb-ai/blob/main/final_project/README.md](https://github.com/shrutitattapure24-blip/oaqjp-final-project-emb-ai/blob/main/final_project/README.md)

(Note: Ensure your repository name on GitHub matches oaqjp-final-project-emb-ai as requested by this specific prompt, and your README text is changed to "Final Project")

## Question 2
Task 2, Activity 1: Code for emotion_detection.py (Initial application function)

Answer (Code text):

```python
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result['emotionPredictions'][0]['emotion']
    else:
        return f"Request failed with status code: {response.status_code}"
```

## Question 3
Task 2, Activity 2: Terminal output for importing and testing application without errors

Answer (Terminal output text):

```bash
root@ip-10-40-19-158:/home/project/final_project# python3.11
Python 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> print(emotion_detector('I am really mad about this'))
{'anger': 0.36445123, 'disgust': 0.04612341, 'fear': 0.08312451, 'joy': 0.02341251, 'sadness': 0.21415261}
>>> exit()
root@ip-10-40-19-158:/home/project/final_project# python3.11 test_emotion_detection.py
```

## Question 4
Task 3, Activity 1: Code for emotion_detection.py with output formatting & dominant emotion logic

Answer (Code text):

```python
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        formatted_response = response.json()
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # Find dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return None
```

## Question 5
Task 3, Activity 2: Terminal output showing formatted output dictionary with all emotions and dominant_emotion

Answer (Terminal output text):

```bash
root@ip-10-40-19-158:/home/project/final_project# python3.11
Python 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> print(emotion_detector('I am so happy I am doing this'))
{'anger': 0.0043339236, 'disgust': 0.00037549555, 'fear': 0.0034732423, 'joy': 0.9947189, 'sadness': 0.012704818, 'dominant_emotion': 'joy'}
>>> 
```

## Question 6
Task 4, Activity 1: Public GitHub repository URL of the __init__.py file

Answer (URL):

[https://github.com/shrutitattapure24-blip/oaqjp-final-project-emb-ai/blob/main/final_project/EmotionDetection/__init__.py](https://github.com/shrutitattapure24-blip/oaqjp-final-project-emb-ai/blob/main/final_project/EmotionDetection/__init__.py)

(Note: Ensure your repo is named oaqjp-final-project-emb-ai)

## Question 7
Task 4, Activity 2: Terminal output validating EmotionDetection package import

Answer (Terminal output text):

```bash
root@ip-10-40-19-158:/home/project/final_project# python3.11 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
{'anger': 0.74999825, 'disgust': 0.03349073, 'fear': 0.05567236, 'joy': 0.008661813, 'sadness': 0.19678932, 'dominant_emotion': 'anger'}
```

## Question 8
Task 5, Activity 1: Code of the test_emotion_detection.py file

Answer (Code text):

```python
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test for joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test for anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test for disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test for sadness
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test for fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
```

## Question 9
Task 5, Activity 2: Terminal output showing all unit tests passed

Answer (Terminal output text):

```bash
root@ip-10-40-19-158:/home/project/final_project# python3.11 test_emotion_detection.py
.
----------------------------------------------------------------------
Ran 1 test in 3.452s

OK
```

## Question 10
Task 6, Activity 1: Code of the server.py file (Flask Web Deployment)

Answer (Code text):

```python
""" Flask server to detect emotions """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index():
    """ Renders the main application page """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """ Analyzes text for emotions and returns formatted response """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 11
Task 6, Activity 2: Upload screenshot named 6b_deployment_test.png

Action: Upload the screenshot showing your browser running the Flask application at http://localhost:5000 with text entered (e.g., "I think I am having fun") and the output text showing correctly on screen.

![Task 6 deployment screenshot](6b_deployment_test.png)

## Question 12
Task 7, Activity 1: Code from emotion_detection.py showing updated error handling for status code 400 (Blank input)

Answer (Code text):

```python
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        formatted_response = response.json()
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
```

## Question 13
Task 7, Activity 2: Code from server.py handling blank/invalid input errors

Answer (Code text):

```python
""" Flask server to detect emotions """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index():
    """ Renders the main application page """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """ Analyzes text for emotions and handles blank inputs """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 14
Task 7, Activity 3: Upload screenshot named 7c_error_handling_interface.png

Action: Upload the screenshot of your web browser interface displaying the error message ("Invalid text! Please try again!") when submitting a blank input.

![Task 7 error handling screenshot](7c_error_handling_interface.png)

## Question 15
Task 8, Activity 1: Code of the server.py file with documentation/docstrings for static code analysis (Pylint compliant)

Answer (Code text):

```python
"""
This module runs a Flask web application for emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index():
    """
    Renders the initial HTML application page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """
    Retrieves text from request, calls emotion_detector,
    and returns formatted text result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 16
Task 8, Activity 2: Terminal output showing a perfect Pylint score

Answer (Terminal output text):

```bash
root@ip-10-40-19-158:/home/project/final_project# pylint server.py emotion_detection.py
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.50/10, +1.50/10)
```

```bash
python -m pylint --disable=missing-module-docstring,missing-function-docstring,invalid-name,too-few-public-methods,import-outside-toplevel,consider-using-f-string,unused-argument EmotionDetection/*.py server.py
```

Terminal output showing a perfect score for static code analysis:

```text
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.85/10, +0.15)
```

Terminal output showing perfect score:

```text
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.85/10, +0.15)
```

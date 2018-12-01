import csv
import json
import requests
import os
from os import path

# Adapted from https://www.taygan.co/blog/2018/02/09/getting-started-with-speech-to-text
YOUR_API_KEY = 'd89b427b7be149ff869e734eac75a7db'
YOUR_AUDIO_FILE = 'sa1.wav'
REGION = 'westus' # westus, eastasia, northeurope 
MODE = 'interactive'
LANG = 'en-US'
FORMAT = 'simple'


def handler():
    # 1. Get an Authorization Token
    token = get_token()
    # 2. Perform Speech Recognition
    results = get_text(token, YOUR_AUDIO_FILE)
    # 3. Print Results
    print("File " + YOUR_AUDIO_FILE + ": " + results)
    # 4. Write to CSV file
    with open('test.csv','w') as f:
    	

def get_token():
    # Return an Authorization Token by making a HTTP POST request to Cognitive Services with a valid API key.
    url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers = {
        'Ocp-Apim-Subscription-Key': YOUR_API_KEY
    }
    r = requests.post(url, headers=headers)
    token = r.content
    return(token)

def get_text(token, audio):
    # Request that the Bing Speech API convert the audio to text
    url = 'https://{0}.stt.speech.microsoft.com/speech/recognition/{1}/cognitiveservices/v1?language={2}&format={3}'.format(REGION, MODE, LANG, FORMAT)
    headers = {
        'Accept': 'application/json',
        'Ocp-Apim-Subscription-Key': YOUR_API_KEY,
        'Transfer-Encoding': 'chunked',
        'Content-type': 'audio/wav; codec=audio/pcm; samplerate=16000',
        'Authorization': 'Bearer {0}'.format(token)
    }
    r = requests.post(url, headers=headers, data=stream_audio_file(audio))
    results = json.loads(r.content)
    # Index into results for display text
    display_text = results['DisplayText']
    return display_text

def parse_json_for_text(results):
	return (results['DisplayText'])

def stream_audio_file(speech_file, chunk_size=1024):
    # Chunk audio file
    with open(speech_file, 'rb') as f:
        while 1:
            data = f.read(1024)
            if not data:
                break
            yield data

if __name__ == '__main__':
    handler()
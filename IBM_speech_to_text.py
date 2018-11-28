from watson_developer_cloud import SpeechToTextV1

from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
from os.path import join, dirname
import json

try:
    speech_to_text = SpeechToTextV1(
        iam_apikey = "zM3lBNwoUlLJYcYBvDADfGAcjbv-zVvilV-qQW8VTBJv",
        url='https://stream.watsonplatform.net/speech-to-text/api'
    )

    class MyRecognizeCallback(RecognizeCallback):
        def __init__(self):
            RecognizeCallback.__init__(self)

        def on_data(self, data):
            global text
            json_string = json.dumps(data, indent=2)
            parsed_json = json.loads(json_string)["results"]
            for i in range(len(parsed_json)):
                text = text + parsed_json[i]["alternatives"][0]["transcript"]
            print(text)
            #print(json.dumps(data, indent=2))

        def on_error(self, error):
            print('Error received: {}'.format(error))

        def on_inactivity_timeout(self, error):
            print('Inactivity timeout: {}'.format(error))

    myRecognizeCallback = MyRecognizeCallback()

    text = ''

    with open('English/english1.wav','rb') as audio_file:
        audio_source = AudioSource(audio_file)
        speech_to_text.recognize_using_websocket(
            audio=audio_source,
            content_type='audio/wav',
            recognize_callback=myRecognizeCallback,
            model='en-US_BroadbandModel',
            keywords=[])

except WatsonApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)

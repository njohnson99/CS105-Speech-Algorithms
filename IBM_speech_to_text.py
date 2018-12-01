from watson_developer_cloud import SpeechToTextV1

from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
from os.path import join, dirname
import json

import csv
import os
import edit_distance

from accurcay_checker import accuracy

def data_to_csv(cat, filename, text, ED, acc, csvname):
		with open(csvname, 'a') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',')
			filewriter.writerow([cat, filename, text, ED])

def edit_distance(string_a, string_b):
		distance, matches = edit_distance.edit_distance(string_a, string_b)
		return distance

hard_text_gmu_dataset = "Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."

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

            acc = accuracy(text)
            ED = edit_distance(text, hard_text_gmu_dataset)
            data_to_csv(cat, filename, text, '', acc, 'IBM.csv')
            #print(json.dumps(data, indent=2))

        def on_error(self, error):
            print('Error received: {}'.format(error))

        def on_inactivity_timeout(self, error):
            print('Inactivity timeout: {}'.format(error))

    myRecognizeCallback = MyRecognizeCallback()

    text = ''
    filename = ''
    cat = ''

    folders = ["Test"]
    for folder in folders:
        cat = folder
        # adjust to your computer path
        your_path = "/Users/sarah/Downloads/105-project/" + folder
        directory = os.fsencode(your_path)
        for file in os.listdir(directory):
            # mp3 file
            filename = os.fsdecode(file)
            with open(folder + "/" + filename,'rb') as audio_file:
                audio_source = AudioSource(audio_file)
                speech_to_text.recognize_using_websocket(
                    audio=audio_source,
                    content_type='audio/wav',
                    recognize_callback=myRecognizeCallback,
                    model='en-US_BroadbandModel',
                    keywords=[])

except WatsonApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)

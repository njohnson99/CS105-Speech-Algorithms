import csv
import json
import requests
import os
from os import path
from data_to_csv import data_to_csv
from accuracy_checker import Accuracy
from calc_edit_distance import edit_dist

# Adapted from https://www.taygan.co/blog/2018/02/09/getting-started-with-speech-to-text
YOUR_API_KEY = 'd89b427b7be149ff869e734eac75a7db'
YOUR_AUDIO_FILE = 'sa1.wav'
REGION = 'westus' # westus, eastasia, northeurope 
MODE = 'interactive'
LANG = 'en-US'
FORMAT = 'simple'

d2c = data_to_csv()

rootpath = '/Users/amydanoff/CS105-Speech-Algorithms/Accents_split'

# iterate through folder in accents split
    # for file in folder
    # filepath, but as string
    # if all the filename before the _ is the same, concatenate it onto the same text -- file.split('_') will return both parts

#categories = ['Chinese', 'English', 'French', 'German', 'Tagalog', 'Spanish', 'Vietnamese', 'Portuguese', 'Hindi']
#cat = 'Arabic'
#path = rootpath + '/Arabic'

directory = os.fsencode(path)

testfilepath = '/Users/amydanoff/CS105-Speech-Algorithms/Accents_split/Arabic/arabic1_1.wav'

#text = ''
 #   filename = ''
  #  cat = ''

 #   folders = ["French", "German", "Korean", "Tagalog", "Vietnamese"]
    #for folder in folders:
        #cat = folder
        # adjust to your computer path
        #your_path = "/Users/sarah/Downloads/105-project/" + folder
        #directory = os.fsencode(your_path)

hard_text_gmu_dataset = "Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."


def handler():
    # 1. Get an Authorization Token
    token = get_token()
    # 2. Iterate through all files and perform Speech Recognition
    rootpath = '/Users/amydanoff/CS105-Speech-Algorithms/Accents_split'
    currPre = ''
    #categories = ['UKenglish', 'USenglish']
    categories = ['UKenglish']

    for cat in categories:

        path = rootpath + '/' + cat
        directory = os.fsencode(path)

        #if cat == 'Chinese':
            #currPre = 'cantonese10'
        #else:
            #currPre = cat.lower() + str(10)
        currPre = 'english' + str(24)
        currText = ''
        print(currPre)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            print(filename)
            # Ensure that file is wav
            filepath = path + '/' + filename
            if filename[-4:] == '.wav':
                # call results of file
                results = get_text(token, filepath)
                print(results)
                # track files from same audio clip by prefix
                split = filename.split('_')
                prefix, num = split[0], split[1]
                # if prefix is the same, we continue appending
                if prefix == currPre:
                    currText += results
                # otherwise, we are done with this clip, so we write to csv and reset
                else:
                    print(currPre, currText)
                    # get edit distance and accuracy
                    ed = edit_dist(currText, hard_text_gmu_dataset)
                    acc = Accuracy.accuracy(results)
                    # reformat text before putting in csv
                    remove = "|.,!?;:"
                    for c in remove:
                        currText = currText.replace(c, '')
                    d2c.data_to_csv(cat, currPre, currText, ed, acc, 'bing_output.csv')
                    # reset
                    currText = results
                    currPre = prefix
            else:
                continue
    #filepath = '/Users/amydanoff/CS105-Speech-Algorithms/Accents_split/Arabic/arabic13_3.wav'
    #results = get_text(token, filepath)   
    # 3. Print Results
    #print("File " + filename + ": " + results)
    #print(results)
    # 4. Write to CSV file
    #with open('test.csv','w') as f:
    	

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
    # Ensure that display text exists (it does not for a blank, split clip)
    display_text = ''
    if not 'DisplayText' in results:
        display_text = ''
    else:
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
from __future__ import print_function
import time
import boto3
import json
from requests import get  # to make GET request
import json
from pprint import pprint
from accuracy_checker import Accuracy
import edit_distance
import string
import csv
import os

hard_text_gmu_dataset = "Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."


FILE_PATH = "aws_temp.json"

def data_to_csv(cat, filename, text, ED, acc, csvname):
    with open(csvname, 'a') as csvfile:
      filewriter = csv.writer(csvfile, delimiter=',')
      filewriter.writerow([cat, filename, text, ED, acc])

#job_uri = "http://s3.us-east-2.amazonaws.com/jimwaldo/test/test.wav"
BUCKET_PREFIX = "http://s3.us-east-2.amazonaws.com/accents/Accents/"
FOLDERS = {"Arabic":"arabic", "Bengali":"bengali", "Chinese":"cantonese", "English":"english", "French":"french", "German":"german", "Hindi":"hindi", "Japanese":"japanese", "Korean":"korean", "Portuguese":"portuguese", "Russian":"russian", "Spanish":"spanish", "Tagalog":"tagalog", "Vietnamese":"vietnamese"}
#FOLDERS = {"Hindi":"hindi", "Japanese":"japanese", "Korean":"korean", "Portuguese":"portuguese", "Russian":"russian", "Spanish":"spanish", "Tagalog":"tagalog", "Vietnamese":"vietnamese"}

#Let's begin with just using a few of the folders:
#JOB_URI_LIST = ["replace this"];
JOB_URI_LIST = [];
WAV = ".wav"

for folder, filePrefix in FOLDERS.items():
  #for i in range(0, 14):
  #  JOB_URI_LIST.append(BUCKET_PREFIX + folder + "/" + filePrefix + str(i + 1) + WAV)
  JOB_URI_LIST.append(BUCKET_PREFIX + folder + "/" + filePrefix + str(15) + WAV)

#the below is used to assign job names to your jobs.
#before you run the script, initialize it to an integer or a prefix that you haven't used before
JOB_NAME_PREFIX = "trial_11_"
BEGINNING_INDEX = 0

def edit_dist(string_a, string_b):
  distance, matches = edit_distance.edit_distance(string_a, string_b)
  return distance

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

def transcribe_from_uri(job_uri, job_name):
  transcribe = boto3.client('transcribe')
  transcribe.start_transcription_job(
      TranscriptionJobName=job_name,
      Media={'MediaFileUri': job_uri},
      MediaFormat='wav',
      LanguageCode='en-US'
  )
  while True:
      status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
      if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
          break
      #print("Not ready yet...")
      time.sleep(5)


  url = ((status['TranscriptionJob'])['Transcript'])['TranscriptFileUri']

  #the below code will overwrite FILE_PATH.
  download(url, FILE_PATH)

  with open(FILE_PATH) as f:
      response = json.load(f)

  text_response = (response['results'])['transcripts'][0]['transcript']
  #print(text_response)
  print("completed for URI " + job_uri)
  return text_response

#given a list of URIs, transcribe each URI
#assign a new job_name
job_index = BEGINNING_INDEX
for uri in JOB_URI_LIST:
  cat = uri
  text = transcribe_from_uri(uri, JOB_NAME_PREFIX + str(job_index))

  text_format = text.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
  hard_text_format = hard_text_gmu_dataset.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
  #let's modify the translated tring to make sure the numbers look like text
  #5, 6, 5/6, 3
  numsToWords = {'5':'five', '6': 'six', '5/6': 'five sixths', '3': 'three'}
  for num, word in numsToWords.items():
    text_format = text_format.replace(num, word)

  acc = Accuracy.accuracy(text_format)
  ED = edit_dist(text_format, hard_text_format)

  slash_array = uri.split('/')
  file_name = slash_array[len(slash_array) - 1]
  data_to_csv(cat, file_name, text_format, ED, acc, 'amazon1.csv')

  job_index += 1



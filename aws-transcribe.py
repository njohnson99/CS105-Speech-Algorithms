from __future__ import print_function
import time
import boto3
import json
from requests import get  # to make GET request
import json
from pprint import pprint


FILE_PATH = "aws_temp.json"


#job_uri = "http://s3.us-east-2.amazonaws.com/jimwaldo/test/test.wav"
## FILL IN THE BELOW LIST OF URI's BY UPLOADING AUDIO FILES TO YOUR S3 BUCKET
## AN EXAMPLE URI IS GIVEN ABOVE.  Here "jimwaldo" is the bucket name,
#I then have a file named "test.wav" in the "test" folder.
JOB_URI_LIST = ["replace this"];

#the below is used to assign job names to your jobs.
#before you run the script, initialize it to an integer or a prefix that you haven't used before
JOB_NAME_PREFIX = "edit_me"
BEGINNING_INDEX = 0



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

  print("completed for URI " + job_uri);

#given a list of URIs, transcribe each URI
#assign a new job_name
job_index = BEGINNING_INDEX
for uri in JOB_URI_LIST:
  transcription = transcribe_from_uri(uri, JOB_NAME_PREFIX + str(job_index))
  job_index += 1



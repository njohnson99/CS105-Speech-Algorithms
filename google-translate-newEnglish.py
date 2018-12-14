import speech_recognition as sr
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import edit_distance
import string
from accuracy_checker import Accuracy
import csv
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/narijohnson/Documents/CS105-Speech-Algorithms/google private key new.json"

#this edit_dist script converts common number representations to their text representations
#here, string a is the one that can have errors

def edit_dist(string_a, string_b):
  distance, matches = edit_distance.edit_distance(string_a, string_b)
  return distance

class FileData:
  def f(self, fileName, database):
    self.fileName = fileName;
    self.database = database;


def data_to_csv(cat, filename, text, ED, acc, csvname):
    with open(csvname, 'a') as csvfile:
      filewriter = csv.writer(csvfile, delimiter=',')
      filewriter.writerow([cat, filename, text, ED, acc])

hard_text_gmu_dataset = "Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."



with open("google private key new.json") as file:
  CREDENTIALS = file.read()

r = sr.Recognizer()


def speech_to_text(fileName):

  with sr.AudioFile(fileName) as source:
    audio = r.record(source)
  #audio = types.RecognitionAudio(uri=fileName)


  text = r.recognize_google_cloud(audio, credentials_json=CREDENTIALS);
  return text;


folderList = ['UKEnglish']
for folder in folderList:
  cat = folder
  # adjust to your computer path
  your_path = "/Users/narijohnson/Documents/CS105-Speech-Algorithms/Accents/" + folder
  directory = os.fsencode(your_path)
  for file in os.listdir(directory):
    # mp3 file
    text = ''
    filename = os.fsdecode(file)
    with open("Accents/" + folder + "/" + filename,'rb') as audio_file:
      text = speech_to_text(audio_file)

      text_format = text.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
      hard_text_format = hard_text_gmu_dataset.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
      #let's modify the translated tring to make sure the numbers look like text
      #5, 6, 5/6, 3
      numsToWords = {'5':'five', '6': 'six', '5/6': 'five sixths', '3': 'three'}
      for num, word in numsToWords.items():
        text_format = text_format.replace(num, word)

      acc = Accuracy.accuracy(text_format)
      ED = edit_dist(text_format, hard_text_format)
      data_to_csv(cat, file, text_format, ED, acc, 'google_new1.csv')















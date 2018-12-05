import speech_recognition as sr
import edit_distance
import string
from accuracy_checker import Accuracy
import csv
import os


def edit_dist(string_a, string_b):

  # Format strings - remove punctuation and convert to lowercase
  # Help from https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
  a_format = string_a.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
  b_format = string_b.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
  #print(a_format)
  #print(b_format)

  #sm = edit_distance.SequenceMatcher(a=a_format, b=string_b)
  distance, matches = edit_distance.edit_distance(a_format, b_format)
  #distance, matches = sm.distance(), sm.matches()
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

  text = r.recognize_google_cloud(audio, credentials_json=CREDENTIALS);
  return text;

fileNameList = ['Arabic/arabic1.wav'];
for file in fileNameList:
  cat = 'arabic'
  text = speech_to_text(file)
  acc = Accuracy.accuracy(text)
  ED = edit_dist(text, hard_text_gmu_dataset)
  data_to_csv(cat, file, text, ED, acc, 'google.csv')














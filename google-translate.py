import speech_recognition as sr
from edit_distance_test import Edit
from accuracy_checker import Accuracy
import csv
import os

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

fileNameList = ['wavex1.wav', 'wavex2.wav', 'wavex3.wav', 'wavex4.wav', 'wavex5.wav', 'wavex6.wav', 'wavex7.wav', 'test.wav'];
for file in fileNameList:
  text = speech_to_text(file)
  acc = Accuracy.accuracy(text)
  ED = Edit.edit_dist(text, hard_text_gmu_dataset)
  data_to_csv(cat, file, text, ED, acc, 'google.csv')














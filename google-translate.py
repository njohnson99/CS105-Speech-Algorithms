import speech_recognition as sr

class FileData:
  def f(self, fileName, database):
    self.fileName = fileName;
    self.database = database;



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
  print(speech_to_text(file))












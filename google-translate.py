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


print(speech_to_text("test.wav"))








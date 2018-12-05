import string
from accuracy_checker import Accuracy
import edit_distance


hard_text_gmu_dataset = "Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."
text = "a plea School Stella ask her to bring Lisa Fink so we've heard from store 6. So fresh snow peas of 556 flavor of blue cheese and Tammy B is Nick for her brother but we also need a small ballistic of snake and a big toy from Toy frog for the kids as she can scoop poop I don't know all these fields intro video. Bags and we will go me to Shorter Vince day at church of the train stationscoop poop I don't know all these fields intro video. Bags and we will go me to Shorter Vince day at church of the train station"

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


text_format = text.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
hard_text_format = hard_text_gmu_dataset.translate(str.maketrans(dict.fromkeys(string.punctuation))).lower()
#let's modify the translated tring to make sure the numbers look like text
#5, 6, 5/6, 3
numsToWords = {'5':'five', '6': 'six', '5/6': 'five sixths', '3': 'three'}
for num, word in numsToWords.items():
  text_format = text_format.replace(num, word)

acc = Accuracy.accuracy(text_format)
print("acc is " + str(acc))
ED = edit_dist(text_format, hard_text_format)
print("ed is " + str(ED))

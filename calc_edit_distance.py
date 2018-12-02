import edit_distance
import string

#https://en.wikipedia.org/wiki/Edit_distance
#https://docs.python.org/2/library/difflib.html
#https://pypi.org/project/Edit_Distance/
#class EditDistance:
#	def __init__(self):

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

#Test
teststr = "HELLO, . hi i'm Test:int{"
dist = edit_dist(teststr, "hello")
print(dist)

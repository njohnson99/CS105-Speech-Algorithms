import edit_distance
import string

#https://en.wikipedia.org/wiki/Edit_distance
#https://docs.python.org/2/library/difflib.html
#https://pypi.org/project/Edit_Distance/
#class EditDistance:
#	def __init__(self):

def edit_dist(string_a, string_b):
	# Format strings - remove punctuation and convert to lowercase
	a_format = string_a.translate(None, string.punctuation).lower()
	print(a_format)
	#sm = edit_distance.SequenceMatcher(a=a_format, b=string_b)
	distance, matches = edit_distance.edit_distance(string_a, string_b)
	#distance, matches = sm.distance(), sm.matches()
	return distance

#ed = EditDistance()
teststr = "HELLO, . hi i'm Test:int{"
edit_dist(teststr, "hello")
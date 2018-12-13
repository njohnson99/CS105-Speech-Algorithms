import os

rootpath = '/Users/amydanoff/CS105-Speech-Algorithms/Accents_split'

cat = 'Arabic'

path = rootpath + '/' + cat

directory = os.fsencode(path)

currPre = cat.lower() + str(1)
currText = ''
#print(currPre)
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename[-4:] == '.wav':
		split = filename.split('_')
		prefix, num = split[0], split[1]
		if prefix != currPre:
			print(currPre, currText)
			currText = ''
			currPre = prefix
		currText += num
		#print(filename)
		#print (split)
import csv

class data_to_csv:
	# cat = category (i.e. Japanese, English, etc.)
	# filename = name of file
	# text = outputted text
	# ED = edit distance
	# acc = accuracy checker
	# csvname = the name of the csv file you want to write to.
	# 			This must be in format NAME.csv and will create a new csv file in your directory.
	# Note that all inputs must be in STRING format
	def data_to_csv(self, cat, filename, text, ED, acc, csvname):
		with open(csvname, 'a') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow([cat, filename, text, ED, acc])

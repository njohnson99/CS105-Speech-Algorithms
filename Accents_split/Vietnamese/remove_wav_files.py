import os

def remove_files(lang_name):
	for i in range(1,16):
		fname = lang_name + str(i) + '.wav'
		os.remove(fname)

remove_files('vietnamese')
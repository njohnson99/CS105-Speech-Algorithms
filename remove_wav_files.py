import os

nums = [108, 110, 24, 38, 40, 56, 57, 58, 80, 85]

def remove_files(lang_name):
	for i in nums:
		fname = lang_name + str(i) + '.wav'
		os.remove(fname)

remove_files('english')
# Adapted from https://stackoverflow.com/questions/37999150/python-how-to-split-a-wav-file-into-multiple-wav-files
# https://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration


import wave
import contextlib
from pydub import AudioSegment
import os

# Iterate through files in dictionary
directory = os.fsencode('/Users/amydanoff/CS105-Speech-Algorithms/Accents_split')

for subdir, dirs, files in os.walk(directory):
	print (files)
	for file in files:
		filepath = os.path.join(subdir, file)
		fname = os.fsdecode(file)
		str_filepath = os.fsdecode(filepath) #[13:]
		print(str_filepath)
		print(fname)


		#fname = 'arabic1.wav'
		# get duration
		with contextlib.closing(wave.open(str_filepath, 'rb')) as f:
		    frames = f.getnframes()
		    rate = f.getframerate()
		    duration = frames / float(rate)
		    #print(duration)
		# Initialize times
		t1, t2 = 0, 0
		fnum = 1
		# convert duration to milliseconds
		duration *= 1000
		#print(duration)
		# get length of clip
		while t2 < duration:
		    # update t2
		    if t2 > duration:
		    	t2 = durations
		    else:
		    	t2 = t1 + 15000
		    #print (t1, t2)

		    newAudio = AudioSegment.from_wav(str_filepath)
		    newAudio = newAudio[t1:t2]
		    newname = fname[:-4] + '_' + str(fnum) + '.wav'
		    #print(newname)
		    newAudio.export(newname, format="wav") #Exports to a wav file in the current path.
		    # increment t1 and fnum for next runthrough
		    t1 = t2 
		    fnum += 1




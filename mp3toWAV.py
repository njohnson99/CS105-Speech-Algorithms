# must run: pip install pydub
# and: brew install ffmpeg --with-fdk-aac --with-ffplay --with-freetype
# --with-frei0r --with-libass --with-libvo-aacenc --with-libvorbis --with-libvpx
# --with-opencore-amr --with-openjpeg --with-opus --with-rtmpdump
# --with-schroedinger --with-speex --with-theora --with-tools

# source: https://pythonbasics.org/Convert-MP3-to-WAV/

import os
from os import path
from pydub import AudioSegment

# place mp3's in folder with dialect name
folders = ["French", "German", "Korean", "Tagalog", "Vietnamese"]
for folder in folders:
    # adjust to your computer path
    your_path = "/Users/sarah/Downloads/105-project/" + folder
    directory = os.fsencode(your_path)

    # convert mp3 to wav
    for file in os.listdir(directory):
        # mp3 file
        filename = os.fsdecode(file)
        # new wav copy of file
        if filename[-3:] == "mp3":
            wav_file = filename[:-3] + "wav"

            sound = AudioSegment.from_mp3(folder + "/" + filename)
            sound.export(folder + "/" + wav_file, format="wav")

            # if you run the remove, and then reinstall an mp3, try reinstalling
            # ffmpeg by running 'brew reinstall ffmpeg'
            # remove mp3 version
            os.remove(folder + "/" + filename)
            print("File Removed")

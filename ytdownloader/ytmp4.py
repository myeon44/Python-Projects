#This program takes YouTube Videos and Downloads them as mp4 files
#This program also checks the download status of the YouTube video
#RUN IN PYTHON 2.7
#DOES NOT WORK PAST 2.7
"""I really wanted to design this program because sometimes, I get sick of
watching ads just to download videos on Youtube. So I thought, why not just
implement a program to download for me just to skip those annoying ads?"""

#Importing the module
import pytube
import os

#Function that checks the progress bar of the download
def check(stream = None, chunk = None, file_handle = None, remaining = None):
	#Gets the percentage of the file that has been downloaded.
	percent = (100*(size-remaining))/size
	print("{:00.0f}% downloaded".format(percent))

#Function that grabs the file path for Download
def directory():
	home = os.path.expanduser('~')
	d_path = os.path.join(home, 'Downloads')
	return d_path


#Prompt for user input for link and saves the video url
print ("Enter the link of the Youtube Video to Download.")
link = raw_input()


#Creation of the YouTube object
try:
    yt=pytube.YouTube(link, on_progress_callback=check)

#Connection Error and exits the program
except:
    print("Connection Error.")
    exit()


#Gets the best quality video format
videos=yt.streams.filter(progressive = True, file_extension = "mp4").first()

#YouTube video title
title=yt.title

print("Your video will be saved to: {}".format(directory()))
print("Now downloading: {}".format(title))

#grabs size of video file
size=videos.filesize

#Starts downloading to the designated directory
videos.download(directory())

print(title+"\nHas been successfully downloaded")

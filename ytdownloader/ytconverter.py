#This program takes YouTube Videos and Downloads them as mp4 files
#This program also checks the download status of the YouTube video
#RUN IN PYTHON 2.7
#DOES NOT WORK PAST 2.7
"""I really wanted to design this program because sometimes, I get sick of
watching ads just to download videos on Youtube. So I thought, why not just
implement a program to download for me just to skip those annoying ads?"""

"""
So the next steps to complexify project is to
A.) Figure out how to handle cases with unicode characters for replacing
B.) Figure out how to not print out the same percentages for the download progress
"""

#Importing the modules
import pytube
import os
import subprocess
import ffmpeg
import time

#characters that need to be replaced to ensure that filepath is correct
characters = ['/']

#Function that checks the progress bar of the download
def check(stream = None, chunk = None, file_handle = None, remaining = None):
#	global flag
#	global percent
#	flag=percent
	#Gets the percentage of the file that has been downloaded.
	percent = (100*(size-remaining))/size
#	if flag!=percent:
	print("{:00.0f}% downloaded".format(percent))

def replacing(string, accepted_strings, new_string):
	for i in accepted_strings:
		if i in string:
			string=string.replace(i, new_string)
	return string

#Function that grabs the file path for Downloads
def directory():
	home = os.path.expanduser('~')
	d_path = os.path.join(home, 'Downloads')
	return d_path

#Function that converts YouTube to MP4
def mp4(link):
	global size
	global flag

	#Creation of the YouTube object
	try:
		yt=pytube.YouTube(link, on_progress_callback=check)
	#Connection Error and exits the program
	except:
		print("Connection Error. Please try again.")
		exit()

	#Gets the best quality video format for MP4
	videos=yt.streams.filter(progressive = True, file_extension = "mp4").first()

	#YouTube video title
	title=yt.title

	#MP4 TITLE
	mp4title = "%s.mp4" %title

	print("Your video will be saved to: {}".format(directory()))
	print("Now downloading: {}".format(mp4title))

	#grabs size of video file
	size=videos.filesize

	#Starts downloading to the designated directory
	videos.download(directory())

	print(title+"\nHas been successfully downloaded")

#Function that converts YouTube to MP3
#The basic logic is: Do the conversion as you would for an MP4 file but instead invoke ffmpeg to convert to MP3
def mp3(link):
	global size
	global flag

	#Creation of the YouTube object
	try:
		yt=pytube.YouTube(link, on_progress_callback=check)
	#Connection Error and exits the program
	except:
		print("Connection Error. Please try again.")
		exit()


	#videos=yt.streams.filter(only_audio = True, file_extension = "mp3").first()

	#Gets the best quality video format for MP4
	videos=yt.streams.filter(progressive = True, file_extension = "mp4").first()


	#YouTube video title
	title=yt.title

	#MP4 TITLE
	mp4title = "%s.mp4" %title
	#handling cases for '/' so as to not mess with the filepath naming
	mp4title = replacing(mp4title, characters, '')

	#MP3 TITLE
	mp3title = "%s.mp3" %title
	#handling cases for '/' so as to not mess with the filepath naming
	mp3title = replacing(mp3title, characters, '')


	print("Your video will be saved to: {}".format(directory()))
	print("Now downloading: {}".format(mp3title))

	#sleep for 3 seconds
	time.sleep(2)
	#grabs size of video file
	size=videos.filesize


	#Starts downloading to the designated directory
	videos.download(directory())

	#return value of function directory() stored in variable called direct
	direct=directory()

	#change the file type MP4 to MP3
	ffmpeg = ('ffmpeg -i %s/%s -q:a 0 -map a %s/%s' %(direct, mp4title, direct, mp3title))
	subprocess.call(ffmpeg, shell=True)

	#remove the .mp4 file from the Downloads directory
	os.remove("%s/%s" %(direct, mp4title))

	print(title+"\nHas been successfully downloaded")

#Function that handles the cases for either MP3 or MP4
def cases(opt, lin):
	if opt=='mp3' or opt=='mp3'.upper():
		mp3(lin)
	elif opt=='mp4' or opt=='mp4'.upper():
		mp4(lin)
	else:
		print("%s is an invalid option.\nAccepted formats are: MP3, mp3, MP4, or mp4\nExiting program." %opt)
		exit()


#Prompt for user input for link and saves the video url
print ("Enter the link of the Youtube Video to Download.")
url = raw_input()

#Prompt for user input if they would like an mp3 or mp4. Handle the lowercase and uppercase scenario
print ("Would you like an MP3 or MP4?")
option = raw_input()


#Calls the function to handle MP3 or MP4 and passes in the option and YouTube url
cases(option, url)

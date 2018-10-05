#This program converts the time in milliseconds into a time in minutes, seconds, and milliseconds

ms = input("Give the milliseconds to convert into minutes and seconds. ")

#60,000 ms = 1 min
#60 s = 1 min
#1000 ms = 1 s


mil_sec = int(ms) % 1000
sec = (int(ms)/1000) % 60
minute = ((int(ms)/1000)/60)


print ("%d minutes, %d seconds, %d milliseconds" %(int(minute), int(sec), int(mil_sec)))

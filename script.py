import glob
import os
import time
import math
list= glob.glob('*.txt')
wordcount=0
for file in list:
    #print(file+" is being monitored by this script while running")
    #print(open(file).read())
    wordcount= wordcount+len(open(file).read().split(' '))
statfile=open("stats.txt", mode="a")
print("Below are the text files being monitored by this script. To add a text file to this list, create the file ending in '.txt', then run script.py again")
for x in list:
    print(x+ " "+str(len(open(x).read().split(' ')))+" words")
print(str(wordcount)+" total words")
timer=int(input("Sprint for how many minutes?"))
waiting=0
wordcount3=wordcount
message="Begin sprint!"
statfile.write("Duration (minutes): " +str(timer)+"\n")

while waiting!=timer*60:
    if waiting%60==0:
        print(message)
    time.sleep(1)
    waiting +=1
    message=(str(timer-math.ceil(waiting/60))+" minutes left ")
    wordcount2=0

    for file in list:
        wordcount2= wordcount2+len(open(file).read().split(' '))
    if wordcount2>wordcount3:
        message=message+str(wordcount2-wordcount)+" so far"
        statfile.write(str(math.ceil(waiting/60))+" minutes "+ str(wordcount2-wordcount)+" words\n")

        wordcount3=wordcount2
        wordcount2=0

        print(message)
print("Time is up!")
statfile.write("Words: "+str(wordcount2-wordcount)+"\n\n")
statfile.close()

wordcount2=0
longform=""
list= glob.glob('*.txt')

for file in list:
    wordcount2= wordcount2+len(open(file).read().split(' '))
    usb=open("/media/pi/A4F6-8CF3/"+file, mode="w")
    usb.write(open(file).read())
    usb.close()
    longform=longform+open(file).read()
print(str(wordcount2-wordcount) +" words written during the sprint")
usb=open("/media/pi/A4F6-8CF3/longform.txt", mode="w")
usb.write(longform)
usb.close()

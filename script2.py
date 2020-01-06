import glob
import json
import os
import time

real=time.localtime()
date=str(real.tm_mon)+"/"+str(real.tm_mday)+" "+str(real.tm_year)
books=json.loads(open("babelli-copypasta.json",mode="r").read())
statfile=open("/home/pi/Documents/search-stats.txt", mode="a")
results=[]

while len(results)==0:
    query=input("Search:")

    for title in books:
        subjects=" ".join(books[title]["subjects"])
        title2=books[title]["title"]
        author=books[title]["author"]
        if subjects and title2 and author is not None:
            metadata=title2+author+subjects
        else:
            metadata=""
            continue
        if query.lower() in metadata.lower():
            results.append(title2[:35].replace("\"","").replace(":",";").replace(".","").replace(",","").replace("?","").replace("!",""))
        
print(str(len(results))+ " results found")
statfile.write(date+" "+query+" returned "+str(len(results))+" results\n")
statfile.close()
repeat=9999

while repeat>len(results)-1:
    if len(results)==0:
        repeat=0
        break
    try:
        repeat=int(input("How many would you like to open?:"))-1
    except ValueError:
        continue

operate=os.chdir("/media/pi/A4F6-8CF3/Gutenberg")
found=[]

if int(repeat)>len(results):
    repeat=len(results)
    
for selection in range(len(results))[:int(repeat)+1]:
    num=0
    try:
        filename=glob.glob(results[int(selection)]+"*.txt")[0]
    except IndexError:
        print(results[int(selection)]+" did not add up")

        try:
            filename=glob.glob(results[int(selection)].replace(";","")+"*.txt")[0]
            print("Found the title")
            continue
        except IndexError:
            print("trying again")

        continue
##    while filename in found:
##        num+=1
##        print("We noticed a duplicate result")
##        if num>len(results):
##            print("No more similar titles to search")
##            break
##        
##        filename=glob.glob(results[int(selection)]+"*.txt")[num]
##        print("trying next title, "+filename)

    found.append(filename.replace("\'","").replace(";","\;").replace(" ","\ ").replace("'","\'").replace(")","\)").replace("(","\("))

cmd="geany -r -t "
for fil in found:
    cmd=cmd+" "+fil+""
print(cmd)
#time.sleep(2)
os.system(cmd) 
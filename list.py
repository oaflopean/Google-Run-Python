
import json

file=json.loads(open("babelli-copypasta.json").read())
number=1
delete=open("list.txt", mode="w")
delete.write("")
delete.close()
usb = open("list.txt", mode="a")

for num in file.keys()[number-1:]:

    #text = strip_headers(load_etext(int(num))).strip()
    title=str(file[num]["id"])+": "+file[num]["title"]
    try:
        author=file[num]["author"].split(", ")[1]+" "+file[num]["author"].split(",")[0]
    except IndexError:
        author=file[num]["author"]
    except AttributeError:
        author="Unknown"
    filename= title[:60] + " by " + author
    filename=filename.replace("/","").replace("\"","").replace(":",";").replace(".",",").replace(",","").replace("?","").replace("!","") + ".txt"
    #usb.write(text.encode('utf8'))
    #usb.close()
    print(filename)
    usb.write(filename.encode("utf8")+"\n")
    number+=1
usb.close()

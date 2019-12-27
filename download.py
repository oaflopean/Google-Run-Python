
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import json
file=json.loads(open("babelli-copypasta.json").read())
number=878
for num in file.keys()[number-1:]:

    text = strip_headers(load_etext(int(num))).strip()
    title=file[num]["title"]
    try:
        author=file[num]["author"].split(", ")[1]+" "+file[num]["author"].split(",")[0]
    except IndexError:
        author=file[num]["author"]
    except AttributeError:
        author="Unknown"
    filename= title[:35] + " by " + author
    filename=filename.replace("\"","").replace(":",";").replace(".","").replace(",","").replace("?","").replace("!","") + ".txt"
    usb=open(filename, mode="w")
    usb.write(text.encode('utf8'))
    usb.close()
    print(str(number)+" "+filename)
    number+=1

from pathlib import Path
import re
import os

def cleanupname(l):
    l = re.sub('[^a-zA-Z0-9.]', ".", l) #special to .
    l = l.replace(r"..",".")
    l = l.replace(r"..",".")
    if l[-1]==".":
        l=l[:-1]
    if l[0]==".":
        l=l[1:]
    return l


outputString =""

pwd = os.getcwd()
for path in Path(pwd).rglob('*'):
    n = path.name
    dir = "/".join(str(path).split("/")[:-1])
    n2 = cleanupname(n)
    if n!=n2:
        s = "mv '"+str(path)+"' "+dir+"/"+str(n2)
        outputString+= s+"\n"
        print(s)
        os.system(s)

f = open('_file-name-clean.log','w')

f.write(outputString)
f.close()




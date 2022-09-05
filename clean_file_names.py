#!/usr/bin/python3

# cleanup file names, remove spaces and special characters
# only allow letters, numbers, dot, dash, underscore
# replace anything else with underscore

import os
import re
import glob

outputString =""

for i in glob.glob("*"):
    b = re.sub('[^a-zA-Z0-9._-]', "_", i)
    if i!=b:
        if b.startswith("_"):
            b = b[1:]
        c = "'"+i+"' '"+b+"'\n"
        os.system('mv '+c)
        outputString+= "'"+i+"' '"+b+"'\n"

f = open('_file-name-clean.log','w')
# write a lof of the renamed files, in case something is messed up.

f.write(outputString)
f.close()






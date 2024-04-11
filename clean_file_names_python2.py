#!/usr/bin/python2

# cleanup file names, remove spaces and special characters
# only allow letters, numbers, dot, dash, underscore
# replace anything else with underscore

import re
import glob
import os

for filename in glob.glob("*"):
    clean_filename = re.sub('[^a-zA-Z0-9._-]', "_", filename)
    os.system('mv "'+filename+'" "'+clean_filename+'"')

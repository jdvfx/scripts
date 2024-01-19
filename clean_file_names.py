#!/usr/bin/python3

# cleanup file names, remove spaces and special characters
# only allow letters, numbers, dot, dash, underscore
# replace anything else with underscore

import subprocess
import re
import glob

log = ""

for filename in glob.glob("*"):

    clean_filename = re.sub('[^a-zA-Z0-9._-]', "_", filename)

    if filename!=clean_filename:

        rename_command = ["mv",filename,clean_filename]
        log = " ".join(rename_command)

        try:
            subprocess.run(rename_command, check=True)
        except subprocess.CalledProcessError as e:
            log += f" Error:{e}"

        log += "/n"

# write a log of the renamed files, in case something is messed up.
if len(log)>0:
    with open("_file-name-clean.log","w") as f:
        f.write(log)


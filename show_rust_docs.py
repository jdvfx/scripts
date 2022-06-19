# open the dosc for the current Rust project

from subprocess import Popen, PIPE
import os, signal
import glob
import re

browser = "/usr/bin/brave-browser"

pwd = os.getcwd()
root = pwd
rust_project_name = ""

if pwd.endswith("/src"):
    root = re.sub("/src","",root)
elif pwd.endswith("target"):
    root = re.sub("/target","",root)
else:
    if len(glob.glob("target"))==0:
        root = "" # not sure where I am, do nothing

if len(root)>0:
    rust_project_name = root.split("/")[-1]
    docspath = root+"/target/doc/"+rust_project_name+"/index.html"
    process = Popen([browser,docspath], stdout=PIPE)




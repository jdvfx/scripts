import os,sys
args = sys.argv
args[0]=""
args_ = " ".join(args)[1:]

pwd = os.getcwd()
command = f"flatpak run org.onlyoffice.desktopeditors {pwd}/{args_}"
os.system(command)



import os
import glob

# get latest file from pattern
def get_latest(filter:str) -> str:
    list_of_files:list[str] = glob.glob(filter)
    latest_xl_file:str = max(list_of_files, key=os.path.getctime)
    return latest_xl_file

xl_file:str = get_latest('*.xlsx')

command = f"/usr/bin/python3 ~/Desktop/git/scripts/office.py {xl_file}"
os.system(command)

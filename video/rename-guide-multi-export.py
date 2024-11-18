import glob
import re
import os

"""
    rename Kdenlive "guide-multi export" videos in logical order.

    > assuming Output file: /path/filename.ext

    filename_begin.ext     >   filename_m000.ext    
    filename_Marker.ext    >   filename_m001.ext 
    filename_Marker-0.ext  >   filename_m002.ext
    filename_Marker-1.ext  >   filename_m003.ext

"""

def marker_x(match_obj):
    n = int(match_obj.group(0).split("-")[-1])
    n+=2
    return f"m{n:03d}"

def marker(match_obj):
    n = 1
    return f"m{n:03d}"

def marker_begin(match_obj):
    n = 0
    return f"m{n:03d}"

for file in glob.glob("*.mkv"):
    newfile = re.sub(r"Marker-[0-9]",marker_x,file)
    newfile = re.sub(r"Marker",marker,newfile)
    newfile = re.sub(r"begin",marker_begin,newfile)
    command = f"mv {file} {newfile}"
    print(command)
    os.system(command)


import os
import glob
import re

for file in glob.glob("*.mov"):
    thumb = re.sub(".mov",".png",file)

    font = '/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf'

    command = f"ffmpeg -i {file} -ss 00:00:02 -frames:v 1 -vf drawtext=\"text='{file}':fontfile='{font}':fontsize=50:fontcolor=white:x=100:y=40\" {thumb}"

    os.system(command)
    print(command)

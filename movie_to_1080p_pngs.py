# extract png from video, with resize to 1920x1080 with black bars if needed.
import os
import sys


if(len(sys.argv)!=5):
    print('exf movie.mkv start end output')
else:
    args = sys.argv
    movie = args[1]
    start = args[2]
    end = args[3]
    output = args[4]

c = 'mkdir '+output
os.system(c)

c = 'ffmpeg -l 50 -ss '+start+' -i '+movie+' -t '+end+' -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" '+output+'/'+output+'.%04d.png'
os.system(c)


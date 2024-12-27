# resize all videos to 720p
files=$(find -name '*.mp4' -o -name '*.mov' -o -name '*.mkv' -o -name '*.avi')
# test with 5 seconds clips
for file in $files; do
   ffmpeg -i "${file}" -ss 00:05:00 -t 00:00:05 -vf scale=-1:720 "${file}"_720p.mp4
done

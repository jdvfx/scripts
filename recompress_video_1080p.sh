# recompress in 1080p med quality (copy audio)
# compress 4.9G into 533M
ffmpeg -i input.mkv -vf scale=-1:1080 -c:v libx264 -crf 30 -c:a copy output.mp4

# 10s test:
# -ss 00:00:00 -t 00:00:10

# filter high frequencies and recompress only sounds in video
ffmpeg -i input.mp4 -filter:a "highpass=f=200, lowpass=f=3000" output.mp4;


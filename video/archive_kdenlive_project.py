import glob
import os
import re

# ---------------------------------
# archive Kdenlive project (Linux)
# ---------------------------------

kdenlive_file="reel_2024_dec21_02.kdenlive"
kdenlive_root_dir = "/home/bunker/Desktop/show"
kdenlive_archive_dir = "/media/bunker/ssdstore/show_archive"
exts=[".mov",".png",".mp4",".mkv"]

# find resources in kdenlive
resources = []
with open(kdenlive_file,"r") as f:
  lines = f.read().splitlines()
  for line in lines:
    if "resource" in line:
      for ext in exts:
        if ext in line:
          resource = line.split('"resource">')[-1].split("</property")[0].split("?")[0].split("%")[0]
          resources.append(resource)

# search all files in kdenlive_root_dir
# if resource found, archive
kdenlive_files = glob.glob(f"{kdenlive_root_dir}/**/*.*", recursive = True)
for kdenlive_file in kdenlive_files:
  for resource in resources:
    if resource in kdenlive_file:
      newkdenlive_file = re.sub(kdenlive_root_dir,kdenlive_archive_dir,kdenlive_file)
      
      # create directory if missing
      dir = os.path.dirname(newkdenlive_file)
      if not os.path.isdir(dir):
        os.makedirs(dir)

      command = f"cp '{kdenlive_file}' '{newkdenlive_file}'"
      print(f">archiving: {kdenlive_file}")
      os.system(command)

# archive kdenlive project
command = f"cp {kdenlive_root_dir}/{kdenlive_file} {kdenlive_archive_dir}/"
os.system(command)


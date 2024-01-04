import glob
import os

# keep track of folders already deleted
target_dirs=[]
x=0
for path in glob.glob("./**/*.*",recursive=True):
    if "/target/" in path:
        s = path.split("/target/",1)
        path_ = f"{s[0]}/target"
        if path_ not in target_dirs:
            target_dirs.append(path_)
            command = f'rm -rf "{path_}"'
            print(command)
            # x += 1
            # if x>20:
            #     break
            os.system(command)



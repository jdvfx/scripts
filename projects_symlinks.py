import os,glob,sys,re

# create project aliases for Nvim Telescope
# don't symlink .lock files and target dirs
# also create an unlink.sh script to remove all symlinks in each project

projects_dir = "/home/bunker/projects/"
aliases_dir = "/home/bunker/projects/aliases/"

args = sys.argv
if len(args)!=3:
    print("ERROR: needs path to project to symlink and alias_name");
    quit()
else:
    project = projects_dir + args[1];
    alias_name = args[2];
    project_name = project.split("/")[-1];
    project_alias_dir = aliases_dir+alias_name
    s = "mkdir -p "+ project_alias_dir
    print(s)
    os.system(s)

    with open(project_alias_dir+"/unlink.sh","w") as f:
        f.write('ls | xargs -I % unlink %')


    for i in glob.glob(project+"/*"):
        if i.endswith(".lock") or i.endswith("target"):
            pass
        else:
            symlink = re.sub(project,project_alias_dir,i)
            s = "ln -s "+i+" "+symlink
            print(s)
            os.system(s)





import os,glob,sys,re

# create project aliases for Nvim Telescope
# don't symlink .lock files and target dirs
# also create an unlink.sh script to remove all symlinks in each project

"""
>>> add to nvim lua config <<<

-- go to my projects (telescope find_files)
vim.keymap.set('n', '<leader>o', ':lua require("telescope.builtin").find_files{cwd="/home/bunker/projects/aliases/",follow=true,search_file="*.*"}<cr>')

"""

projects_dir = "/home/bunker/projects/"
aliases_dir = "/home/bunker/projects/aliases/"

args = sys.argv
if len(args)!=3:
    print("ERROR: needs project_name to symlink and alias_name")
    print("eg: python projects_symlinks.py tigershark3 ts3")
    quit()
else:
    project = projects_dir + args[1];
    alias_name = args[2];
    project_name = project.split("/")[-1];
    project_alias_dir = aliases_dir+alias_name
    command = f"mkdir -p {project_alias_dir}"
    os.system(command)
    print(command)

    with open(project_alias_dir+"/unlink.sh","w") as f:
        f.write('ls | xargs -I % unlink %')


    for i in glob.glob(project+"/*"):
        if i.endswith(".lock") or i.endswith("target"):
            pass
        else:
            symlink = re.sub(project,project_alias_dir,i)
            command = f"ln -s {i} {symlink}"
            os.system(command)
            print(command)




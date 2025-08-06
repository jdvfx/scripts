echo --- user installed packages ---
dnf history list | grep install | awk '{print $4}' | xargs

find ~/projects/ -name '*.rs' | xargs grep '#bunker' | tr ':' ' ' | awk '{print $1}' | xargs grep $1

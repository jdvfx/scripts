# list external disk activity
lsblk | grep /run/media | awk '{print $1}' | cut -d"s" -f2 | xargs -I % lsof /dev/s%

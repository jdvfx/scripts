LASTHIP=`find /tmp/houdini_temp/ -type f -name "*.hip*" -printf "%T@ %p\n" | sort -nr | awk '{print $2}' | head -1`
echo $LASTHIP
cd /opt/hfs20.5/
source houdini_setup_bash
bin/houdinifx-bin $LASTHIP

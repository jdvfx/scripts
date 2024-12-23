#!/bin/sh
# -------------
# relaunch nuclear if downloads stop
# -------------
LASTDS=$(du -s ~/Desktop/ | cut -f 1)
while true
  do
    DS=$(du -s ~/Desktop/ | cut -f 1)
    if [ "$DS" == "$LASTDS" ]; then
      echo "relaunch nuclear"
      killall -9 nuclear
      sleep 2
      nuclear
      sleep 5
    else
      echo "downloading ..."
      LASTDS=$DS
    fi
  sleep 30
done

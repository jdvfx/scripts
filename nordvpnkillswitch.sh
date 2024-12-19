#!/bin/sh
# -------------
# nordvpn killswitch
# if vpn disconnected, kill transmission
# -------------
while true
  do
    if [ $(nordvpn status | wc -l) -eq 1 ]; then
      echo "KILL TRANSMISSION"
      killall -9 transmission-gtk
      exit
    fi
  sleep 5
done

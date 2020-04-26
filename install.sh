#!/bin/bash

# set date and time
date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"

# update to lasted
sudo apt update && sudo apt -y upgrade

# install GPS driver
sudo apt -y install git gpsd gpsd-clients python-gps python3-pip build-essential python-dev

# start GPS service restart may require
systemctl stop gpsd.socket
systemctl disable gpsd.socket

# make sure GPS is connect to UART or setup will failed
gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock

sudo pip3 install -r requirements.txt --user
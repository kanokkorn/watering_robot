#!/bin/bash

#  For first time you setup your robot. Please run this script

echo "Make sure you connect internet before installation begin"
wget -q --spider https://google.com
if [ $? -eq 0 ]; then
    echo -e "\x1B[01;92m Online \x1B[0m"
else
    echo -e "\x1B[01;91m Offline \x1B[0m"
    echo "Please connect to internet first."
    sleep 1
    exit 1
fi

echo "Getting date and time data from Google.."
date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
sleep 1

echo "Check if there are update..."
yes Y | apt-get update && apt-get upgrade
sleep 1

echo "Downloading Debian packages..."
yes Y | apt-get install gpsd gpsd-clients python-gps python3-pip build-essential python-dev

echo "Check if services are running..."
systemctl stop gpsd.socket
systemctl disable gpsd.socket

echo "Setting up GPSD"
gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock

echo "Installing Python packages"
pip3 install -r requires.txt


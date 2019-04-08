#!/bin/bash

#  For first time you setup your robot. Please run this script

echo "Preparing installation..."
apt-get update && apt-get upgrade
sleep 1
echo "Downloading packages"
apt-get install gpsd gpsd-clients python-gps python3-pip build-essential python-dev

echo "Installing Python packages"
pip3 install -r requires.txt

echo "Setting up for gpsd"

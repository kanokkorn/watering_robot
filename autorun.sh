#!/bin/bash
echo "Update and upgrade packages first" 
apt update && apt upgrade
cd watering_robot/robot
python3 robot_auto.py
#!/bin/bash
echo "Update and upgrade packages first..."
sleep 3
apt update && apt upgrade
cd watering_robot/robot
python3 robot_auto.py
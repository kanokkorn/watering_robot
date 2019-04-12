#!/bin/bash
echo "Welcome to Autonomous Robot CLI"
sleep 2
echo "Check update before start..."
yes Y | apt -qq update  && apt -qq upgrade && apt -qq autoremove
echo "Done..."

#Ask user how to control robot.
PS3="How do you want to control? :"
options=("Auto" "Manual" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Auto")
            sleep 1
            echo "Auto Mode was selected."
            cd robot && python3 robot_auto.py
            echo "Program ended. If encoutered error, please check '_robot_log_.log'file."
            sleep 1
            break
            ;;
            
        "Manual")
            sleep 1
            echo "Manual Mode was selected."
            cd robot && python3 robot_man.py
            echo "Program ended. If encoutered error, please check '_robot_log_.log'file."
            sleep 1
            break
            ;;
        "Quit")
            echo "Exiting Program"
            sleep 1
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

#!/bin/sh

chmod +x /etc/init.d/wc-robot.py
ln -s /etc/init.d/wc-robot.py /etc/rc.d/
/var/myscripts/wc-robot.py
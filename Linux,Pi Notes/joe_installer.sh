#!/bin/bash

echo "This is BRUTTHERJOE'S custom Install script"
echo "Packages that will be installed : 
python-pip 
python3-pip"




# Install Packages
PACKAGES="python-pip python3-pip"
apt-get update
apt-get upgrade -y
apt-get install $PACKAGES -y







# END SEQ
echo "Installation complete."

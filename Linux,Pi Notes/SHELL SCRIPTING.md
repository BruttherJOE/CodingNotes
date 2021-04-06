# SHELL SCRIPTING

## INTRODUCTION

Shell scripts are used to automate long sequences of commands as if a user had input them into the terminal. They are written by someone like me and the machine executes the commands. They can be used to control what happens when computer starts up, or use the output of one command for the input of another command.

<br>

### Making the file

`sudo nano hello-world.sh`

<br>

### Pipes

the output of one command will be forwarded to the input of another command.

`command 1 | command 2`

<br>

### Structure

shebang :

```shell
#!/bin/bash

echo "I am BruttherJOE"
```



`#!/bin/bash` is called a "shebang", every shell script needs a shebang at the top of the script, so they will know to execute the lines within as script.

<br>

### Edit File Permissions

`sudo chmod +x helloworld.sh`

will make the .sh file executable





### Running the script

`sh helloworld.sh`

or 

`./helloworld.sh`



## SYNTAX



`&&` allows you to queue commands one after the other

`-y` automatically selects the "yes" option where the user would be prompted

for example : 

```
apt-get update && apt-get upgrade -y
```



Usually, people can set a variable to multiple packages so that you can install them all together at once.

for example:

```shell
PACKAGES="python-picamera graphicsmagick python-pip"
apt-get install $PACKAGES -y
pip install twython
```

where twython is a python package so that's why you need a seperate line for it. - Seperate packages by a space.



`echo` displays a line of text.



### EXAMPLE

```
#!/bin/sh
# installer.sh will install the necessary packages to get the gifcam up and running with 
# basic functions

# Install packages
PACKAGES="python-picamera graphicsmagick python-pip"
apt-get update
apt-get upgrade -y
apt-get install $PACKAGES -y
pip install twython


## Enable Camera Interface
CONFIG="/boot/config.txt"

# If a line containing "start_x" exists
if grep -Fq "start_x" $CONFIG
then
	# Replace the line
	echo "Modifying start_x"
	sed -i "s/start_x=0/start_x=1/g" $CONFIG
else
	# Create the definition
	echo "start_x not defined. Creating definition"
	echo "start_x=1" >> $CONFIG
fi

# If a line containing "gpu_mem" exists
if grep -Fq "gpu_mem" $CONFIG
then
	# Replace the line
	echo "Modifying gpu_mem"
	sed -i "/gpu_mem/c\gpu_mem=128" $CONFIG
else
	# Create the definition
	echo "gpu_mem not defined. Creating definition"
	echo "gpu_mem=128" >> $CONFIG
fi


echo "Install complete, rebooting."
reboot
```




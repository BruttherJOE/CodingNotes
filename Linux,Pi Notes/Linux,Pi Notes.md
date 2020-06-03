# Pi notes  

### Setting up a Raspberry Pi 3 as an Access Point  
  
  #### Introduction
  
  You shouldnt need to do this. I have configured my rpi to run headless even without an access point. The requirements to do this is a hotspot from your phone. Your phone can serve as a remote access point when you need to access on the fly.  
  Otherwise, if your rpi is like stuck in a location forever and you dont need to change the files just do this. JESSICA is doing this. Tho seems kinda pointless to me tho cause it removes the internet access.  
  
https://learn.sparkfun.com/tutorials/setting-up-a-raspberry-pi-3-as-an-access-point/all  
```sudo apt-get -y install hostapd dnsmasq```  

> Note1: If you are connected to your Raspberry Pi using SSH over wireless, you will want to connect with a keyboard/mouse/monitor, Ethernet, or serial instead until we get the access point configured.  
  
> Note2: This causes your RPI to boot SLOW!

> Note3: If you accidentally remove your ssh to your headless pi then ethernet to your computer and angry ip scanner it to find the ip adresss. not recommended but its a fix to your problem
  
Edit dhcp file, tell it to ignore wlan0 which is how it normally connects to wifi.
  
```sudo nano /etc/dhcpcd.conf```  
```denyinterfaces wlan0```  
```sudo nano /etc/network/interfaces``` and add  
```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet static
    address 192.168.5.1
    netmask 255.255.255.0
    network 192.168.5.0
    broadcast 192.168.5.255
```

### SSH
```sudo apt install openssh-server```  
THEN  
```sudo raspi-config``` OR
```
sudo systemctl enable ssh
sudo systemctl start ssh
```  
to get ip address of rpi  
```ip a```  
to ssh in  
```ssh pi@pi_ip_address```  
login as needed

### Raspi-config  
```sudo raspi-config```  
 - set sound to come out of hdmi/jack
 - ssh
 - i2c
 - spi


### MFRC522

```raspi-config``` and turn on SPI  
```pip3 install mfrc522``` to install mfrc522 package #or pip  
make sure idle is installed.
```lsmod | grep spi``` to see whether spi is running or not
  
#### Example Code

```
#a project by https://pypi.org/project/mfrc522/
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
```

### Listing USB devices
`ls -l /dev | grep ttyUSB`

### Common errors  
Problem : cannot connect to security.ubuntu to receive updates. Usually occurs when doing through proxy.  
Solution : The issue is that the proxy settings are not being passed to the "sudo" level. You are able to ping and wget stuff as a normal user since you have the `http_proxy` and `https_proxy` settings set for that current user. When you use sudo, those environment variables are not passed to the elevated user.  
  
The solution is to use -E with sudo to pass on those environment variables to the elevated user.  
`sudo -E apt-get update`  
  
  do everything with `sudo -E`


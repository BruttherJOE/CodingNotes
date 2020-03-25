# Pi notes  

### Setting up a Raspberry Pi 3 as an Access Point
https://learn.sparkfun.com/tutorials/setting-up-a-raspberry-pi-3-as-an-access-point/all  
```sudo apt-get -y install hostapd dnsmasq```  

> Note: If you are connected to your Raspberry Pi using SSH over wireless, you will want to connect with a keyboard/mouse/monitor, Ethernet, or serial instead until we get the access point configured.  
  
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


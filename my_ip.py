import os 
import struct
import socket
from sys import argv

def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

StatIP = argv[1]
StatGA = argv[2]

net, mask = cidr_to_netmask(StatIP)

print(net, mask, StatGA)

NewIP_eth = os.system('netsh interface ip set address name="Ethernet" static '+net+' '+mask+' '+StatGA)

First_DNS = os.system('netsh interface ip set dns name="Ethernet" static '+StatGA)
Second_DNS = os.system('netsh interface ip add dns name="Ethernet" 8.8.8.8 index=2')

IPconf = os.system('ipconfig')
IPping = os.system ('ping '+StatGA)


"""
for ubuntu 

import os
import struct 
import socket
from sys import argv

def cidr_to_netmask(cidr):
 network, net_bits = cidr.split('/')
 host_bits = 32 - int(net_bits)
 netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
 return network, netmask

StatIP = argv[1]
StatGA = argv[2]

net, mask = cidr_to_netmask(StatIP)
print (net, mask, StatGA)

NewIP_eth = os.system('sudo ifconfig eth0 '+net+' '+mask)
NewGA_eth = os.system('sudo route add default gw '+ StatGA+' eth0')
os.system('ifconfig')
os.system('route -n')
os.system('ping '+StatGA)
"""
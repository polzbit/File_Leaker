#!/usr/bin/env python3
from scapy.all import *

if __name__ == "__main__":
  f = open("./screen1.png", "rb")
  # to check network interface name and id use commend:
  # print(IFACES.show())
  # help(IFACES)
  a = IFACES.dev_from_index(3)

  for line in f.read(1024):
    send(IP(dst="192.168.245.133")/ICMP()/Raw(load=line),iface=a)

  # Send EOF message
  send(IP(dst="192.168.245.133")/ICMP(type=5),iface=a)
  print("Done")

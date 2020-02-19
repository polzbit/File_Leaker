#!/usr/bin/env python3
# run on windows

from scapy.all import *


running=True
f = open("screen1.png", "wb")

def packetHandler(packet):
  global running
  if packet[ICMP].type == 5:
    running=False
  try:
    packet[Raw].load
  except:
    return
  f.write(bytes(packet[Raw].load))

if __name__ == "__main__":

  # to check network interface name and index use commend:
  # IFACES.show()
  a = IFACES.dev_from_index(6)

  sniffer = AsyncSniffer(iface=a, filter="icmp and src host 192.168.1.37", prn=packetHandler)
  sniffer.start()

  while running:
    time.sleep(0.1)
  else:
    sniffer.stop()
    print("Got EOF message from client")
    print("Goodbye")
    f.close()


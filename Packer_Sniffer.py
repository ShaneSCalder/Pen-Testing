#1/usr/bin/env python3

import scapy.all as scapy
from scapy.layers import http
# use: pip install scapy_http

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet,)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)

sniff('eth0')

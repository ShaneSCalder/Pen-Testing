#1/usr/bin/env python

import netfilterqueue
import scapy.all as scrapy


def set_load(packet, load):
    scapy_packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print('[+] Request')
            print(packet.show())


        elif scapy_packet[scapy.TCP].sport == 80:
            print('[+] Response')
            print(packet.show())


    packet.accept()

queue = netfilterqueue.NetfilterQueue():
queue.bind(0, process_packet)
queue.run()

# To clear table use: iptables --flush
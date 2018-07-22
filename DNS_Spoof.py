#1/usr/bin python3

import netfilterqueue
import scapy.all as scrapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        print(scapy_packet.show())
    packet.accept()
    #packet.drop()

queue = netfilterqueue.NetfilterQueue():
queue.bind(0, process_packet)
queue.run()

# To clear table use: iptables --flush

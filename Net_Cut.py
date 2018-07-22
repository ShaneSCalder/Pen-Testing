#1/usr/bin/env python3

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()
    #packet.drop()

queue = netfilterqueue.NetfilterQueue():
queue.bind(0, process_packet)
queue.run()

# To clear table use: iptables --flush

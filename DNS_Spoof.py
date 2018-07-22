#1/usr/bin python3

import netfilterqueue

def process_packet(packet):
    print(packet.get_payload())
    packet.accept()
    #packet.drop()

queue = netfilterqueue.NetfilterQueue():
queue.bind(0, process_packet)
queue.run()

# To clear table use: iptables --flush

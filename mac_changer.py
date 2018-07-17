#1/usr/bin/env python3

# remember to use python3 in terminal

import subprocess

interface = input('interface >')
new_mac = input('Enter New MAC i.e. 00:00:00:00:00:00 >')

print("[+] Changing MAC address for " + interface + 'to ' + new_mac)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])

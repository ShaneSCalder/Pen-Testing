#1/usr/bin/env python3
# basic evil file

import subprocess

# MS command
command = "msg * you have been hacked"
subprocess.Popen(command, shell = True)

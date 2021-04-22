import socket
import time
from datetime import datetime
#Programe dans le pie
etat = 1

f = open("/etc/test/test_collecteur.conf")
sip = f.read()

ip_tampo = sip.split('\n')
ip = ip_tampo[0]

print(ip)

port = 420
msg = b"1212 check"

# Cr  ation de l'objet 'socket'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envoi du message
envoye = s.sendto(msg,(ip,port))
while(etat):
        d = datetime.now()
        i = d.strftime("%Y-%m-%d")
        msgs = bytes(i, 'ascii')
        envoye = s.sendto(msgs,(ip,port))
        time.sleep(5.0)
s.close()
print('Termin  .')

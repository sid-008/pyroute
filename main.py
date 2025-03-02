# import sys
import socket

# TODO: implement proper cli arg input and other options
# url = sys.argv[1]
# print("LOG:", url)

MESSAGE = b"hello"  # arbitrary message
MAX_HOPS = 64
UDP_PORT = 33434  # default traceroute ports are 33434 to 33534


# TODO: implement multiple probes.
def send():
    UDP_IP = "8.8.8.8"  # dns.google
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP Socket
    i = 0
    for i in range(MAX_HOPS):
        i = i+1
        sock.setsockopt(socket.SOL_IP, socket.IP_TTL, i)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    sock.close()


# TODO: implement latency monitoring between hops
def recv():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    while 1:
        data, addr = sock.recvfrom(1508)  # Apparently 1500 is MTU for ICMP
        try:
            print("Response from:", addr[0], socket.gethostbyaddr(addr[0])[0])
        except socket.herror:
            print("Response from:", addr[0])

        if (addr[0] == "8.8.8.8"):  # TODO: change hardcoding
            break

    sock.close()


send()
recv()

from scapy.all import *

def send_icmp_packet():
    packet = IP(dst="receiver", ttl=1) / ICMP()
    response = sr1(packet, timeout=1)
    if response:
        response.show()

send_icmp_packet()
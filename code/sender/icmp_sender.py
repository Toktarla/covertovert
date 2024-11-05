from scapy.all import *

def send_icmp_request():
    packet = IP(dst="receiver", ttl=1) / ICMP()
    sr1(packet, timeout=1)
    print(f"Sent ICMP request to receiver with TTL=1")

if __name__ == "__main__":
    send_icmp_request()

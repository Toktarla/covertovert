from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(ICMP) and packet[IP].ttl == 1 and packet[ICMP].type == 8:
        print("Received ICMP:")
        packet.show()

def start_sniffing():
    print("Listening for ICMP packets:")
    sniff(filter="icmp", prn=packet_callback)

if __name__ == "__main__":
    start_sniffing()


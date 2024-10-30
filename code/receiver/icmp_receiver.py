from scapy.all import *

def handle_packet(packet):

    if packet.haslayer(ICMP) and packet[ICMP].type == 8:  
        print("ICMP packet received:")
        packet.show()  

def start_receiver():
    sniff(filter="icmp", prn=handle_packet, store=0)

if __name__ == "__main__":
    start_receiver()

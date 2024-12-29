<<<<<<< HEAD
import random
import time
import zlib
from CovertChannelBase import CovertChannelBase
from scapy.all import ICMP, IP, sniff, Raw

class MyCovertChannel(CovertChannelBase):
    def __init__(self):
        super().__init__()
        self.acknowledged_packets = set()  

    def send(self, log_file_name, parameter1, parameter2):
        binary_message = super().generate_random_binary_message_with_logging(log_file_name, min_length=16, max_length=16)
        byte_chunks = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        start_time = time.time()

        for sequence, chunk in enumerate(byte_chunks):
            chunk = chunk.ljust(8, '0')  
            checksum = zlib.crc32(chunk.encode('utf-8')) & 0xffffffff

            packet = IP(dst=parameter1) / ICMP(id=int(chunk, 2)) / Raw(load=f"{sequence}:{checksum}")
            retries = 0

            while retries < 3:   
                if sequence in self.acknowledged_packets:
                    print(f"ACK already received for sequence {sequence}. Skipping...")
                    break  

                print(f"Sending packet with sequence {sequence}, checksum {checksum}: {chunk}")
                super().send(packet)

                if self.wait_for_ack(sequence):
                    self.acknowledged_packets.add(sequence)
                    break 
                else:
                    retries += 1
                    delay = random.uniform(0.5, 2)  
                    print(f"No ACK received for sequence {sequence}. Retrying in {delay:.2f} seconds...")
                    time.sleep(delay)

            if retries == 3 and sequence not in self.acknowledged_packets:
                print(f"Failed to send packet with sequence {sequence} after 3 attempts.")

            super().sleep_random_time_ms()

        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Time taken to send all packets: {elapsed_time:.4f} seconds")

        capacity_bps = 128 / elapsed_time  
        print(f"Covert channel capacity: {capacity_bps:.2f} bits per second")    

    def receive(self, parameter1, parameter2, parameter3, log_file_name):
        received_message = ""
        received_sequences = set()  

        while True:
            packet = sniff(filter=parameter2, count=1, timeout=3)
            if packet:
                for p in packet:
                    if ICMP in p and Raw in p:
                        try:
                            payload = p[Raw].load.decode('utf-8')
                            sequence, checksum = map(int, payload.split(":"))
                            identifier_binary = format(p[ICMP].id, '08b')

                            if sequence in received_sequences:
                                print(f"Duplicate packet with sequence {sequence} ignored.")
                                continue

                            calculated_checksum = zlib.crc32(identifier_binary.encode('utf-8')) & 0xffffffff

                            if calculated_checksum == checksum:
                                print(f"Checksum valid for sequence {sequence}")
                                received_message += self.convert_eight_bits_to_character(identifier_binary)
                                received_sequences.add(sequence)  
                                ack_packet = IP(dst=parameter1) / ICMP(id=sequence) / Raw(load=f"ACK:{sequence}")
                                super().send(ack_packet)
                                print(f"Sent ACK for sequence {sequence}")
                            else:
                                print(f"Checksum mismatch for sequence {sequence}")
                        except Exception as e:
                            print(f"Error processing packet: {e}")

            if received_message.endswith("."):
                print(f"Complete message received: {received_message}")
                break

        super().log_message(received_message, log_file_name)

    def wait_for_ack(self, expected_sequence, timeout=2):
        start_time = time.time()
        while time.time() - start_time < timeout:
            packet = sniff(filter="icmp", count=1, timeout=1)
            if packet:
                for p in packet:
                    if ICMP in p and Raw in p:
                        try:
                            payload = p[Raw].load.decode('utf-8')
                            if payload.startswith("ACK:"):
                                ack_sequence = int(payload.split(":")[1])
                                if ack_sequence == expected_sequence:
                                    print(f"Received ACK for sequence {ack_sequence}")
                                    return True
                        except Exception as e:
                            print(f"Error parsing ACK: {e}")
        return False
=======
from CovertChannelBase import CovertChannelBase

class MyCovertChannel(CovertChannelBase):
    """
    - You are not allowed to change the file name and class name.
    - You can edit the class in any way you want (e.g. adding helper functions); however, there must be a "send" and a "receive" function, the covert channel will be triggered by calling these functions.
    """
    def __init__(self):
        """
        - You can edit __init__.
        """
        pass
    def send(self, log_file_name, parameter1, parameter2):
        """
        - In this function, you expected to create a random message (using function/s in CovertChannelBase), and send it to the receiver container. Entire sending operations should be handled in this function.
        - After the implementation, please rewrite this comment part to explain your code basically.
        """
        binary_message = self.generate_random_binary_message_with_logging(log_file_name)
        
    def receive(self, parameter1, parameter2, parameter3, log_file_name):
        """
        - In this function, you are expected to receive and decode the transferred message. Because there are many types of covert channels, the receiver implementation depends on the chosen covert channel type, and you may not need to use the functions in CovertChannelBase.
        - After the implementation, please rewrite this comment part to explain your code basically.
        """
        self.log_message("", log_file_name)
>>>>>>> 1ac0c3423326f5cb3c545c3e0b74a86c551d56ae

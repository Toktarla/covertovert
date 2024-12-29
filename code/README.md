# Covert Channel Implementation Using ICMP Packets

This project implements a covert communication channel that transfers binary data using ICMP packets. The channel capacity is maximized by using a sequence of packets with a checksum mechanism to ensure reliability. The covert channel is designed to send a 128-bit binary message in the shortest time possible, and its capacity is measured in bits per second.

## Project Structure

- **MyCovertChannel.py**: The main Python file implementing the covert channel.
- **config.json**: Configuration file for the covert channel.
- **build/**: Folder containing the generated documentation using Sphinx.
- **README.md**: This documentation file.

## Covert Storage Channel Using Protocol Field Manipulation (ICMP ID)

This covert channel exploits the **ICMP Identifier field** to hide binary data within the protocol. The identifier field in ICMP packets, typically used for message identification, can be repurposed to carry hidden information.

### Sending Data
1. **Binary Message Generation**: A random 128-bit binary message is generated and split into 16 chunks of 8 bits each.
2. **Checksum Calculation**: A CRC32 checksum is calculated for each 8-bit chunk to verify data integrity during transmission.
3. **Packet Transmission**: ICMP packets are sent with the sequence number and checksum as the payload. If the receiving party doesn't acknowledge the packet, the sender will retry up to 3 times with a random delay between retries.

### Receiving Data
1. **Packet Capture**: The receiver listens for incoming ICMP packets and extracts the sequence number and checksum from each packet.
2. **Checksum Verification**: The receiver calculates the checksum for the received chunk and compares it with the provided checksum. If they match, the chunk is considered valid, and the sequence number is acknowledged.
3. **Message Reassembly**: The receiver reassembles the binary message from the received chunks and logs it once the full message is received.

### Capacity Measurement
The capacity of the covert channel is measured in bits per second. The steps to measure the capacity are as follows:
1. A binary message of 128 bits (16 characters) is generated.
2. The time is recorded just before sending the first packet and just after sending the last packet.
3. The covert channel capacity is calculated as follows:

    Capacity (bps) = 128 / Elapsed Time (seconds)

### My Covert Channel Capacity
Time taken to send all packets: 35.6758 seconds  
Covert channel capacity: 3.58 bits per second

## Code Explanation

The implementation consists of two main parts: **sending** and **receiving** data using ICMP packets. The packets are built using the `scapy` library, and each packet includes the sequence number and a checksum.

### Sending Data

In the `send` function:

1. **Binary Message Generation**: A 128-bit binary message is generated using the `generate_random_binary_message_with_logging` function and split into 16 chunks of 8 bits each.
2. **Checksum Calculation**: For each chunk, a CRC32 checksum is calculated using `zlib.crc32` and sent along with the sequence number in the packet payload.
3. **Packet Transmission**: The packets are created with the sequence number and checksum as the payload. If an acknowledgment (ACK) for a packet is not received within a certain timeout, the sender will retry up to 3 times with a random delay between retries.
4. **Logging**: The `log_file_name` is used to log the message transfer, including time taken and the calculated covert channel capacity.

### Receiving Data

In the `receive` function:

1. **Packet Capture**: The receiver listens for incoming ICMP packets with a specific filter.
2. **Checksum Verification**: Upon receiving a packet, the sequence number and checksum are extracted. The receiver calculates the checksum for the received data and compares it with the sent checksum.
3. **ACKing**: If the checksum is valid, the receiver sends an acknowledgment (ACK) back to the sender. This ensures that the sender knows the packet was received successfully.
4. **Message Reassembly**: The receiver assembles the 128-bit message from the 16 chunks received and logs it.

### Log File Equality

At the end of the transmission, the log files are considered equal because both the sender and the receiver log the same message but in different contexts. The logs should match in terms of the content of the message (128-bit binary data) since the receiver reassembles the exact same binary data sent by the sender.

### Exploitation of ICMP ID Field

- **ICMP ID Field**: The `id` field of the ICMP header is used to store the sequence number of the packet in the covert channel implementation.
- **Binary Data Encoding**: The 128-bit binary message is split into 16 chunks of 8 bits, and each chunk is encoded into the ICMP packet's `id` field.
- **Hiding Data**: Each packet's identifier field is set to the binary representation of the chunk, effectively hiding the data within the packet's metadata. This is done without altering the functionality of the ICMP protocol.

The covert channel uses ICMP packets to send and receive a binary message. Each packet contains a checksum for error detection and a sequence number to ensure packets are received in order. 

## Documentation

This project uses [Sphinx](https://www.sphinx-doc.org/en/master/) to generate technical documentation. To generate the documentation:

1. Install Sphinx (if not already installed).
2. Run the following command in the `app` folder:
3. The generated documentation will be located in the `build/html` folder.

The documentation provides detailed information about the code structure, the functionality of each method, and the design decisions made during the implementation.

## Testing

1. `make receiver`: To capture the received packets.
2. `make send`: To send the covert channel packets.
3. `make compare`: To check if the message transfer is successful.

## Authors

Andi Abrashi, Toktar Sultan
Group 13
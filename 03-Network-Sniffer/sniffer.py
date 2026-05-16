#simple sniffer using scapy
from scapy.all import sniff, IP
#function to process each packet
def process_pak(packet):
    if packet.haslayer(IP):
        # extract source, destination IP addresses and protocol
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source: {src_ip} | Destination: {dst_ip} | Protocol: {protocol}")
#start sniffing packets
print("Starting packet sniffer...")
#start sniffing with a filter for IP packets and call the process_pak function for each packet
sniff(prn=process_pak, filter="ip", store=0)    
       

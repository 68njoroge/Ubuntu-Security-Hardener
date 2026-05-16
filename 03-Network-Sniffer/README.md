Project 03: Python Network Sniffer
What I Built
A network forensics tool that captures and analyzes real-time IP traffic. Using the Scapy library, it dissects packets to extract source/destination addresses and protocol types.

Why
To understand the Data Link and Network layers of the OSI model. This tool helps in:

Monitoring network traffic for suspicious activity.

Understanding how data is routed between local and external networks.

Learning how to handle raw network data in Python.

Deployment Instructions
Install dependencies: sudo apt install python3-scapy

Run with elevated privileges: sudo python3 sniffer.py

Analyze: Observe the traffic logs in the terminal.

What I Learnt
Privileged Access: Why network sniffing requires sudo permissions.

Packet Filtering: How to use BPF (Berkeley Packet Filters) to look for specific traffic.

Encapsulation: Visualizing the IP headers I studied in my CCNA course.

What I Would Improve
Packet Decoding: Add logic to show if the protocol is specifically TCP (6), UDP (17), or ICMP (1).


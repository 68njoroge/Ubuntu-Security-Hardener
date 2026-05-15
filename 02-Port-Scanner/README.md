Project 02: Python TCP Port Scanner
🛠 What I Built
A lightweight reconnaissance tool written in Python that identifies open TCP ports on a target IP address. It utilizes the socket library to attempt a 3-way handshake with common service ports including SSH (22), HTTP (80), HTTPS (443), and MySQL (3306).

🎯 Why
In Ethical Hacking, reconnaissance is the first and most critical phase. This tool was built to:

Automate the discovery of active services on a network.

Verify that my System Hardening (Project 01) script successfully closed unnecessary ports.

Practice implementing networking protocols through code rather than just using pre-built tools like Nmap.

🚀 Deployment Instructions
Clone the repository:


git clone https://github.com/68njoroge/Ubuntu-Security-Hardener.git
Navigate to the project:


cd "02-Port-Scanner"
Run the scanner:


python3 scanner.py
Input Target: Enter 127.0.0.1 for local testing or a specific IP address on your network.

What I Learnt
The 3-Way Handshake: I saw how a SYN packet results in an ACK (Open) or RST (Closed) at the code level.

Socket Programming: Learned how to manage connection timeouts so the script doesn't hang on filtered ports.

Defense-in-Depth: Confirmed that a port can appear "Closed" even if the service exists if the firewall (UFW) isn't configured to allow it.

What I Would Improve
Multi-threading: Currently, the scan is sequential (one by one). I would add threading to scan hundreds of ports simultaneously.

Banner Grabbing: Add functionality to identify the version of the service running on the open port (e.g., "OpenSSH 8.2").

User Experience: Allow the user to input a range of ports (e.g., 1-1024) instead of a hardcoded list.
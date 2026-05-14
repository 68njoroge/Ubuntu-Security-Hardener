Advanced Ubuntu Security Hardener

Project Overview
This project is an automated security baseline script for Ubuntu Linux. It moves beyond basic updates by implementing Intrusion Prevention (IPS), Automated Patch Management, and Network Hardening.

I developed this tool to bridge the gap between my CCNA networking knowledge and practical Cybersecurity/Ethical Hacking applications.

Key Security Features
Intrusion Prevention: Automatically installs and enables Fail2Ban to monitor system logs and block IP addresses that exhibit brute-force behavior.

Automated Vulnerability Management: Configures unattended-upgrades to ensure critical security patches are installed daily without manual intervention.

Network Perimeter Control: Implements a "Default Deny" firewall policy using UFW, specifically allow-listing only Port 22 (SSH) for secure remote management.

Incident Response Logging: Automates the extraction of failed login attempts from system logs (/var/log/auth.log) into a dedicated report for security auditing.

2 How to Run
Clone the repository:
git clone https://github.com/68njoroge/Ubuntu-Security-Hardener.git
cd Ubuntu-Security-Hardener

Make the script executable:
chmod +x harden.sh
    ```
3.  **Run with root privileges:**
    ```bash
    sudo ./harden.sh
    ```

## Verification of Success
After running, the script provides a status report. A successful hardening will show:
   **UFW Status:** `active`
   **Default Policy:** `deny (incoming)`
   **Allow Rules:** `22/tcp (SSH)`
   **Service Status:** `fail2ban.service` enabled and active.

##  Concepts Mastered
Concept | Security Benefit

Brute-Force Protection Using Fail2Ban to prevent automated password guessing.

Layer 4 Filtering Applying CCNA principles to restrict traffic by port and protocol. 

Automation (Bash) Reducing human error by scripting repetitive security tasks. 

Log Analysis Tracking unauthorized access attempts via `auth.log`. 

##  Disclaimer
This script is intended for **educational purposes** and personal workstation hardening. Always test security configurations in a virtual lab environment (VirtualBox/VMware) before deploying to production systems.
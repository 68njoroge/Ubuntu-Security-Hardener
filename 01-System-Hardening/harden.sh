#!/bin/bash
# Project : Advanced Ubuntu Security Hardener
echo "step 1: update and install programmes "
sudo apt update && sudo apt install -y unattended-upgrades apt-listchanges
sudo dpkg-reconfigure -plow unattended-upgrades

#create ssh folder and set permissions
echo "step 2: create ssh folder"
mkdir -p ~/.ssh
chmod 700 ~/.ssh

#protection aganst brute force attacks
echo "step3: install fail2ban"
sudo apt install -y fail2ban
sudo systemctl enable --now fail2ban

#configure firewall
echo "step 4: configure firewall"
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp comment "Allow ssh"
sudo ufw --force enable

#check ufw status
echo "step 4.1: check ufw status"
sudo ufw status verbose

#check failed logins 
echo "step 5: check failed logins"
sudo grep "Failed password" /var/log/auth.log > ~/Documents/failed_logins.txt


echo "hardening complete. Failed login attempts saved to ~/Documents/failed_logins.txt"
# SIEM Authentication Log Monitor

## Overview

This project is a simple Security Information and Event Management (SIEM) style log monitoring tool built with Python. The script continuously monitors Ubuntu authentication logs in real time and detects failed authentication attempts or unauthorized access activity.

The purpose of this project was to understand how security monitoring systems work at a foundational level by interacting directly with Linux log files and implementing basic threat detection logic.

---

## Features

- Real-time monitoring of Ubuntu authentication logs
- Detection of failed login attempts
- Detection of authentication failures
- Continuous live monitoring using file tailing techniques
- Basic alerting system through terminal output
- Permission handling for restricted system logs

---

## Technologies Used

- Python 3
- Linux Authentication Logs (`/var/log/auth.log`)
- Python `os` module
- Python `time` module

---

## Project Structure

```bash
log_monitor.py
README.md

## How it works 
The script:

Checks whether the authentication log file exists
Opens the log file in read mode
Moves to the end of the file to avoid reading old logs
Continuously watches for newly added log entries
Detects suspicious authentication activity using keyword matching
Displays alerts when failed authentication attempts are identified

##Future Improvements

In the future, I would improve this project by adding:

Email or Telegram alert notifications
IP address extraction and analysis
Brute-force attack detection
Log storage in a database
Dashboard visualization
Multiple detection rules
Support for additional log sources
Integration with threat intelligence feeds
Automated blocking of malicious IP addresses
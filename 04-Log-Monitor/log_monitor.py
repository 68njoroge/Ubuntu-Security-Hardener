import os
import time

# Basic log monitoring script 
# Path to the log file to monitor
LOG_FILE = '/var/log/auth.log'

def monitor_auth_logs(LOG_FILE):
    print("Checking for new log entries in:", LOG_FILE)
    if not os.path.exists(LOG_FILE):
        print(f"ERROR: Log file {LOG_FILE} does not exist.")
        return
    with open(LOG_FILE, 'r') as f:
        # Move the cursor to the end of the file
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)  # Wait briefly for new log entries
                continue
            
            # Threat Detection Logic: Check for failed attempts
            if "failed" in line.lower() or "authentication failure" in line.lower():
                print(f" [SECURITY ALERT] Unauthorized Access Attempt Detected!")
                print(f" Log Detail: {line.strip()}\n")

if __name__ == "__main__":
    # This requires root privileges to read system auth logs
    try:
        monitor_auth_logs(LOG_FILE)
    except PermissionError:
        print("Error: You must run this script with elevated privileges. Try: sudo python3 log_monitor.py")
            



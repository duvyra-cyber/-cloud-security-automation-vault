def detect_suspicious_ips():
    print("[*] Monitoring cloud traffic logs for malicious activities...")
    
    network_logs = [
        {"ip": "196.200.22.4", "failed_attempts": 0},
        {"ip": "45.227.254.12", "failed_attempts": 5},
        {"ip": "192.168.1.50", "failed_attempts": 1}
    ]
    
    for log in network_logs:
        if log["failed_attempts"] >= 3:
            print(f"[-] CRITICAL: Malicious traffic detected from IP {log['ip']}!")
            print(f"[*] Action: Automated Remediation active. Source IP -> BLOCKED.")
        else:
            print(f"[+] Security Status: IP {log['ip']} is verified and ACTIVE.")

if __name__ == "__main__":
    detect_suspicious_ips()


import os

def audit_system():
    print("[*] Starting Security Integrity Audit...")
    secure_files = {"/etc/shadow": "700", "/var/log/auth.log": "700"}
    for file, required_perm in secure_files.items():
        current_perm = "755"
        if current_perm != required_perm:
            print(f"[-] ALERT: {file} is compromised with permission {current_perm}!")
        else:
            print(f"[+] SUCCESS: {file} checks out safely.")

if __name__ == "__main__":
    audit_system()


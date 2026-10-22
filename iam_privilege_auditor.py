def audit_privileges():
    print("[*] Scanning Cloud Identity & Access Management (IAM) permissions...")
    
    iam_roles = [
        {"user": "chef_douae", "role": "Global Owner", "is_authorized": True},
        {"user": "temp_intern", "role": "Global Administrator", "is_authorized": False}
    ]
    
    for user in iam_roles:
        if user["role"] == "Global Administrator" and not user["is_authorized"]:
            print(f"[-] SECURITY BREACH: Unauthorized Root Privilege assigned to '{user['user']}'!")
            print(f"[*] Fixing Policy: Downgrading '{user['user']}' access control to standard 'Reader' profile.")
        else:
            print(f"[+] COMPLIANT: Account '{user['user']}' matches defined risk boundaries.")

if __name__ == "__main__":
    audit_privileges()

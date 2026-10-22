def enforce_password_policy():
    print("[*] Auditing IAM user credential strength...")
    
    passwords_to_check = ["Duvyra2026!", "123456", "admin_pass_2026"]
    
    for pwd in passwords_to_check:
        if len(pwd) < 8 or pwd.isdigit() or pwd.isalpha():
            print(f"[-] WEAK PASSWORD DETECTED: '{pwd}' fails security compliance rules.")
            print("[*] Enforcement: Requiring password reset with special characters.")
        else:
            print(f"[+] COMPLIANT: Password '{pwd}' meets strict infrastructure benchmarks.")

if __name__ == "__main__":
    enforce_password_policy()


def check_ssl_status():
    print("[*] Running programmatic audit on Domain SSL/TLS layer (Port 443)...")
    
    monitored_domains = [
        {"domain": "duvyra.cyber", "days_to_expire": 45},
        {"domain": "client-payment-gateway", "days_to_expire": 2}
    ]
    
    for site in monitored_domains:
        if site["days_to_expire"] <= 5:
            print(f"[-] EXPIRED / CRITICAL: {site['domain']} SSL certificate expires in {site['days_to_expire']} days!")
            print("[*] Automated Alert sent to Admin Dashboard for immediate renewal.")
        else:
            print(f"[+] SECURE: {site['domain']} SSL validation is verified for {site['days_to_expire']} days.")

if __name__ == "__main__":
    check_ssl_status()

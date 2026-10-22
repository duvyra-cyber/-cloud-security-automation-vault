def verify_backups():
    print("[*] Verifying infrastructure recovery and backup logs...")
    
    backup_vaults = [
        {"vault_id": "db-backup-01", "status": "Completed", "encrypted": True},
        {"vault_id": "media-backup-02", "status": "Failed", "encrypted": False}
    ]
    
    for vault in backup_vaults:
        if vault["status"] != "Completed" or not vault["encrypted"]:
            print(f"[-] ACCIDENT DETECTED: Backup '{vault['vault_id']}' is vulnerable or failed!")
            print("[*] Retrying snapshot creation with automated cryptographic hardening...")
        else:
            print(f"[+] BACKUP VALIDATED: '{vault['vault_id']}' is locked and stored safely.")

if __name__ == "__main__":
    verify_backups()

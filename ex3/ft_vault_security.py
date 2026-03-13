if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()
    try:
        print("SECURE EXTRACTION:")
        with open("classified_data.txt", "r") as e:
            data = e.read()
            print(data)
        print()
        print("SECURE PRESERVATION:")
        with open("file.txt", "w") as f:
            f.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
        print()
        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("Error: file not found!")
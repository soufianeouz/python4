# ancient_fragment.txt

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    
    try:
        with open("ancient_fragment.txt") as f:
            data = f.read()
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(data)
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
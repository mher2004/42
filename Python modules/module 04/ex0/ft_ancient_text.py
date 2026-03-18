print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
print("Accessing Storage Vault: ancient_fragment.txt")
try:
    file = open("ancient_fragment.txt", "r")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(file.read())
    print("\nData recovery complete. Storage unit disconnected.")
    file.close()
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")

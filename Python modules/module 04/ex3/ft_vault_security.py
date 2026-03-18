print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")

try:
    with open("classified_data.txt", "r") as file:
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:")
        print(file.read())
    with open("security_protocols.txt", "r") as file:
        print("\nSECURE PRESERVATION:")
        print(file.read())
except FileNotFoundError:
    print("Error: No files to read")
except PermissionError:
    print("Error: No permission to read")
else:
    print("Vault automatically sealed upon completion")

print("\nAll vault operations completed with maximum security.")

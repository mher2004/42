print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

try:
    with open("new_discovery.txt", "r") as file:
        pass
except FileNotFoundError:
    with open("new_discovery.txt", "w") as file:
        print("Initializing new storage unit: new_discovery.txt")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        print("[ENTRY 001] New quantum algorithm discovered")
        print("[ENTRY 002] Efficiency increased by 347%")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee")
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
else:
    print("Error: A file with that name was found!")
    print("Terminating the process...")

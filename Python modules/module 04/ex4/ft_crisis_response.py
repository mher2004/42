print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

try:
    with open("lost_archive.txt", "r") as file:
        pass
except FileNotFoundError:
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")
try:
    with open("classified_vault.txt", "w") as file:
        raise PermissionError
except PermissionError:
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")
with open("standard_archive.txt", "r") as file:
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    print(f"SUCCESS: Archive recovered - ``{file.read()}''")
    print("STATUS: Normal operations resumed\n")

print("All crisis scenarios handled successfully. Archives secure.")

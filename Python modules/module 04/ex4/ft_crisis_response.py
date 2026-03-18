print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")


def open_file(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPOSE: Some error ocurred")


open_file("lost_archive.txt")
open_file("classified_vault.txt")
open_file("standard_archive.txt")

print("All crisis scenarios handled successfully. Archives secure.")

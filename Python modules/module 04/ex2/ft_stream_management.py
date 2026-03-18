import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
iD = input("\nInput Stream active. Enter archivist ID: ")
report = input("Input Stream active. Enter status report: ")
print(f"\n[STANDARD] Archive status\
 from {iD}: {report}")
print("[ALERT] System diagnostic:\
 Communication channels verified", file=sys.stderr)
print("[STANDARD] Data transmission complete")
print("\nThree-channel communication test successful.")

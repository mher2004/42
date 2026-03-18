import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
sys.stdout.write("\nInput Stream active. Enter archivist ID:")
iD = sys.stdin.readline().strip()
sys.stdout.write("\nInput Stream active. Enter status report:")
report = sys.stdin.readline().strip()
sys.stdout.write(f"\n[STANDARD] Archive status\
 from {iD}: {report}\n")
sys.stderr.write("[ALERT] System diagnostic:\
 Communication channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n")

print("\nThree-channel communication test successful.")

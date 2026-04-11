import sys
import site

is_venv = sys.prefix != sys.base_prefix

print("MATRIX STATUS:",
      "You're still plugged in" if not is_venv else "Welcome to the construct")
print("\nCurrent Python: ", sys.executable)
print("Virtual Environment: ",
      "None detected" if not is_venv else sys.prefix.split("/")[-1])
if not is_venv:
    print("\nWARNING: You're in the global environment!\n\
The machines can see everything you install.")
    print("\nTo enter the construct, run:\n\
python -m venv matrix_env\n\
source matrix_env/bin/activate # On Unix\n\
matrix_env\\Scripts\\activate # On Windows\n\n\
Then run this program again.")

else:
    print("Envirnment Path:", sys.prefix)
    print("\nSUCCESS: You're in an isolated environment!\n\
Safe to install packages without affecting\n\
the global system.\n\
Package installation path:")
    print([
        name for name in site.getsitepackages() if "/site-packages" in name
        ])
    print()

import os

def suid_scan():
    print("\n[+] SUID FILES")

    os.system("find / -perm -4000 2>/dev/null")

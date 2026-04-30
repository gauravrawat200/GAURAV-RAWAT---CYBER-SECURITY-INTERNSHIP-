import os

def cron_scan():
    print("\n[+] CRON JOBS")

    os.system("crontab -l 2>/dev/null")
    os.system("ls -la /etc/cron*")

import time

def run_all():
    system_info()
    suid_scan()
    permission_scan()
    cron_scan()

if __name__ == "__main__":
    while True:
        run_all()
        print("Running again in 60 seconds...")
        time.sleep(60)

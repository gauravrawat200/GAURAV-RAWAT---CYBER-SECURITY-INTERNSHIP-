import time

from system_scan import system_info
from suid_scan import suid_scan
from permission_scan import permission_scan
from cron_scan import cron_scan


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

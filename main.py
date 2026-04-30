from flask import Flask
import threading
import time

from system_scan import system_info
from suid_scan import suid_scan
from permission_scan import permission_scan
from cron_scan import cron_scan

app = Flask(_name_)

def run_all():
    system_info()
    suid_scan()
    permission_scan()
    cron_scan()

def background_task():
    while True:
        run_all()
        print("Running again in 60 seconds...")
        time.sleep(60)

@app.route("/")
def home():
    return "Cyber Security Scanner is Running!"

if _name_ == "_main_":
    t = threading.Thread(target=background_task)
    t.start()
    app.run(host="0.0.0.0", port=10000)

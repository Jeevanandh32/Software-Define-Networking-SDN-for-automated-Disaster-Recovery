import subprocess
import time

def monitor_traffic():
    print("[INFO] Starting network traffic monitoring...")
    with open("traffic_logs.txt", "w") as logfile:
        while True:
            result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                logfile.write(f"[{time.ctime()}] Network is up\n")
                print(f"[{time.ctime()}] Network is up")
            else:
                logfile.write(f"[{time.ctime()}] Network is down\n")
                print(f"[{time.ctime()}] Network is down")
            time.sleep(5)

if __name__ == "__main__":
    monitor_traffic()

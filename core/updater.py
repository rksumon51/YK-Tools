import os
import time

GREEN = '\033[1;32m'
RESET = '\033[0m'

def update_project():
    print(f"\n{GREEN}[+] Checking for updates from GitHub...{RESET}")
    print(f"{GREEN}[+] Syncing files and removing deleted codes...{RESET}")
    
    # Git Hard Reset কমান্ড যা টার্মাক্সকে হুবহু গিটহাবের মতো করে ফেলবে
    os.system("cd $HOME/yk-tools && git fetch --all && git reset --hard origin/main")
    
    print(f"\n{GREEN}[+] Project updated successfully! Restarting tool...{RESET}")
    time.sleep(2)
    exit()

import os
import time
from core.network import get_network_status
from core.updater import update_project

# কালার কোড
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
RED = '\033[1;31m'
RESET = '\033[0m'

def show_banner():
    os.system('clear')
    banner = f"""{CYAN}
 __     __ _  __   _______  ____    ____  _       _____ 
 \ \   / /| |/ /  |__   __|/ __ \  / __ \| |     / ____|
  \ \_/ / | ' /      | |  | |  | || |  | | |    | (___  
   \   /  |  <       | |  | |  | || |  | | |     \___ \ 
    | |   | . \      | |  | |__| || |__| | |____ ____) |
    |_|   |_|\_\     |_|   \____/  \____/|______|_____/ 
    {RESET}"""
    print(banner)

def main():
    while True:
        show_banner()
        print(f"{YELLOW}[+] Checking Internet Speed and Ping... Please wait.{RESET}\n")
        
        # নেটওয়ার্ক স্ট্যাটাস চেক করে হোম স্ক্রিনে দেখানো
        ping, speed, capacity = get_network_status()
        
        print(f"{GREEN}Ping: {ping} | Upload Speed: {speed}{RESET}")
        print(f"{CYAN}Max Live Stream Capacity: {capacity} Channels{RESET}")
        print(CYAN + "-" * 55 + RESET + "\n")
        
        # শুধু আপনার বলা দুটি বাটন
        print(f"{GREEN}1. YT Work{RESET}")
        print(f"{YELLOW}2. Update Project{RESET}")
        print(f"{RED}0. Exit{RESET}\n")
        
        choice = input(f"{CYAN}Select Option: {RESET}")
        
        if choice == '1':
            print(f"\n{YELLOW}[!] Opening YT Work... (কোডিং পরে যোগ করা হবে){RESET}")
            time.sleep(1.5)
            # ভবিষ্যতে এখানে platforms.youtube.yt_menu কল করা হবে
        elif choice == '2':
            update_project()
        elif choice == '0':
            print(f"\n{GREEN}Exiting YK Tools...{RESET}")
            break
        else:
            print(f"\n{RED}[X] Invalid Option!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()

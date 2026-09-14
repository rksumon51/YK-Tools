import os
import sys
import time
import threading
import subprocess
import math
from core.updater import update_project

# কালার কোড
C_RED = '\033[1;31m'
C_YELLOW = '\033[1;33m'
C_GREEN = '\033[1;32m'
C_CYAN = '\033[1;36m'
C_MAGENTA = '\033[1;35m'
C_WHITE = '\033[1;37m'
C_RESET = '\033[0m'

# গ্লোবাল লাইভ ডেটা
live_ping = "Checking..."
live_speed = "Testing..."
live_capacity = "Calculating..."
app_running = True

def live_ping_checker():
    global live_ping
    while app_running:
        try:
            out = subprocess.check_output(['ping', '-c', '1', '8.8.8.8'], stderr=subprocess.STDOUT, text=True)
            live_ping = out.split('time=')[1].split(' ms')[0] + ' ms'
        except:
            live_ping = "Timeout"
        time.sleep(1)

def live_speed_checker():
    global live_speed, live_capacity
    while app_running:
        try:
            import speedtest
            st = speedtest.Speedtest(secure=True)
            st.get_best_server() 
            mbps = round(st.upload() / 1000000, 2)
            live_speed = f"{mbps} Mbps"
            cap = math.floor(mbps / 2.5)
            live_capacity = f"{cap} Channels"
        except:
            pass
        time.sleep(3) 

def live_ui_updater():
    banner = [
        r" __   __ _  __   _____ ___   ___  _    ___ ",
        r" \ \ / /| |/ /  |_   _/ _ \ / _ \| |  / __|",
        r"  \ V / | ' <     | || (_) | (_) | |__\__ \ ",
        r"   |_|  |_|\_\    |_| \___/ \___/|____|___/"
    ]
    colors = [C_RED, C_YELLOW, C_GREEN, C_CYAN, C_MAGENTA]
    step = 0
    
    while app_running:
        sys.stdout.write('\0337') 
        
        sys.stdout.write('\033[2;1H')
        for j, line in enumerate(banner):
            c_idx = (step + j) % len(colors)
            sys.stdout.write(f"{colors[c_idx]}{line}{C_RESET}\033[K\n")
            
        sys.stdout.write('\033[10;1H')
        sys.stdout.write(f" {C_CYAN}│ {C_GREEN}⚡ Ping     :{C_RESET} {live_ping:<26} {C_CYAN}│{C_RESET}\033[K\n")
        
        sys.stdout.write('\033[11;1H')
        sys.stdout.write(f" {C_CYAN}│ {C_YELLOW}🚀 Upload   :{C_RESET} {live_speed:<26} {C_CYAN}│{C_RESET}\033[K\n")
        
        sys.stdout.write('\033[12;1H')
        sys.stdout.write(f" {C_CYAN}│ {C_MAGENTA}📊 Capacity :{C_RESET} {live_capacity:<26} {C_CYAN}│{C_RESET}\033[K\n")
        
        sys.stdout.write('\0338') 
        sys.stdout.flush()
        
        step += 1
        time.sleep(0.5)

def main():
    global app_running
    
    # [!] টুল চালু হওয়ার সাথেই নেটওয়ার্ক ও সিপিইউ প্রায়োরিটি লক করা হলো
    os.system("termux-wake-lock")
    
    # স্ক্রিন সম্পূর্ণ ক্লিয়ার করে ফ্রেম ফিক্স করা
    sys.stdout.write("\033[2J\033[H")
    
    sys.stdout.write("\n\n\n\n\n\n")
    sys.stdout.write(f" {C_CYAN}╭────────────────────────────────────────╮{C_RESET}\n")
    sys.stdout.write(f" {C_CYAN}│ {C_WHITE}🌐 NETWORK STATUS                      {C_CYAN}│{C_RESET}\n")
    sys.stdout.write(f" {C_CYAN}├────────────────────────────────────────┤{C_RESET}\n")
    sys.stdout.write(f" {C_CYAN}│                                        │{C_RESET}\n") 
    sys.stdout.write(f" {C_CYAN}│                                        │{C_RESET}\n") 
    sys.stdout.write(f" {C_CYAN}│                                        │{C_RESET}\n") 
    sys.stdout.write(f" {C_CYAN}╰────────────────────────────────────────╯{C_RESET}\n\n")
    
    sys.stdout.write(f"  {C_GREEN}[1] YT Work{C_RESET}\n")
    sys.stdout.write(f"  {C_YELLOW}[2] Update Project{C_RESET}\n")
    sys.stdout.write(f"  {C_RED}[0] Exit{C_RESET}\n\n")
    
    sys.stdout.write(f" {C_CYAN}╭─[{C_WHITE}Select Option{C_CYAN}]\n")
    
    threading.Thread(target=live_ping_checker, daemon=True).start()
    threading.Thread(target=live_speed_checker, daemon=True).start()
    threading.Thread(target=live_ui_updater, daemon=True).start()
    
    while True:
        choice = input(f" {C_CYAN}╰─➤ {C_RESET}")
        
        if choice == '1':
            print(f"\n {C_YELLOW}[!] Opening YT Work... (কোডিং পরে যোগ করা হবে){C_RESET}")
            time.sleep(1.5)
        elif choice == '2':
            app_running = False
            time.sleep(1)
            # আপডেটের সময় লক রিলিজ করা
            os.system("termux-wake-unlock")
            update_project()
            break
        elif choice == '0':
            app_running = False
            # টুল থেকে বের হওয়ার সময় লক রিলিজ করা
            os.system("termux-wake-unlock")
            print(f"\n {C_GREEN}Exiting YK Tools. Goodbye!{C_RESET}")
            break
        else:
            print(f"\n {C_RED}[X] Invalid Option!{C_RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()

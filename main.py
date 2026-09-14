import os
import time
from core.network import get_network_status
from core.updater import update_project

# RGB ও অন্যান্য কালার কোড
C_RED = '\033[1;31m'
C_YELLOW = '\033[1;33m'
C_GREEN = '\033[1;32m'
C_CYAN = '\033[1;36m'
C_BLUE = '\033[1;34m'
C_MAGENTA = '\033[1;35m'
C_WHITE = '\033[1;37m'
C_RESET = '\033[0m'

def show_banner():
    os.system('clear')
    # মোবাইলের জন্য পারফেক্ট সাইজের ASCII আর্ট
    banner = [
        r"  __  __ _  __   _____ ___   ___  _    ___ ",
        r"  \ \/ /| |/ /  |_   _/ _ \ / _ \| |  / __|",
        r"   >  < | ' <     | || (_) | (_) | |__\__ \ ",
        r"  /_/\_\|_|\_\    |_| \___/ \___/|____|___/"
    ]
    
    # RGB লাইট ইফেক্ট (প্রতি লাইনে আলাদা রং)
    colors = [C_RED, C_YELLOW, C_GREEN, C_CYAN]
    
    print("\n")
    for i, line in enumerate(banner):
        print(f"{colors[i % len(colors)]}{line}{C_RESET}")
    print("\n")

def main():
    while True:
        show_banner()
        print(f" {C_YELLOW}[+] Checking Network Status...{C_RESET}\n")
        
        # নেটওয়ার্ক ডেটা ফেচ করা
        ping, speed, capacity = get_network_status()
        capacity_text = f"{capacity} Channels"
        
        # প্রফেশনাল নেটওয়ার্ক বক্স ডিজাইন
        print(f" {C_CYAN}╭────────────────────────────────────────╮{C_RESET}")
        print(f" {C_CYAN}│ {C_WHITE}🌐 NETWORK STATUS                      {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}├────────────────────────────────────────┤{C_RESET}")
        print(f" {C_CYAN}│ {C_GREEN}⚡ Ping     :{C_RESET} {ping:<26} {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}│ {C_YELLOW}🚀 Upload   :{C_RESET} {speed:<26} {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}│ {C_MAGENTA}📊 Capacity :{C_RESET} {capacity_text:<26} {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}╰────────────────────────────────────────╯{C_RESET}\n")
        
        # মেনু বাটন
        print(f"  {C_GREEN}[1] YT Work{C_RESET}")
        print(f"  {C_YELLOW}[2] Update Project{C_RESET}")
        print(f"  {C_RED}[0] Exit{C_RESET}\n")
        
        # প্রফেশনাল ইনপুট প্রম্পট
        print(f" {C_CYAN}╭─[{C_WHITE}Select Option{C_CYAN}]")
        choice = input(f" {C_CYAN}╰─➤ {C_RESET}")
        
        if choice == '1':
            print(f"\n {C_YELLOW}[!] Opening YT Work...{C_RESET}")
            time.sleep(1.5)
        elif choice == '2':
            update_project()
        elif choice == '0':
            print(f"\n {C_GREEN}Exiting YK Tools. Goodbye!{C_RESET}")
            break
        else:
            print(f"\n {C_RED}[X] Invalid Option!{C_RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()

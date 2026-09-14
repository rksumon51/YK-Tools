import os
import time
from core.network import get_network_status
from core.updater import update_project

C_RED = '\033[1;31m'
C_YELLOW = '\033[1;33m'
C_GREEN = '\033[1;32m'
C_CYAN = '\033[1;36m'
C_BLUE = '\033[1;34m'
C_MAGENTA = '\033[1;35m'
C_WHITE = '\033[1;37m'
C_RESET = '\033[0m'

def animate_banner():
    banner = [
        r" __   __ _  __   _____ ___   ___  _    ___ ",
        r" \ \ / /| |/ /  |_   _/ _ \ / _ \| |  / __|",
        r"  \ V / | ' <     | || (_) | (_) | |__\__ \ ",
        r"   |_|  |_|\_\    |_| \___/ \___/|____|___/"
    ]
    colors = [C_RED, C_YELLOW, C_GREEN, C_CYAN, C_BLUE, C_MAGENTA]
    
    # রিয়েল টাইম RGB ব্লিংক অ্যানিমেশন লুপ
    for i in range(15):
        os.system('clear')
        print("\n")
        for j, line in enumerate(banner):
            c_idx = (i + j) % len(colors)
            print(f"{colors[c_idx]}{line}{C_RESET}")
        print("\n")
        time.sleep(0.1)
    
    # অ্যানিমেশন শেষে ফাইনাল ব্যানার সেট করা
    os.system('clear')
    print("\n")
    for j, line in enumerate(banner):
        print(f"{colors[j % len(colors)]}{line}{C_RESET}")
    print("\n")

def main():
    while True:
        animate_banner()
        
        # রিয়েল টাইম স্পিড টেস্টের জন্য ওয়ার্নিং
        print(f" {C_YELLOW}[+] Checking Real-Time Network Status (Takes 10-15s)...{C_RESET}\n")
        
        ping, speed, capacity = get_network_status()
        
        print(f" {C_CYAN}╭────────────────────────────────────────╮{C_RESET}")
        print(f" {C_CYAN}│ {C_WHITE}🌐 NETWORK STATUS                      {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}├────────────────────────────────────────┤{C_RESET}")
        print(f" {C_CYAN}│ {C_GREEN}⚡ Ping     :{C_RESET} {ping:<26} {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}│ {C_YELLOW}🚀 Upload   :{C_RESET} {speed:<26} {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}│ {C_MAGENTA}📊 Capacity :{C_RESET} {capacity:<26} {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}╰────────────────────────────────────────╯{C_RESET}\n")
        
        print(f"  {C_GREEN}[1] YT Work{C_RESET}")
        print(f"  {C_YELLOW}[2] Update Project{C_RESET}")
        print(f"  {C_RED}[0] Exit{C_RESET}\n")
        
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

import os
import sys
import time
import threading
import itertools
from core.network import get_network_status
from core.updater import update_project

# কালার কোড
C_RED = '\033[1;31m'
C_YELLOW = '\033[1;33m'
C_GREEN = '\033[1;32m'
C_CYAN = '\033[1;36m'
C_BLUE = '\033[1;34m'
C_MAGENTA = '\033[1;35m'
C_WHITE = '\033[1;37m'
C_RESET = '\033[0m'

# গ্লোবাল ভেরিয়েবল
network_result = None
animating = True

def fetch_network():
    """ব্যাকগ্রাউন্ডে রিয়েল-টাইম স্পিড টেস্ট"""
    global network_result
    network_result = get_network_status()

def banner_animator():
    """ব্যাকগ্রাউন্ড থ্রেড: ইউজারের কাজে বাধা না দিয়ে ব্যানার অ্যানিমেট করবে"""
    banner = [
        r" __   __ _  __   _____ ___   ___  _    ___ ",
        r" \ \ / /| |/ /  |_   _/ _ \ / _ \| |  / __|",
        r"  \ V / | ' <     | || (_) | (_) | |__\__ \ ",
        r"   |_|  |_|\_\    |_| \___/ \___/|____|___/"
    ]
    colors = [C_RED, C_YELLOW, C_GREEN, C_CYAN, C_BLUE, C_MAGENTA]
    step = 0
    
    while animating:
        # বর্তমান কার্সার পজিশন সেভ করে স্ক্রিনের ২ নম্বর লাইনে যাবে
        sys.stdout.write('\033[s\033[2;1H')
        
        for j, line in enumerate(banner):
            c_idx = (step + j) % len(colors)
            # কালার চেঞ্জ করে লাইন প্রিন্ট করবে
            sys.stdout.write(f"{colors[c_idx]}{line}{C_RESET}\033[K\n")
        
        # কাজ শেষে কার্সার আবার ইউজারের ইনপুটের জায়গায় ফেরত পাঠাবে
        sys.stdout.write('\033[u')
        sys.stdout.flush()
        
        step += 1
        time.sleep(0.4) # অ্যানিমেশনের স্পিড

def main():
    global animating
    
    # টুল ওপেন হওয়ার সাথেই ব্যানারের ব্যাকগ্রাউন্ড থ্রেড চালু হয়ে যাবে
    b_thread = threading.Thread(target=banner_animator, daemon=True)
    b_thread.start()
    
    while True:
        os.system('clear')
        # ব্যানার অ্যানিমেট হওয়ার জন্য উপরে ৫ লাইনের ফাঁকা জায়গা তৈরি
        print("\n\n\n\n\n")
        
        # স্পিড টেস্টের থ্রেড
        t = threading.Thread(target=fetch_network)
        t.start()
        
        print(f" {C_CYAN}╭────────────────────────────────────────╮{C_RESET}")
        print(f" {C_CYAN}│ {C_WHITE}🌐 NETWORK STATUS                      {C_CYAN}│{C_RESET}")
        print(f" {C_CYAN}├────────────────────────────────────────┤{C_RESET}")
        
        spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        
        while t.is_alive():
            spin = next(spinner)
            visible_text = f"Analyzing Network {spin}"
            spaces = " " * 20 
            sys.stdout.write(f"\r {C_CYAN}│{C_RESET} {C_YELLOW}{visible_text}{C_RESET}{spaces}{C_CYAN}│{C_RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
            
        t.join()
        ping, speed, capacity = network_result
        
        sys.stdout.write(f"\r {C_CYAN}│ {C_GREEN}⚡ Ping     :{C_RESET} {ping:<26} {C_CYAN}│{C_RESET}\n")
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
            animating = False # আপডেট করার আগে অ্যানিমেশন থামানো
            b_thread.join(timeout=1)
            update_project()
            break
        elif choice == '0':
            animating = False
            print(f"\n {C_GREEN}Exiting YK Tools. Goodbye!{C_RESET}")
            break
        else:
            print(f"\n {C_RED}[X] Invalid Option!{C_RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()

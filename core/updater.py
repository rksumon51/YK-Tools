import os
import time
import sys

C_GREEN = '\033[1;32m'
C_RED = '\033[1;31m'
C_CYAN = '\033[1;36m'
C_RESET = '\033[0m'

def update_project():
    print(f"\n {C_CYAN}[+] GitHub থেকে আপডেট চেক করা হচ্ছে...{C_RESET}")
    print(f" {C_CYAN}[+] নতুন কোড সিঙ্ক হচ্ছে, দয়া করে অপেক্ষা করুন...{C_RESET}")
    
    # সঠিক ফোল্ডার পাথ (YK-Tools) এবং Git Hard Reset লজিক
    update_command = "cd $HOME/YK-Tools && git fetch --all && git reset --hard origin/main"
    result = os.system(update_command)
    
    if result == 0:
        print(f"\n {C_GREEN}[+] প্রজেক্ট সফলভাবে আপডেট হয়েছে!{C_RESET}")
        print(f" {C_GREEN}[+] টুলটি রিস্টার্ট করা হচ্ছে...{C_RESET}")
        time.sleep(2)
        # আপডেট শেষ হওয়ার সাথে সাথে নতুন কোড দিয়ে অটোমেটিক রিস্টার্ট হবে
        os.system("python $HOME/YK-Tools/main.py")
        sys.exit()
    else:
        print(f"\n {C_RED}[X] আপডেট ব্যর্থ হয়েছে! ইন্টারনেট কানেকশন চেক করুন।{C_RESET}")
        time.sleep(2)

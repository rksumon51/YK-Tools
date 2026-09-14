import subprocess
import math

def get_network_status():
    # Ping চেক
    try:
        ping_output = subprocess.check_output(['ping', '-c', '1', '8.8.8.8'], stderr=subprocess.STDOUT, universal_newlines=True)
        ping_time = ping_output.split('time=')[1].split(' ms')[0] + ' ms'
    except:
        ping_time = "Error"
    
    # রিয়েল টাইম স্পিড টেস্ট
    try:
        import speedtest
        st = speedtest.Speedtest(secure=True)
        st.get_servers()
        st.get_best_server()
        
        # আপলোড স্পিড বের করে Mbps-এ কনভার্ট করা
        upload_bps = st.upload()
        upload_mbps = round(upload_bps / 1000000, 2)
        speed_str = f"{upload_mbps} Mbps"
        
        # রিয়েল টাইম ক্যাপাসিটি (প্রতি চ্যানেল ২.৫ Mbps ধরে)
        capacity_calc = math.floor(upload_mbps / 2.5)
        if capacity_calc < 1:
            capacity_str = "0 Channels (Low Speed)"
        else:
            capacity_str = f"{capacity_calc} Channels"
            
    except ImportError:
        speed_str = "Error (Module Missing)"
        capacity_str = "N/A"
    except Exception:
        speed_str = "Network Error"
        capacity_str = "N/A"
        
    return ping_time, speed_str, capacity_str

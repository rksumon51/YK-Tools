import subprocess

def get_network_status():
    # টার্মাক্স থেকে গুগল সার্ভারে পিং করে রেজাল্ট বের করা
    try:
        ping_output = subprocess.check_output(['ping', '-c', '1', '8.8.8.8'], stderr=subprocess.STDOUT, universal_newlines=True)
        ping_time = ping_output.split('time=')[1].split(' ms')[0] + ' ms'
    except:
        ping_time = "Error"
    
    # স্পিড টেস্ট (আপাতত স্ট্রাকচার করা আছে, পরে রিয়েল স্পিডটেস্ট লাইব্রেরি যোগ করা যাবে)
    upload_speed = "10 Mbps (Test)"
    
    # স্পিড অনুযায়ী কয়টি লাইভ করা যাবে তার হিসাব (প্রতি স্ট্রিমে ২-৩ Mbps ধরে)
    stream_capacity = "3-4" 
    
    return ping_time, upload_speed, stream_capacity

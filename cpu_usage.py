############### Python script to check CPU usage ##################

############ import psutill and time for contiue monitoring ############

import psutil
import time

############ set threshold #################
threshold = 80

############# Main logic ##################
try:
    
    while True:
        cpu_usage = psutil.cpu_percent(interval=2)
        print ("CPU Usage:", cpu_usage , "%")
        time.sleep(2)
        
        if cpu_usage > threshold:
            print (f"CPU usage crossed the threshold: {cpu_usage}%")
        
        else:
            print(f"CPU usage: {cpu_usage}%")
            
        time.sleep (2)
        
except Exception as error:
    print ("error occured while checking cpu usage:", error)
    time.sleep(2)
    

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")

    
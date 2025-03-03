import os  

def spoof_gps(lat, lon):  
    os.system(f"gps-sdr-sim -e brdc3540.14n -l {lat},{lon},100")  
    print(f"[+] GPS Spoofed to {lat}, {lon}")  

if __name__ == "__main__":  
    spoof_gps(40.7128, -74.0060)  # New York coordinates  

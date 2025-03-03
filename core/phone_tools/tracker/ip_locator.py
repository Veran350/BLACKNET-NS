import requests  

def track_ip(ip):  
    try:  
        response = requests.get(f"http://ip-api.com/json/{ip}")  
        data = response.json()  
        if data['status'] == 'success':  
            print(f"""  
[+] IP: {data['query']}  
[+] ISP: {data['isp']}  
[+] Location: {data['city']}, {data['regionName']}, {data['country']}  
[+] Coordinates: {data['lat']}, {data['lon']}  
            """)  
        else:  
            print("[!] IP lookup failed.")  
    except Exception as e:  
        print(f"[!] Error: {e}")  

if __name__ == "__main__":  
    ip = input("Enter IP address: ")  
    track_ip(ip)  

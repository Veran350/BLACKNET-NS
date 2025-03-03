import requests  

def locate_sim(number):  
    response = requests.get(f"http://ip-api.com/json/{number}")  
    data = response.json()  
    print(f"[+] SIM Location: {data['city']}, {data['country']}")  

if __name__ == "__main__":  
    locate_sim("+2348123456789")  

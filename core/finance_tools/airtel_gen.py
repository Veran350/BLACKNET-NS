import random  

def generate_airtel_code():  
    prefix = random.choice(["0708", "0812", "0902"])  
    suffix = ''.join(random.choices("0123456789", k=11))  
    return f"{prefix}{suffix}"  

if __name__ == "__main__":  
    print(f"[+] Airtel Recharge Code: {generate_airtel_code()}")  

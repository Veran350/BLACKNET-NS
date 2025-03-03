import random  

def generate_mtn_code():  
    prefix = random.choice(["0703", "0803", "0903"])  
    suffix = ''.join(random.choices("0123456789", k=11))  
    return f"{prefix}{suffix}"  

if __name__ == "__main__":  
    print(f"[+] MTN Recharge Code: {generate_mtn_code()}")  

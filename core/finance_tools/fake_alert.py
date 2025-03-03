import random  

def generate_fake_alert():  
    amount = random.randint(1000, 50000)  
    print(f"[+] Fake Alert: ₦{amount} credited to your account.")  

if __name__ == "__main__":  
    generate_fake_alert()  

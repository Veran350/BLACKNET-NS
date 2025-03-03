import random  

def generate_btc_address():  
    chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"  
    return ''.join(random.choices(chars, k=34))  

if __name__ == "__main__":  
    print(f"[+] BTC Ransom Address: {generate_btc_address()}")  

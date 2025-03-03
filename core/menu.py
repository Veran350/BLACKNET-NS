from banner import show_banner  
import os  

def main_menu():  
    show_banner()  
    print("1. Deploy RAT\n2. Launch Phishing\n3. Generate CC\n4. Track Phone\n5. Destroy Device\n99. EXIT")  
    choice = input("Choice: ")  
    return choice  

if __name__ == "__main__":  
    while True:  
        os.system("clear")  
        choice = main_menu()  
        if choice == "99":  
            break  

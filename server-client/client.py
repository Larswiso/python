import socket

myIP  = socket.gethostbyname(socket.gethostname())
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!LEAVE"
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "[IPv4-Adresse: 92.168.2.114]"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    try:
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        #print(client.recv(2048).decode(FORMAT))
    except: 
        print("[ERROR] Connection to server failed")
        quit()

# send("Hello World!")
# input()
# send("Hello Everyone!")
# input()
# send("Hello Tim!")

# send(DISCONNECT_MESSAGE)

while True:
    msg = input("[Me] ")
    if msg == DISCONNECT_MESSAGE:
        send("User leftet!")
        break
    else:
        send(msg)
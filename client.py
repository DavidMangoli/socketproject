import socket


HEADER = 64
PORT = 49450
FORMAT = 'utf-8'
DISCONNECT = "DISCONNECTED."
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
BUFFERSIZE = 1024 #the size of the message

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)



def send(message):
    sent = message.encode(FORMAT)
    message_length = len(sent)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(sent)
    print(client.recv(2048).decode(FORMAT))


def options():
    print("Available commands:")
    print("* register @[handle] [IPv4-address] [port1] [port2] [port3]")
    print("* query handles")
    print("* follow @[handle i] @[handle j]")
    print("* drop @[handle i] @[handle j]")
    print("* tweet @[handle] [tweet]")
    print("* end-tweet @[handle]")
    print("* exit @[handle]")
    print("* quit")


def register(username, addy, portnum1 , portnum2, portnum3):
    data,addr = client.recvfrom(BUFFERSIZE)
    important = str.encode(f"register @"+{username} + {addy} + {portnum1} + {portnum2} + {portnum3})
    client.sendto((important),addr)
    messageBackToServer = data.decode(FORMAT)
    print(f"Response for Tracker" + {messageBackToServer})


def quit():
    message = "the client has decided to quit"
    print(message)
    quit(0)


def query_handles(count, display_of_handles):
    data, addr = client.recvfrom(BUFFERSIZE)
    display = int.encode(count)
    display1 = str.encode(display_of_handles)
    client.sendto(display, addr)
    client.sendto(display1, addr)
    message_back = data.decode(FORMAT)
    message_back1 = data.decode(FORMAT)
    print(f"The number of handlers register are" + message_back)
    print(f"The list of handles are shown as" + message_back1)


def follow_procedure(self, other_person):
    data, addr = client.recvfrom(BUFFERSIZE)
    important = str.encode(f"follow @"+ self + other_person)
    client.sendto(important, addr)
    backToServer = data.decode(FORMAT)
    print(backToServer + "has been executed")


def drop(old_self, old_person):
    data, addr = client.recvfrom(BUFFERSIZE)
    important = str.encode(f"drop @" + old_self + old_person)
    client.sendto(important, addr)
    backToServer = data.decode(FORMAT)
    print(backToServer + "has been executed")

for _ in range(3):
    options()
    message = input("Enter command you like to use:")
    send(message)
input()

client.close()

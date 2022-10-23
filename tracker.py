import socket
import threading
import json
from collections import Counter

HEADER = 120
PORT = 49450
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
BUFFERSIZE = 1024
DISCONNECT = "DISCONNECTED."

person_info = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def handle_client(connection, address):
    print(f"{address} has connected.")

    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
            if message == DISCONNECT:
                connected = False

            print(f"[{address}] {message}")
            connection.send(message.encode(FORMAT))

    connection.close()

def start():
    server.listen()
    print(f"[WAITING] SERVER IS WAITING FOR CONNECTIONS TO {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"CURRENT ACTIVE CONNECTIONS: {threading.active_count()-1}")


def main():
    while True:
        data, addr = server.recvfrom(BUFFERSIZE)
        message = "welcome new client"
        server.sendto(message, addr)
        options1 = data.decode(FORMAT).split()

        if options1[0] == "exit":
            message1 = handle_client(options1[1])
            bytesToSend = str.decode(message1)
            server.sendto(bytesToSend, addr)
        elif options1[0] == "register":
            message1 = register(options1[1],options1[2], options1[3], options1[4], options1[5])
            bytesToSend = str.decode(message1)
            server.sendto(bytesToSend, addr)
        elif options1[0] == "query" and options1[1] == "handles":
            num, handlers = query_handles()
            bytesToSend = int.decode(num) #decode is for when you receive
            bytesToSend1 = str.decode(handlers)
            server.sendto(bytesToSend,addr)
            server.sendto(bytesToSend1, addr)
        elif options1[0] == "follow":
            new_follower = query_handles(options1[1], options1[2])
            bytesToSend = str.decode(new_follower)
            server.sendto(bytesToSend,addr)
        elif options1[0] == "drop":
            new_follower = drop(options1[1], options1[2])
            bytesToSend = str.decode(new_follower)
            server.sendto(bytesToSend,addr)
        else:
            print("This command is not an option")


print("[START] THE SERVER IS STARTING, PLEASE WAIT...")


def register(tag, spot, pt1, pt2, pt3):
    emptyList = server.recv(BUFFERSIZE).decode()
    tag_length = len(tag)
    if tag_length > 15:
        print("FAILURE")

    strings = json.loads(emptyList)
    values = list(strings.values())
    if len(set(values())) == len(values):
        print("SUCCESS")
    elif pt1 > 49450 and pt1 < 49454:
        print("Port is available")
    elif pt2 > 49453 and pt2 < 49457:
        print("Port is available")
    elif pt3 > 49456 and pt3 < 49460:
        print("Port is available")
    else:
        print("FAILURE")

def query_handles(number, each_hand):
    number_list = register.emptyList()
    number = Counter(number_list("register"))
    if number != 0:
        number = number['register']
        print(number)
        each_hand = number.elements()
        print(list(each_hand))
    else:
        print("0")


def follow_procedure(follower, receiver):
    followers_list = []
    new_follower = input(follower)
    followers_list[0] = new_follower
    if(len(followers_list) != 0):
        for j in range(followers_list.len()):
            followers_list.append(new_follower)
        followers_list.sort()
        print("SUCCESS")
    else:
        print("FAILURE")


def drop(old_follower, old_receiver):
    delete_list = follow_procedure.followers_list()
    new_follower = input(old_follower)
    if(len(delete_list) != 0):
        for j in range(delete_list.len()):
            if delete_list[j] == new_follower:
                delete_list[j].remove()
            delete_list.sort()
            print("SUCCESS")
    else:
        print("FAILURE")



start()
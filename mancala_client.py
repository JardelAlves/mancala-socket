import socket
import select
import errno
import sys
from threading import Thread
import mancala_game as game

HEADER_LENGTH = 10

if len(sys.argv) != 3:
    print("Uso correto: python client.py <endereço de ip> <número da porta>")
    exit()

IP: str = sys.argv[1]
PORT: int = int(sys.argv[2])

my_username = input("Nome de usuário: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

def sendMessage():
    while True:
        message = input(f'{my_username} > ')

        if message == 'desconectar':
            print('Chat encerrado')
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)
            sys.exit()

        if message:
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)

def recieveMessage():
    while True:
        try:
            username_header = client_socket.recv(HEADER_LENGTH)

            if not len(username_header):
                print('\nConexão fechada pelo servidor')
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())

            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            if message == 'desconectar':
                print('\nChat encerrado pelo outro usuário')
                sys.exit()

            print(f"\n{username} > {message}\n{my_username} > ", end="")

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            continue

        except Exception as e:
            print('Reading error: '.format(str(e)))
            sys.exit()

threadSendMessage = Thread(target=sendMessage)
threadSendMessage.start()

threadReceiveMessage = Thread(target=recieveMessage)
threadReceiveMessage.start()

game.startGame()
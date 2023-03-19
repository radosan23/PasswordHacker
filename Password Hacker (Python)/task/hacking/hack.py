import socket
import sys


class PasswordHacker:
    def __init__(self):
        self.address = (sys.argv[1], int(sys.argv[2]))
        self.msg = sys.argv[3]

    def get_data(self):
        with socket.socket() as client:
            client.connect(self.address)
            client.send(self.msg.encode())
            return client.recv(1024).decode()


def main():
    hacker = PasswordHacker()
    print(hacker.get_data())


if __name__ == '__main__':
    main()

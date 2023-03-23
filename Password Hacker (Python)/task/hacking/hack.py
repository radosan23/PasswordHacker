import itertools
import os
import socket
import string
import sys


class PasswordHacker:
    def __init__(self, ip, port):
        self.address = (ip, int(port))
        self.client = None

    def connect(self):
        self.client = socket.socket()
        self.client.connect(self.address)

    def disconnect(self):
        self.client.close()

    def force_crack(self):
        letters = string.ascii_lowercase + string.digits
        n_letters = 0
        while True:
            n_letters += 1
            for password in itertools.product(letters, repeat=n_letters):
                password = ''.join(password)
                self.client.send(password.encode())
                if self.client.recv(1024).decode() == 'Connection success!':
                    return password

    def dictionary_crack(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.txt'), 'rt') as f:
            for word in f:
                combinations = [(x[0]) if x[0] == x[1] else x for x in zip(word.strip(), word.strip().upper())]
                for password in itertools.product(*combinations):
                    password = ''.join(password)
                    self.client.send(password.encode())
                    if self.client.recv(1024).decode() == 'Connection success!':
                        return password


def main():
    hacker = PasswordHacker(*sys.argv[1:])
    hacker.connect()
    print(hacker.dictionary_crack())
    hacker.disconnect()


if __name__ == '__main__':
    main()

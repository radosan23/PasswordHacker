import json
import socket


def set_server():
    true_data = {'login': 'su', 'password': 'SuP12e'}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('127.0.0.1', 9090))
        server.listen()
        conn, addr = server.accept()
        with conn:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                data = json.loads(data)
                print(data)
                if data == true_data:
                    msg = 'Connection success!'
                elif data['login'] == true_data['login'] and data['password'] \
                        and true_data['password'].startswith(data['password']):
                    msg = 'Exception happened during login'
                elif data['login'] == true_data['login']:
                    msg = 'Wrong password!'
                else:
                    msg = 'Wrong login!'
                conn.send(json.dumps({'result': msg}).encode())


set_server()

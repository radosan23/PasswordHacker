import socket


def set_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('127.0.0.1', 9090))
        server.listen()
        conn, addr = server.accept()
        with conn:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print(data)
                if data == 'qWerTy123':
                    conn.send('Connection success!'.encode())
                else:
                    conn.send('wrong!'.encode())


set_server()

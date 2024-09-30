import socket


def start(host="0.0.0.0", port=8000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))

    try:
        print(f"Started server on port {host}:{port}")
        while True:
            conn, addr = sock.accept()

            request = conn.recv(1024).decode()
            print(f"Received request {request}")

            response = "HTTP/1.0 200 OK\n\nHello, World!"
            conn.sendall(response.encode())
            conn.close()
    finally:
        sock.close()


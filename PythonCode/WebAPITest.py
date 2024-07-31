import sys
import time
import os
import socket
import json
import platform
import base64




api_options = ["/cpu","/temps","/status","/time","/"]

def NewResponder():
    addr = socket.getaddrinfo("0.0.0.0",8088)[0][-1] #port 80 does not work on WIndows atm.
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET,
                 socket.SO_REUSEADDR,1)
    s.bind(addr)
    s.listen()
    print(f"Listening on: {addr}")

    while True:
        response = {}

        #Review this stuffs: https://docs.python.org/3/library/socket.html#timeouts-and-the-accept-method
        cl,addr = s.accept()
        request_data = cl.recv(1024).split()
        request = request_data[1] if len(request_data) > 1 else "No Request"

        cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n'.encode())
        try:
            if request.decode() in api_options:
                match request.decode():
                    case "/cpu":
                        response = json.dumps({"machine_cpu": [platform.processor()]})
                    case "/time":
                        response = json.dumps({"Time": [time.localtime()]})
                    case other:
                        response = json.dumps({"DefaultRequest": [os.uname()]})

        except AttributeError:
            print("The type changed...moving on")
        except BrokenPipeError:
            print("Broken Pipe?, what did you do?")

        try:
            cl.send(str(response).encode())
            print(f"Sent {sys.getsizeof(response)} Bytes")
            print(f"Client: {addr} with request: {request}\nResponded with: {response}")

        except ConnectionAbortedError:
            print("Connection was aborted by the client.")
            
        cl.close()

NewResponder()


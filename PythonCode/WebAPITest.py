import time
import os
import socket
import json
import platform




def NewResponder():
    addr = socket.getaddrinfo("0.0.0.0",8088)[0][-1] #port 80 does not work on WIndows atm.
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET,
                 socket.SO_REUSEADDR,1)
    s.bind(addr)
    s.listen()
    print(f"Listening on: {addr}")

    
    

    while True:

        json_data = {
            "machine_arc": platform.architecture(),
            "os": platform.system()

        }
        response = json.dumps(json_data)

        cl,addr = s.accept()
        request_data = cl.recv(1024).split()
        request = request_data[1] if len(request_data) > 1 else "No Request"

        if request.decode() == "/":
            print("This is the default.")
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n'.encode())
        print(f"Client Connected from: {addr} with request: {request}\nResponded: {response} to client")

        if request.decode() =="/":
            response = json.dumps(
                {
                    "machine_cpu" : platform.processor()
                }
            )

        try:
            cl.send(response.encode())
            
        except ConnectionAbortedError:
            print("Connection was aborted by the client.")
            
        cl.close()

NewResponder()


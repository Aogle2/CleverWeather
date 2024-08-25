import sys
import time
import os
import socket
import json
import platform
import cpuinfo as info
import psutil




api_options = ["/cpu","/temps","/status","/time","/"]

#Socket programming https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

class newserver:
    def __init__(self,host="0.0.0.0",port=8088):
        self.address = socket.getaddrinfo(host,port, socket.AF_INET,socket.SOCK_STREAM)[0][4]
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.bind(self.address)

    def startlisten(self):
        self.sock.listen()
        #while True:
        #    conn ,addr = self.sock.accept()
        #    print(f"Connection from: {addr}")
        #    conn.close()

    def acceptnewconnection(self):
        pass
    def senddata(self):
        pass



server = newserver()

server.startlisten()

def NewResponder():
    addr = socket.getaddrinfo("0.0.0.0",8088)[0][-1] #port 80 does not work on WIndows atm.
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
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
                        response = json.dumps({"machine_cpu": [info.get_cpu_info()]})
                    case "/time":
                        response = json.dumps({"Time": [time.localtime()]})
                    case "/temps":
                        response = json.dumps({"Temps": [psutil.sensors_fans()]})
                    case '/':
                        response = json.dumps({"DefaultRequest": [os.uname()]})

        except AttributeError:
            print("The type changed...moving on")
        except BrokenPipeError:
            print("Broken Pipe?, what did you do?")

        try:
            cl.send(str(response).encode())
            print(f"Client: {addr} with request: {request.decode()}\n"
                  f"Responded with: {response}\n"
                  f" Data sent is {sys.getsizeof(response)} Bytes")

        except ConnectionAbortedError:
            print("Connection was aborted by the client.")
            
        cl.close()




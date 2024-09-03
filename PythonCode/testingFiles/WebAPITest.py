import sys
import time
import os
import socket
import json
import platform
import cpuinfo as info
import psutil
import time




api_options = ["/cpu","/temps","/status","/time","/"]

#Socket programming https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
#Work in some more improvements: https://www.delftstack.com/howto/python/get-ip-address-python/
#May look into using this for more improvements https://thepythoncode.com/article/make-a-chat-room-application-in-python
#More improvements https://www.golinuxcloud.com/python-multiprocessing/#:~:text=To%20use%20the%20multiprocessing%20features%20in%20your%20Python,and%20classes%3A%20python%20from%20multiprocessing%20import%20Process%2C%20Queue

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
        request_data = cl.recv(2048).split()
        request = request_data[1] if len(request_data) > 1 else "No Request"

        cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n'.encode()) #Need to figure out why this is sent.
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
                        response = json.dumps({"DefaultRequest": ["Nothing stated"]})
                    case _:
                        response = json.dumps({"Default Request":[]})

        except AttributeError:
            print("The type changed...moving on")
        except BrokenPipeError:
            print("Broken Pipe?, what did you do?")

        try:
            cl.send(str(response).encode())
            try:
                print(f"Client: {addr} with request in bytes: {request}\n"
                      f"Responded with: {response}\n"
                      f" Data sent is {sys.getsizeof(response)} Bytes")
            except AttributeError:
                print("Wrong encode for some stupid reason, nothing has changed?")

        except ConnectionAbortedError:
            print(f"Connection was aborted by the client: {addr}")

        cl.close()

NewResponder()




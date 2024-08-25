import json
import network
import socket
import time
import os
from machine import ADC
import machine

#Core Items
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("airCube-79E","local#123")


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen()
print('Listening on', addr)


# Main loop for handling client requests
        
while True:      
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        
        request = request.split()[1]
        print('Request:', request)
        
        adc = ADC(4)
        ADC_voltage = adc.read_u16() * (3.3 / (65535))  # Convert ADC reading to voltage
        temp_celcius = 27 - (ADC_voltage - 0.706)/0.001721  # Convert voltage to temperature
        temp_celcius= round(temp_celcius, 2)
        temp_celcius=temp_celcius-15
        temp_fahrenheit=32+(1.8*temp_celcius)
        
        
        # Create a dictionary with the temperature data
        temp_data = {
            "enviroment_info": [
            {
            "temp_celcius": temp_celcius,
            "temp_fahrenheit": temp_fahrenheit
            }
        ],
            "general_info" : [
            {
            "device" : os.uname()[-1],
            "cpu_freq" : machine.freq() /1_000_000,
            "device_location": "Barn Entrence"
            }
        ]
            
        }
        
        # Convert the dictionary to a JSON string
        response = json.dumps(temp_data)
        
        # Send the JSON response
        cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
        cl.send(response)
        cl.close()
        print("Connection Closed")

    except:
        pass
    time.sleep(0.1)
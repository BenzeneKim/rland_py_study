#-*-coding:utf-8-*-
import sys
import time
import serial
import serial.tools.list_ports

class SerialBasic(self):
    def port_search():
        available_port_list = list()
    ports = serial.tools.list_ports.comports()
    for p in ports:
        available_port_list.append(p.device)
    print(available_port_list)
        
def port_open(port):
    global process
    global robot
    robot = serial.serial_for_url(str(port), baudrate=115200, timeout=1)
    print("Opening port...")
    if robot.is_open:
        print("Robot connected : " + str(port))
        print("Start reading process")
        
        print("Start data calculation process")

    else:
        port_close()

def port_close():
    global robot
    while(robot.is_open):
        print("Disconnecting robot")
        robot.close()
        if robot.is_open:
            time.sleep(1)
    print("Port closed")    


    


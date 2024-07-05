import serial
import time
from queue import Queue
from robot.api.deco import library
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

@library
class HTP_temp:
    def __init__(self, port: str, baudrate: int):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port=self.port, baudrate=self.baudrate)
        self.data_queue = Queue()
        self.buffer_queue = Queue()
        self.can_bus_list = []
        self.data_log = {}
        self.flag = True

        self.start_time = 0

    @keyword
    def open_COM(self) -> None:
        if self.ser.isOpen:
            print('Connected !')
        else:
            self.ser.open()

    @keyword
    def write(self, dgc: str):
        if not dgc.endswith("\r\n"):
            dgc += "\r\n"
        #print('dgc =',dgc)
        self.ser.write(dgc.encode("ascii"))
        data_received = self.ser.readline().decode('utf-8')
        print(data_received)
        return data_received

    @keyword
    def can_send(self, CAN_ID: str, CAN_type: bool, Payload: str):
        dgc = "DG+CANSEND="
        dgc = dgc + CAN_ID +","+ CAN_type + "," + "[" + Payload + "]" + "\r"
        print('dgc =',dgc)
        self.ser.write(dgc.encode("ascii"))


    @keyword
    def start_record_can_bus(self):
        List = []
        while self.flag:
            temp = ''
            if self.ser.in_waiting > 0:
                dd = self.ser.read(size=self.ser.in_waiting)
                if not dd:
                    return
                ss = dd.decode('utf-8')
                temp += ss
                print('len of temp =', len(temp))
                print("just append:", temp)
                if "\r\n" in temp:
                    x2 = temp.split('\r\n')
                    print('*x2 =',x2)
                    for i in x2:
                        self.data_queue.put(i.split(','))
                        print('i=',i)
                    temp = ''
            else:
                print('')


            temp_item = []
        print('end of record')


    @keyword
    def stop(self, t: int):
        self.flag = False
        print('stop the flag')

    @keyword
    def time_out(self, seconds: str):
        time.sleep(int(seconds))

    def start(self):
        self.flag = True

'''

hy = HTP_temp("COM17",115200)
hy.open_COM()
dgc = b'\xFF\x00\x00\x00\x00\x00\x00\x00'
hy.write("AT")


time.sleep(1)
hy.write('AT+LOADTEST=1000,8,1,[\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,3000')
hy.write('AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,1000')
hy.write('AT+LOADTEST=1000,8,1,[\\x02\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,200')
hy.write('AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,2000')
hy.write('AT+LOADTEST=1000,8,1,[\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,200')
hy.write('AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,2000')
hy.write('AT+LOADTEST=1000,8,1,[\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,3000')
hy.write('ATT')
hy.write('AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,1000')
hy.write("AT+TEST=1")

for i in range(100):
    hy.write('AT+LOADTEST=1000,8,1,[\\x02\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,1000')
    hy.write('AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,2000')
    hy.write('AT+LOADTEST=1000,8,1,[\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,1000')
    hy.write('AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,2000')
    hy.write("AT+TEST=1")
    time.sleep(2)

print('done')
'''
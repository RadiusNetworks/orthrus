from serial import Serial
from serial import SerialException
from serial.tools import list_ports
import sys


class SerialDevice:

    vendor_id = 0x0403
    device_id = 0x6010
    baud_rate = 115200
    timeout = 1
    
    def __init__(self):
        self.port = None
        
    def find_device(self, vid, pid, sn=None):
        device = None
        port = None
        for i in list_ports.comports():
            if i.vid == vid and i.pid == pid:
                device = i.device
                break
        if device:
            try:
                port = Serial(port=device, baudrate=self.baud_rate, timeout=self.timeout)
                print('Serial Device found: ' + device)
                print("Serial Device Ready\r\nOpening port...")
            except SerialException:
                print('Couldn\'t open port')
                sys.exit()
        else:
            print('Serial Device not found, connect a device and try again')
            
        return port
    
    def read_line(self):
        rcv_str = None
        try:
            rcv_bytes = self.port.readline()
            rcv_str = str(rcv_bytes)
        except SerialException as e:
            print(str(e))
            sys.exit()
    
        return rcv_str
        
    def open(self):
        self.port = self.find_device(self.vendor_id, self.device_id)
    
    def close(self):
        try:
            print("Closing Serial Device...")
            self.port.close()
        except SerialException:
            print('Port already closed')
            sys.exit()
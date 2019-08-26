from serial import Serial
from serial import SerialException
from serial.tools import list_ports
import sys


class SerialDevice:

    vendor_id = 0x0403
    device_id = 0x6010
    baud_rate = 115200
    timeout = 1
    dev_list = []
    
    def __init__(self):
        self.port = None
        
    def find_device(self, vid, pid, sn=None):
        device = None
        port = None
        for i in list_ports.comports():
            if i.vid == vid and i.pid == pid:
                self.dev_list.append(i.device)

        if len(self.dev_list) > 0:
    
            print("Devices available:")
    
            for dev in self.dev_list:
                selection_str = "{}) {}"
                print(selection_str.format(self.dev_list.index(dev), dev))

            sys.stdout.write("Select device from list:")
            sys.stdout.flush()
            dev_index = int(sys.stdin.readline())
        
            if dev_index < len(self.dev_list):
                try:
                    port:Serial = Serial(port=self.dev_list[int(dev_index)], baudrate=self.baud_rate, timeout=self.timeout)
                    print('Serial Device found: ' + self.dev_list[int(dev_index)])
                    print("Serial Device Ready\r\nOpening port...")
                except SerialException as e:
                    print('Couldn\'t open port')
                    sys.exit()
            else:
                print("Invalid device selection, try again")
        else:
            print('Serial device not found, connect a device and try again')
            
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
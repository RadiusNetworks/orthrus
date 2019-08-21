#!/usr/bin/env python3

import sys
from orthrus.serialdevice import SerialDevice
import _thread
from orthrus.util.logger import DataLogger
from orthrus.util.argparser import ArgParser
from orthrus.ui.plotter import DataPlotter


def print_tof(distance):
    outstring = "Distance from transmitter: {}m"
    print(outstring.format(distance))


def get_distance_value(data):
    list = str.split(data, ":")
    list = list[1].split(",")
    return float(list[0])
        
    
def read_data_thread(thread_name, dev, isVerbose, logger=None, plotter=None):
    distance_label = "distance"
    print("Starting " + thread_name  + " Thread")
    print("Receiving receptor signal...")
    while True:
        rcv_line = dev.read_line()
        if distance_label in rcv_line:
            distance = get_distance_value(rcv_line)
            if logger is not None:
                logger.write(distance)
            if plotter is not None:
                plotter.update_data(distance)
            if isVerbose is True:
                print_tof(distance)


if __name__ == '__main__':
    
    isVerbose = False
    plotter = logger = device = None
    
    arg = ArgParser(ArgParser.TOF_DEMO_TYPE)
        
    device = SerialDevice()
    device.open()
        
    if device.port is not None:
        isVerbose = arg.do_verbose()
        if arg.do_log() is True:
            try:
                logger = DataLogger(arg.get_file_name(), DataLogger.TOF_LOG_DATA_TYPE)
            except SystemExit:
                sys.exit()
        if arg.do_show() == "xyplot":
            plotter = DataPlotter()
        try:
            _thread.start_new_thread(read_data_thread, ("Read_Data", device, isVerbose, logger, plotter))
            if plotter is not None:
                plotter.start()
            while True:
                pass
        except KeyboardInterrupt as e:
            _thread.exit()
        
        device.close()


#!/usr/local/bin/ python3

import sys
import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ["KIVY_NO_CONSOLELOG"] = "1"

from orthrus.ui.gauge import GaugeApp
from orthrus.serialdevice import SerialDevice
from orthrus.util.argparser import ArgParser
from orthrus.util.logger import DataLogger
from orthrus.ui.plotter import DataPlotter
import _thread


def print_aoa(angle):
    degree_sign = u'\N{DEGREE SIGN}'
    outstring = "Angle of arrival: {}{}"
    print(outstring.format(angle, degree_sign))

def parse_angle(aoaData):
    list = str.split(aoaData, ":")
    return int(float(list[1]))


def read_data_thread(threadName, device, isVerbose, logger, plotter, gauge):

    print('Starting ' + threadName + ' Thread...')
    print('Receiving transmitter signal')
    while True:
        rcv_str = device.read_line()
        if rcv_str is not None:
            if "AoA estimation" in rcv_str:
                angle = parse_angle(rcv_str)
                if logger is not None:
                    logger.write(angle)
                if plotter is not None:
                    plotter.update_data(angle)
                if gauge is not None:
                    gauge.update(angle)
                if isVerbose is True:
                    print_aoa(angle)


if __name__ == "__main__":
    
    isVerbose = False
    gauge = logger = device = plotter = None
    
    arg = ArgParser(ArgParser.AOA_DEMO_TYPE)
    
    device = SerialDevice()
    device.open()
        
    if device.port is not None:
        isVerbose = arg.do_verbose()
        if arg.do_log() is True:
            try:
                logger = DataLogger(arg.get_file_name(), DataLogger.AOA_LOG_DATA_TYPE)
            except SystemExit:
                sys.exit()
        if arg.do_show() == "gauge":
            print("Starting Gauge UI")
            gauge = GaugeApp()
        elif arg.do_show() == "xyplot":
            print("Starting XY Plot")
            plotter = DataPlotter()
        
        try:
            _thread.start_new_thread(read_data_thread, ("Read-Data", device, isVerbose, logger, plotter, gauge))
            if gauge is not None:
                gauge.run()
            elif plotter is not None:
                plotter.start()
            while True:
                pass
        except KeyboardInterrupt as e:
            _thread.exit()
    
        device.close()
        
    
    



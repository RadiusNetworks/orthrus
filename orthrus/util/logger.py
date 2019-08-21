import os
import datetime


class DataLogger:
    
    logdir = 'log/'
    AOA_LOG_DATA_TYPE = "Angle-of-Arrival"
    TOF_LOG_DATA_TYPE = "Time-of-Flight"
    
    def __init__(self, filename, logtype=''):
        self.filename = filename + '.txt'
        self.file = None
        self.filepath = self.logdir + self.filename
        if os.path.exists(self.filepath) is True:
            print('Log file with name ' + filename + ' already exists, provide a different name next time')
            raise SystemExit
        else:
            if os.path.isdir(self.logdir) is False:
                os.mkdir(self.logdir)
            self.file = open(self.filepath, 'w+')
            self.file.write("--> " + logtype + " Data Log <--\r\n")
            if logtype == self.AOA_LOG_DATA_TYPE:
                self.file.write("Timestamp, Angle(deg)\r\n")
                print("Logging AoA data to... " + self.filename)
            else:
                self.file.write("Timestamp, Distance(m)\r\n")
                print("Logging ToF data to... " + self.filename)
            self.file.close()
            
        
    def write(self, data):
        with open(self.filepath, 'a') as logfile:
            logstring = str(datetime.datetime.now().time()) + ',' + str(data) + '\r\n'
            logfile.write(logstring)
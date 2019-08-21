from argparse import ArgumentParser


class ArgParser:
    
    AOA_DEMO_SHOW_OPTIONS = {"xyplot", "gauge"}
    TOF_DEMO_SHOW_OPTIONS = {"xyplot"}
    AOA_DEMO_TYPE = "AoA_Demo"
    TOF_DEMO_TYPE = "ToF_Demo"
    
    def __init__(self, demotype):
        parser = ArgumentParser(description='Angle of Arrival Demo')

        parser.add_argument('-f', type=str, action='store', help='log file name', dest='filename')
        if demotype == self.AOA_DEMO_TYPE:
            parser.add_argument('--show', action='store', help='pretty visual of angle-of-arrival data',
                            choices=self.AOA_DEMO_SHOW_OPTIONS)
        else:
            parser.add_argument('--show', action='store', help='pretty visual of time-of-flight data',
                            choices=self.TOF_DEMO_SHOW_OPTIONS)
        parser.add_argument('-v', '--verbose', action='store_true', help='print telemetry data to stdout')
    
        self.args = parser.parse_args()
    
    def get_file_name(self):
        return self.args.filename
    
    def do_log(self):
        if self.args.filename is None:
            return False
        else:
            return True
        
    def do_show(self):
        return self.args.show
    
    def do_verbose(self):
        return self.args.verbose
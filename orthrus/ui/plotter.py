import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import signal

fig = plt.figure()
axis = fig.add_subplot(1, 1, 1)
line, = axis.plot([], [], color="blue")
moving_average = []
distance_average = []


class DataPlotter:
    
    distanceBWInHz = 250
    update_interval = 500
    
    def __init__(self):
        self.sampleNum = []
        self.distanceData = []
        self.moving_average = []
        self.distance_average = []
        FuncAnimation(fig, self.update, init_func=self.init, interval=self.update_interval, blit=True)
        
    def start(self):
        plt.show()

    def init(self):
        plt.title('Angle of Arrival')
        plt.xlabel('Sample(n)')
        plt.ylabel("Angle(degrees)")
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        return line,
    
    def update(self, frame):
        axis.clear()
        plt.title('Angle of Arrival')
        plt.xlabel('Sample(n)')
        plt.ylabel("Angle(degrees)")
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        axis.plot(self.sampleNum, self.distanceData)
        return line,
    
    def update_data(self, data):
        self.distanceData.append(data)
        self.sampleNum.append(len(self.distanceData))

    def filter_data(self):
        if len(self.distanceData) >= 10:
            self.moving_average = signal.medfilt(self.distanceData[len(self.distanceData) - 10: len(self.distanceData)], 9)
            self.distance_average.extend(self.moving_average.tolist())
            self.sampleNum = (list(range(0, len(self.distance_average), 1)))
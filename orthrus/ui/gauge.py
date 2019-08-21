from kivy.app import App
from kivy.garden.gauge import Gauge
from kivy.uix.boxlayout import BoxLayout


class GaugeApp(App):
    def __init__(self):
        self.gauge = None
        super().__init__()
    
    def update(self, value):
        if self.gauge != None:
            self.gauge.value = value + 50
    
    def build(self):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.gauge = Gauge(value=0, size_gauge=256, size_text=20)
        self.gauge._gauge.do_scale = True
        self.gauge._needle.do_scale = True
        self.gauge._gauge.do_translation = True
        self.gauge._needle.do_translation = True
        box.add_widget(self.gauge)
        return box
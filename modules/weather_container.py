import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets

import json

from utils import request

class WeatherContainer(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setFixedSize(828, 800)
        
        self.WEATHER_CONTEINER_LAYOUT = widgets.QVBoxLayout(self)
        self.WEATHER_CONTEINER_LAYOUT.setContentsMargins(0,0,0,0)
        self.WEATHER_CONTEINER_LAYOUT.setSpacing(20)
        self.WEATHER_CONTEINER_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.WEATHER_CONTEINER_LAYOUT)
        
        self.TOP_FRAME = widgets.QFrame(self)
        self.TOP_FRAME.setFixedSize(788, 36)
        self.TOP_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.1);")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.TOP_FRAME, alignment = core.Qt.AlignmentFlag.AlignHCenter)
        
        
        self.MAIN_FRAME = widgets.QFrame(self)
        self.MAIN_FRAME.setFixedSize(788, 677)
        self.MAIN_FRAME.setStyleSheet("border-radius: 17px;")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.MAIN_FRAME, alignment = core.Qt.AlignmentFlag.AlignHCenter)
        
        self.MAIN_FRAME_LAYOUT = widgets.QVBoxLayout(self.MAIN_FRAME)
        self.MAIN_FRAME.setLayout(self.MAIN_FRAME_LAYOUT)
        self.MAIN_FRAME_LAYOUT.setSpacing(10)
        self.MAIN_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        
        
        
        self.MOMENT_WEATHER_FRAME = widgets.QFrame(self.MAIN_FRAME)
        self.MOMENT_WEATHER_FRAME.setFixedSize(788, 303)
        self.MOMENT_WEATHER_FRAME.setStyleSheet("border-radius: 17px;")
        self.MAIN_FRAME_LAYOUT.addWidget(self.MOMENT_WEATHER_FRAME) 
        
        self.MOMENT_WEATHER_LAYOUT = widgets.QHBoxLayout(self.MOMENT_WEATHER_FRAME)
        self.MOMENT_WEATHER_FRAME.setLayout(self.MOMENT_WEATHER_LAYOUT)
        self.MOMENT_WEATHER_LAYOUT.setContentsMargins(0,0,0,0)
        self.MOMENT_WEATHER_LAYOUT.setSpacing(10)
        
        self.LEFT_MOMENT_FRAME = widgets.QFrame(self.MOMENT_WEATHER_FRAME)
        self.LEFT_MOMENT_FRAME.setFixedSize(390, 303)
        self.LEFT_MOMENT_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); border-radius: 17px;")
        self.MOMENT_WEATHER_LAYOUT.addWidget(self.LEFT_MOMENT_FRAME)
        
        self.RIGHT_MOMENT_FRAME = widgets.QFrame(self.MOMENT_WEATHER_FRAME)
        self.RIGHT_MOMENT_FRAME.setFixedSize(390, 303)
        self.RIGHT_MOMENT_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); border-radius: 17px;")
        self.MOMENT_WEATHER_LAYOUT.addWidget(self.RIGHT_MOMENT_FRAME)

        self.DAY_WEATHER_FRAME = widgets.QFrame(self.MAIN_FRAME) 
        self.DAY_WEATHER_FRAME.setFixedSize(788, 157)
        self.DAY_WEATHER_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); border-radius: 17px;")
        self.MAIN_FRAME_LAYOUT.addWidget(self.DAY_WEATHER_FRAME)
        
        self.DIAGRAM_FRAME = widgets.QFrame(self.MAIN_FRAME)
        self.DIAGRAM_FRAME.setFixedSize(788, 197)
        self.DIAGRAM_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); border-radius: 17px;")
        self.MAIN_FRAME_LAYOUT.addWidget(self.DIAGRAM_FRAME)
        # response = request("Sydney")
        
        # print(json.dumps(response, indent=4))
        
        # if response["cod"] != 404:
        #     label = widgets.QLabel(self.CETRAL_FRAME, text = str(response["main"]["temp"]))
        #     self.CENTRAL_LAYOUT.addWidget(label)
            
            
        #     city_label = widgets.QLabel(self.CETRAL_FRAME, text = str(response["name"]))
        #     self.CENTRAL_LAYOUT.addWidget(city_label)
        
        # self.CETRAL_FRAME = widgets.QFrame(self)
        # self.CETRAL_FRAME.setFixedSize(788, 303)
        # self.CETRAL_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); border-radius: 17px;")
        # self.WEATHER_CONTEINER_LAYOUT.addWidget(self.CETRAL_FRAME)
        
        # self.CENTRAL_LAYOUT = widgets.QHBoxLayout(self.CETRAL_FRAME)
        # self.CETRAL_FRAME.setLayout(self.CENTRAL_LAYOUT)
        
        # self.FOOTER = widgets.QFrame(parent = self)
        # self.FOOTER.setFixedSize(788, 364)
        # self.FOOTER.setStyleSheet("background-color: rgba(0, 0, 0, 0.1); border-radius: 17px;")
        # self.WEATHER_CONTEINER_LAYOUT.addWidget(self.FOOTER)

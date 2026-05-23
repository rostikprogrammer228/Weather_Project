import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets

class WeatherContainer(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setFixedSize(828, 800)
        
        self.setObjectName("WEATHER_CONTAINER")
        self.WEATHER_CONTEINER_LAYOUT = widgets.QVBoxLayout(self)
        self.WEATHER_CONTEINER_LAYOUT.setContentsMargins(0,0,0,0)
        self.WEATHER_CONTEINER_LAYOUT.setSpacing(20)
        self.WEATHER_CONTEINER_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.WEATHER_CONTEINER_LAYOUT)
        
        
        # Внутри weather frame
        self.TOP_FRAME = widgets.QFrame(self)
        self.TOP_FRAME.setFixedSize(788, 36)
        self.TOP_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.1);")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.TOP_FRAME, alignment = core.Qt.AlignmentFlag.AlignHCenter)
        
        # Внутри weather frame
        self.MAIN_FRAME = widgets.QFrame(self)
        self.MAIN_FRAME.setFixedSize(788, 677)
        self.MAIN_FRAME.setStyleSheet("border-radius: 17px;")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.MAIN_FRAME, alignment = core.Qt.AlignmentFlag.AlignHCenter)
        
        self.MAIN_FRAME_LAYOUT = widgets.QVBoxLayout(self.MAIN_FRAME)
        self.MAIN_FRAME.setLayout(self.MAIN_FRAME_LAYOUT)
        self.MAIN_FRAME_LAYOUT.setSpacing(10)
        self.MAIN_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        
        
        # Внутри main frame
        self.MOMENT_WEATHER_FRAME = widgets.QFrame(self.MAIN_FRAME)
        self.MOMENT_WEATHER_FRAME.setFixedSize(788, 303)
        self.MOMENT_WEATHER_FRAME.setStyleSheet("border-radius: 17px;")
        self.MAIN_FRAME_LAYOUT.addWidget(self.MOMENT_WEATHER_FRAME) 
        
        self.MOMENT_WEATHER_LAYOUT = widgets.QHBoxLayout(self.MOMENT_WEATHER_FRAME)
        self.MOMENT_WEATHER_FRAME.setLayout(self.MOMENT_WEATHER_LAYOUT)
        self.MOMENT_WEATHER_LAYOUT.setContentsMargins(0,0,0,0)
        self.MOMENT_WEATHER_LAYOUT.setSpacing(10)
        
        # Внутри moment weather frame
        self.LEFT_MOMENT_FRAME = widgets.QFrame(self.MOMENT_WEATHER_FRAME)
        self.LEFT_MOMENT_FRAME.setFixedSize(390, 303)
        self.LEFT_MOMENT_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 17px;")
        self.MOMENT_WEATHER_LAYOUT.addWidget(self.LEFT_MOMENT_FRAME)
        
        self.LEFT_MOMENT_LAYOUT = widgets.QVBoxLayout(self.LEFT_MOMENT_FRAME)
        self.LEFT_MOMENT_FRAME.setLayout(self.LEFT_MOMENT_LAYOUT)
        self.LEFT_MOMENT_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.LEFT_MOMENT_LAYOUT.setContentsMargins(0,0,0,0)
        self.LEFT_MOMENT_LAYOUT.setSpacing(16)
        # Внутри left moment frame
        self.LEFT_MOMENT_TOP_FRAME = widgets.QFrame(self.LEFT_MOMENT_FRAME)
        self.LEFT_MOMENT_TOP_FRAME.setFixedSize(358, 27)
        self.LEFT_MOMENT_TOP_FRAME.setStyleSheet("background-color: transparent;")
        self.LEFT_MOMENT_LAYOUT.addWidget(self.LEFT_MOMENT_TOP_FRAME,alignment = core.Qt.AlignmentFlag.AlignCenter)
        # Внутри left moment weather frame
        self.LEFT_CITY_LABEL = widgets.QLabel(self.LEFT_MOMENT_FRAME)
        self.LEFT_CITY_LABEL.setStyleSheet("font-family: 'Roboto';font-weight: 500; color: white; font-size: 44px; border-radius: 0px; background-color: transparent;")
        self.LEFT_CITY_LABEL.setFixedSize(390, 52)
        self.LEFT_CITY_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.LEFT_MOMENT_LAYOUT.addWidget(self.LEFT_CITY_LABEL, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        # Внутри left moment weather frame
        self.LEFT_WEATHER_FRAME = widgets.QFrame(self.LEFT_MOMENT_FRAME)
        self.LEFT_WEATHER_FRAME.setFixedSize(197,87)
        self.LEFT_WEATHER_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent;")
        self.LEFT_MOMENT_LAYOUT.addWidget(self.LEFT_WEATHER_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)

        self.LEFT_WEATHER_LAYOUT = widgets.QHBoxLayout(self.LEFT_WEATHER_FRAME)
        self.LEFT_WEATHER_FRAME.setLayout(self.LEFT_WEATHER_LAYOUT)
        self.LEFT_WEATHER_LAYOUT.setSpacing(0)
        self.LEFT_WEATHER_LAYOUT.setContentsMargins(0,0,0,0)
        self.LEFT_WEATHER_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        # Внутри left weather frame
        self.LEFT_WEATHER_ICON = widgets.QLabel(self.LEFT_WEATHER_FRAME)
        self.LEFT_WEATHER_ICON.setFixedSize(84, 87)
        self.LEFT_WEATHER_ICON.setStyleSheet("border-radius: 0px;")
        self.LEFT_WEATHER_LAYOUT.addWidget(self.LEFT_WEATHER_ICON)
        # Внутри left weather frame
        self.LEFT_WEATHER_LABEL = widgets.QLabel(self.LEFT_WEATHER_FRAME)
        self.LEFT_WEATHER_LABEL.setFixedSize(113, 87)
        self.LEFT_WEATHER_LABEL.setStyleSheet("color: white; font-size: 74px;border-radius: 0px;background-color: transparent;font-family: 'Roboto';font-weight: 500;")

        self.LEFT_WEATHER_LAYOUT.addWidget(self.LEFT_WEATHER_LABEL)
        # Внутри left moment weather frame
        self.LEFT_DESCRIPTION_FRAME = widgets.QFrame(self.LEFT_MOMENT_FRAME)
        self.LEFT_DESCRIPTION_FRAME.setFixedSize(259, 57)
        self.LEFT_DESCRIPTION_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent;")
        self.LEFT_MOMENT_LAYOUT.addWidget(self.LEFT_DESCRIPTION_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.LEFT_DESCRIPTION_LAYOUT = widgets.QVBoxLayout(self.LEFT_DESCRIPTION_FRAME)
        self.LEFT_DESCRIPTION_FRAME.setLayout(self.LEFT_DESCRIPTION_LAYOUT)
        self.LEFT_DESCRIPTION_LAYOUT.setContentsMargins(0,0,0,0)
        self.LEFT_DESCRIPTION_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignHCenter)
        # Внутри left description frame
        self.LEFT_DESCRIPTION_LABEL1 = widgets.QLabel(self.LEFT_DESCRIPTION_FRAME)
        self.LEFT_DESCRIPTION_LABEL1.setFixedSize(259, 28)
        self.LEFT_DESCRIPTION_LABEL1.setStyleSheet("color: white; font-size: 24px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.LEFT_DESCRIPTION_LABEL1.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.LEFT_DESCRIPTION_LAYOUT.addWidget(self.LEFT_DESCRIPTION_LABEL1, alignment = core.Qt.AlignmentFlag.AlignVCenter)
        # Внутри left description frame
        self.LEFT_DESCRIPTION_LABEL2 = widgets.QLabel(self.LEFT_DESCRIPTION_FRAME)
        self.LEFT_DESCRIPTION_LABEL2.setFixedSize(259, 19)
        self.LEFT_DESCRIPTION_LABEL2.setStyleSheet("color: rgba(255, 255, 255, 0.8); font-size: 16px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.LEFT_DESCRIPTION_LABEL2.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.LEFT_DESCRIPTION_LAYOUT.addWidget(self.LEFT_DESCRIPTION_LABEL2, alignment = core.Qt.AlignmentFlag.AlignVCenter)

        
        
        

        # Внутри moment weather frame
        self.RIGHT_MOMENT_FRAME = widgets.QFrame(self.MOMENT_WEATHER_FRAME)
        self.RIGHT_MOMENT_FRAME.setFixedSize(390, 303)
        self.RIGHT_MOMENT_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 17px;")
        self.MOMENT_WEATHER_LAYOUT.addWidget(self.RIGHT_MOMENT_FRAME)

        self.RIGHT_MOMENT_LAYOUT = widgets.QVBoxLayout(self.RIGHT_MOMENT_FRAME)
        self.RIGHT_MOMENT_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.RIGHT_MOMENT_FRAME.setLayout(self.RIGHT_MOMENT_LAYOUT)
        self.RIGHT_MOMENT_LAYOUT.setContentsMargins(0,0,0,0)
        self.RIGHT_MOMENT_LAYOUT.setSpacing(16)
        
        # Внутри right moment frame
        self.RIGHT_TODAY_FRAME = widgets.QFrame(self.RIGHT_MOMENT_FRAME)
        self.RIGHT_TODAY_FRAME.setFixedSize(358, 27)
        self.RIGHT_TODAY_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent; border-bottom: 1px solid #c7c07f;")
        self.RIGHT_MOMENT_LAYOUT.addWidget(self.RIGHT_TODAY_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.RIGHT_TODAY_LAYOUT = widgets.QHBoxLayout(self.RIGHT_TODAY_FRAME)
        self.RIGHT_TODAY_FRAME.setLayout(self.RIGHT_TODAY_LAYOUT)
        self.RIGHT_TODAY_LAYOUT.setContentsMargins(0,0,0,0)
        self.RIGHT_TODAY_LAYOUT.setSpacing(0)
        self.RIGHT_TODAY_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        # Внутри right moment frame
        self.RIGHT_TODAY_LABEL = widgets.QLabel(self.RIGHT_MOMENT_FRAME, text = "Сьогодні")
        self.RIGHT_TODAY_LABEL.setFixedSize(67, 19)
        self.RIGHT_TODAY_LABEL.setStyleSheet("color: white; font-size: 16px; border-radius: 0px;background-color: transparent; border: none;")
        self.RIGHT_TODAY_LAYOUT.addWidget(self.RIGHT_TODAY_LABEL, alignment = core.Qt.AlignmentFlag.AlignLeft)
        
        self.RIGHT_DATA_FRAME = widgets.QFrame(self.RIGHT_MOMENT_FRAME)
        self.RIGHT_DATA_FRAME.setFixedSize(358, 44)
        self.RIGHT_DATA_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent;")
        self.RIGHT_MOMENT_LAYOUT.addWidget(self.RIGHT_DATA_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.RIGHT_DATA_LAYOUT = widgets.QHBoxLayout(self.RIGHT_DATA_FRAME)
        self.RIGHT_DATA_FRAME.setLayout(self.RIGHT_DATA_LAYOUT)
        self.RIGHT_DATA_LAYOUT.setContentsMargins(0,0,0,0)
        self.RIGHT_DATA_LAYOUT.setSpacing(116)
        self.RIGHT_DATA_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        # Внутри right data frame
        self.RIGHT_DATA_LABEL1 = widgets.QLabel(self.RIGHT_DATA_FRAME)
        self.RIGHT_DATA_LABEL1.setFixedSize(119, 28)
        self.RIGHT_DATA_LABEL1.setStyleSheet("color: white; font-size: 24px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.RIGHT_DATA_LAYOUT.addWidget(self.RIGHT_DATA_LABEL1, alignment = core.Qt.AlignmentFlag.AlignLeft)
        # Внутри right data frame
        self.RIGHT_DATA_LABEL2 = widgets.QLabel(self.RIGHT_DATA_FRAME)
        self.RIGHT_DATA_LABEL2.setFixedSize(123, 28)
        self.RIGHT_DATA_LABEL2.setStyleSheet("color: white; font-size: 24px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.RIGHT_DATA_LAYOUT.addWidget(self.RIGHT_DATA_LABEL2, alignment = core.Qt.AlignmentFlag.AlignRight)
        # Внутри right moment frame
        self.RIGHT_CLOCK_FRAME = widgets.QLabel(self.RIGHT_MOMENT_FRAME)
        self.RIGHT_CLOCK_FRAME.setFixedSize(168,168)
        self.RIGHT_CLOCK_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent;")
        self.RIGHT_MOMENT_LAYOUT.addWidget(self.RIGHT_CLOCK_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.RIGHT_CLOCK_LAYOUT = widgets.QHBoxLayout(self.RIGHT_CLOCK_FRAME)
        self.RIGHT_CLOCK_FRAME.setLayout(self.RIGHT_CLOCK_LAYOUT)
        self.RIGHT_CLOCK_LAYOUT.setContentsMargins(0,0,0,0)
        self.RIGHT_CLOCK_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.RIGHT_CLOCK_LAYOUT.setSpacing(0)
        
        # Внутри right clock frame
        self.RIGHT_CLOCK_LABEL = widgets.QLabel(self.RIGHT_CLOCK_FRAME)
        self.RIGHT_CLOCK_LABEL.setFixedSize(74,34)
        self.RIGHT_CLOCK_LABEL.setStyleSheet("color: white; font-size: 29px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.RIGHT_CLOCK_LAYOUT.addWidget(self.RIGHT_CLOCK_LABEL)
        
        # Внутри main frame
        self.DAY_WEATHER_FRAME = widgets.QFrame(self.MAIN_FRAME) 
        self.DAY_WEATHER_FRAME.setFixedSize(788, 157)
        self.DAY_WEATHER_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 17px;")
        self.MAIN_FRAME_LAYOUT.addWidget(self.DAY_WEATHER_FRAME)
        
        
        # Внутри main frame
        self.DIAGRAM_FRAME = widgets.QFrame(self.MAIN_FRAME)
        self.DIAGRAM_FRAME.setFixedSize(788, 197)
        self.DIAGRAM_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 17px;")
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

import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core

from utils import json_write, request, clear_layout
from datetime import datetime, timezone, timedelta
from .vertical_card import Vertical_Card
from .sun_move_card import Sun_Move_Card


class Cards(widgets.QFrame):
   
    CARDS_LIST = []
    def __init__(self, parent, city_name):
        self.CITY_NAME = city_name
        super().__init__(parent)
        self.REQUEST_DATA = request(self.CITY_NAME, "current")
        
        
        self.data_time()
        self.SELECTED = False
        
        self.setStyleSheet("border-bottom: 1px solid #859892;")
        self.setFixedSize(330, 98)
        
        self.CARD_LAYOUT = widgets.QHBoxLayout()
        self.CARD_LAYOUT.setContentsMargins(0,0,0,0)
        
        self.setLayout(self.CARD_LAYOUT)

        self.FRAME1 = widgets.QFrame(parent = self)
        self.FRAME1.setFixedSize(200, 82)
        self.FRAME1.setStyleSheet("border: none; background-color: transparent;")
        self.FRAME1_LAYOUT = widgets.QVBoxLayout()
        self.FRAME1.setLayout(self.FRAME1_LAYOUT)
        
        self.FRAME1_LABEL1 = widgets.QLabel(text = self.REQUEST_DATA["name"], parent = self.FRAME1)
        self.FRAME1_LABEL1.setFixedSize(200,28)
        self.FRAME1_LABEL1.setStyleSheet("font-size: 24px; font-family: 'Roboto';font-weight: 500;")
        
        self.FRAME1_LABEL2 = widgets.QLabel(text = self.TIME_STR, parent = self.FRAME1)
        self.FRAME1_LABEL2.setStyleSheet("font-size: 12px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME1_LABEL2.setFixedSize(105,14)
        
        self.FRAME1_LABEL3 = widgets.QLabel(text = self.REQUEST_DATA["weather"][0]["description"].capitalize(), parent = self.FRAME1)
        self.FRAME1_LABEL3.setStyleSheet("font-size: 12px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME1_LABEL3.setFixedSize(105,14)
        
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL1)
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL2)
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL3)

        self.FRAME2 = widgets.QFrame(parent = self)
        self.FRAME2.setFixedSize(110, 82)
        self.FRAME2.setStyleSheet("border: none; background-color: transparent;")
        
        self.FRAME2_LAYOUT = widgets.QVBoxLayout()
        self.FRAME2_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.FRAME2_LAYOUT.setContentsMargins(0,0,0,0)
        self.FRAME2.setLayout(self.FRAME2_LAYOUT)
        
        self.FRAME2_LABEL1 = widgets.QLabel(text = f"{int(self.REQUEST_DATA["main"]["temp"])}°", parent = self.FRAME2)
        self.FRAME2_LABEL1.setStyleSheet("font-size: 44px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME2_LABEL1.setFixedSize(67,52 )
        
        
        self.FRAME2_LABEL2 = widgets.QLabel(text = f"Макс.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Мін.:{int(self.REQUEST_DATA["main"]["temp_min"])}°", parent = self.FRAME2)
        self.FRAME2_LABEL2.setStyleSheet("font-size: 12px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME2_LABEL2.setFixedSize(110,14)
        self.FRAME2_LABEL2.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        self.FRAME2_LAYOUT.addWidget(self.FRAME2_LABEL1, alignment = core.Qt.AlignmentFlag.AlignRight)
        self.FRAME2_LAYOUT.addWidget(self.FRAME2_LABEL2)
        
        self.CARD_LAYOUT.addWidget(self.FRAME1)
        self.CARD_LAYOUT.addStretch(1)
        self.CARD_LAYOUT.addWidget(self.FRAME2)
        
        Cards.CARDS_LIST.append(self)

    def data_time(self):
        city_timezone = self.REQUEST_DATA["timezone"]
        self.day_request_data = request(self.CITY_NAME, "daily")
        tz = timezone(timedelta(seconds=city_timezone))
        
        current_time = datetime.now(tz)
        self.TIME_STR = current_time.strftime("%H:%M")

        self.DAY_STR = current_time.strftime("%A")
        self.DATE = current_time.strftime("%d.%m.%Y")

        self.sunrise = self.REQUEST_DATA["sys"]["sunrise"]
        self.SUNRISE_TIME = datetime.fromtimestamp(self.sunrise + self.day_request_data["city"]["timezone"], timezone.utc)
        
        self.sunset = self.REQUEST_DATA["sys"]["sunset"] 
        self.SUNSET_TIME = datetime.fromtimestamp(self.sunset + self.day_request_data["city"]["timezone"], timezone.utc)
        

    def select(self):
        
        self.REQUEST_DATA = request(self.CITY_NAME, "current")
        self.day_request_data = request(self.CITY_NAME, "daily")
        
        weather_container = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER")
        
        clear_layout(weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT)
        clear_layout(weather_container.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT)
        clear_layout(weather_container.FORECAST_DIAGRAM_ITSELF_LAYOUT)
        # Цикл для получения данных о погоде в течение дня и отображения их в виде диаграммы и скролла с часами, температурой и иконкой погоды
        for index in range(len(self.day_request_data["list"])):
                hour_data = self.day_request_data["list"][index]
                hour_temp = hour_data["main"]["temp"]
                
                hour_time = datetime.fromtimestamp(hour_data["dt"]+ self.day_request_data["city"]["timezone"], timezone.utc).hour 
                if index <= 21:
                    weather_forecast_icon = widgets.QLabel(parent = weather_container.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME)
                    weather_forecast_icon.setFixedSize(16,16)
                    forecast_icon = gui.QPixmap(f"media/title_bar/scrollbar_weather_icons/{hour_data["weather"][0]["icon"]}.png")
                    
                    if not forecast_icon.isNull():
                        scaled_pixmap = forecast_icon.scaled(16,16, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                        weather_forecast_icon.setPixmap(scaled_pixmap)
                    weather_container.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT.addWidget(weather_forecast_icon, alignment = core.Qt.AlignmentFlag.AlignCenter)
                    
                    for i in range(3):
                        if hour_temp <= -10:
                            height = 0
                        else:  
                            height = 3 * int(hour_temp +10)
                        diagramma = widgets.QFrame(parent = weather_container.FORECAST_DIAGRAM_ITSELF_FRAME)
                        diagramma.setFixedWidth(8)
                        diagramma.setFixedHeight(height)
                        
                        diagramma.setStyleSheet("""background: qlineargradient(y1:0, y2:1, stop:0 #FFDF56 stop:1 #87CEFA);""")
                        
                        weather_container.FORECAST_DIAGRAM_ITSELF_LAYOUT.addWidget(diagramma, alignment = core.Qt.AlignmentFlag.AlignBottom)
                
                if index == 0:
                    self.TEXT_LABEL = "Зараз"
                
                
                
                if hour_time > 24:
                    hour_time -=24
                elif hour_time < 0:
                    hour_time +=24
                

                if index + 1 < len(self.day_request_data["list"]):
                    next_hour = datetime.fromtimestamp(self.day_request_data["list"][index + 1]["dt"] + self.day_request_data["city"]["timezone"], timezone.utc).hour
                    
                    if next_hour > 24:
                        next_hour -=24
                    elif next_hour <= 0 :
                        next_hour += 24    
                else:
                    next_hour = None
              
                
                vertical_card = Vertical_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME)
                if self.TEXT_LABEL:
                    vertical_card.TIME_LABEL.setText(f"{self.TEXT_LABEL}")
                    self.TEXT_LABEL = None
                else:
                    vertical_card.TIME_LABEL.setText(f"{hour_time}")
                pixmap_scroll_card = gui.QPixmap(f"media/title_bar/scrollbar_weather_icons/{hour_data["weather"][0]["icon"]}.png")
               
                if not pixmap_scroll_card.isNull():
                    scaled_pixmap = pixmap_scroll_card.scaled(24,24, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                    vertical_card.WEATHER_LABEL.setPixmap(scaled_pixmap)
                    
                vertical_card.TEMPERATURE_LABEL.setText(f"{int(hour_temp)}°")
                weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT.addWidget(vertical_card)
                
                if next_hour is not None and self.SUNRISE_TIME.hour >= hour_time and self.SUNRISE_TIME.hour < next_hour:
                    sunrise_card = Sun_Move_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME)
                    if self.TEXT_LABEL:
                        sunrise_card.TIME_LABEL.setText(f"{self.TEXT_LABEL}") 
                        self.TEXT_LABEL = None
                    else:
                        sunrise_card.TIME_LABEL.setText(f"{self.SUNRISE_TIME.strftime('%H:%M')}") 
                    sunrise_pixmap = gui.QPixmap(f"media/title_bar/sunmove_icons/sunrise.png")
                    
                    if not sunrise_pixmap.isNull():
                        scaled_pixmap = sunrise_pixmap.scaled(sunrise_card.ICON_LABEL.size(), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                        sunrise_card.ICON_LABEL.setPixmap(scaled_pixmap)
                    
                    sunrise_card.TEXT_LABEL.setText("Схід сонця")
                    weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT.addWidget(sunrise_card)
                
                elif next_hour is not None and self.SUNSET_TIME.hour >= hour_time and self.SUNSET_TIME.hour < next_hour:
                    sunset_card = Sun_Move_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME)
                    if self.TEXT_LABEL:
                        sunset_card.TIME_LABEL.setText(f"{self.TEXT_LABEL}")
                        self.TEXT_LABEL = None
                    else:
                        sunset_card.TIME_LABEL.setText(f"{self.SUNSET_TIME.strftime('%H:%M')}")
                    
                    
                    sunset_pixmap = gui.QPixmap(f"media/title_bar/sunmove_icons/sunset.png")
                    if not sunset_pixmap.isNull():
                        scaled_pixmap = sunset_pixmap.scaled(24,24, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                        sunset_card.ICON_LABEL.setPixmap(scaled_pixmap)
                        
                    sunset_card.TEXT_LABEL.setText("Захід сонця")    
                    weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT.addWidget(sunset_card) 
                
                self.TEXT_LABEL = None
            
                
        weather_container.LEFT_CITY_LABEL.setText(self.REQUEST_DATA["name"])
            # temperature
        weather_container.LEFT_WEATHER_LABEL.setText(f"{int(self.REQUEST_DATA["main"]["temp"])}°")
            
            # description
        weather_container.LEFT_DESCRIPTION_LABEL1.setText(self.REQUEST_DATA["weather"][0]["description"].capitalize())
            # max min temp
        weather_container.LEFT_DESCRIPTION_LABEL2.setText(f"Макс.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Мін.:{int(self.REQUEST_DATA["main"]["temp_min"])}°")
            
            
        pixmap = gui.QPixmap(f"media/title_bar/weather_icons/{self.REQUEST_DATA["weather"][0]["icon"]}.png")

        if not pixmap.isNull():
            scaled = pixmap.scaled(weather_container.LEFT_WEATHER_ICON_SIZE, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
            weather_container.LEFT_WEATHER_ICON.setPixmap(scaled)
            # Запись в правую часть контейнера погоды данных о погоде с запроса API при каждом клике на карточку
        weather_container.RIGHT_DATA_LABEL1.setText(self.DAY_STR.capitalize())
            
        weather_container.RIGHT_DATA_LABEL2.setText(self.DATE)
            
        weather_container.RIGHT_CLOCK_LABEL.setText(self.TIME_STR)
            
        weather_container.RIGHT_CLOCK_FRAME.setPixmap(gui.QPixmap(f"media/title_bar/clock.svg"))
            
            
            # Обновление данных на карточке, которая была выбрана
        self.FRAME1_LABEL2.setText(self.TIME_STR)
        self.FRAME1_LABEL3.setText(self.REQUEST_DATA["weather"][0]["description"].capitalize())
        self.FRAME2_LABEL1.setText(f"{int(self.REQUEST_DATA["main"]["temp"])}°")
        self.FRAME2_LABEL2.setText(f"Макс.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Мін.:{int(self.REQUEST_DATA["main"]["temp_min"])}°")
            
        for card in Cards.CARDS_LIST:
            if card.SELECTED:
                card.setStyleSheet("background-color: transparent; border-radius:0px;border-bottom: 1px solid #859892;")
                card.SELECTED = False

        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border-radius: 8px;border-bottom: 1px solid #859892;")
        self.SELECTED = True
            

    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton :
            self.window().findChild(widgets.QLineEdit, "SEARCH_FIELD").DROP_DOWN_FRAME.hide()
        if event.button() == core.Qt.MouseButton.LeftButton and self.SELECTED == False:
    
            self.select()
        

            
            
           # print(f"city - {self.DAY_REQUEST_DATA["city"]["name"]}")
                # print(f"hour_data - {self.HOUR_TIME}")
                # print(f"data - {datetime.fromtimestamp(self.DAY_REQUEST_DATA["list"][index]["dt"],timezone.utc).hour + self.DAY_REQUEST_DATA["city"]["timezone"] // 3600} ")
                # print(f"index - {index} ")
                # print(f"timezone - {self.DAY_REQUEST_DATA["city"]["timezone"]} ")
                # print(f"city - {self.DAY_REQUEST_DATA["city"]["name"]}")
                # print(f"temperature - {self.DAY_REQUEST_DATA["list"][index]["main"]["temp"]}")
                # print(f"hour_data - {hour_data["main"]["temp"]}")
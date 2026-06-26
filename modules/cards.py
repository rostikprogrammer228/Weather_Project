import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core

from utils import json_write, request, clear_layout
from datetime import datetime, timezone, timedelta
from .vertical_card import Vertical_Card
from .sun_move_card import Sun_Move_Card
from utils import close_drop_menu
from utils import scale
class Cards(widgets.QFrame):
    
    CARDS_LIST = []
    def __init__(self, parent, city_name):
        
        super().__init__(parent)
        
        self.setObjectName("CARD")
        self.CITY_NAME = city_name
        self.REQUEST_DATA = request(self.CITY_NAME, "current")
        self.GEOCODING_DATA = request(self.CITY_NAME, "geocoding")
        json_write("current.json",self.REQUEST_DATA)
        json_write("geocoding.json",self.GEOCODING_DATA)
        
        self.data_time()
        self.language_widget = self.window().findChild(widgets.QFrame, "WEATHER_CONTAINER")
        self.current_language = self.language_widget.LANGUAGE
        self.language = self.language_widget.LANGUAGE
        if self.language == "Українська":
            
            self.frame1_label3 = self.REQUEST_DATA["weather"][0]["description"].capitalize()
            self.max_min_temp = f"Макс.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Мін.:{int(self.REQUEST_DATA["main"]["temp_min"])}°"
            try:
                self.CITY_TEXT = self.GEOCODING_DATA[0]["local_names"]["uk"]  
            except:
                self.CITY_TEXT = self.CITY_NAME
        elif self.language == "English" :
            
            self.frame1_label3 = self.REQUEST_DATA["weather"][0]["main"].capitalize()
            self.max_min_temp = f"Max.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Min.:{int(self.REQUEST_DATA["main"]["temp_min"])}°"
            self.CITY_TEXT = self.CITY_NAME
        
        
        
        self.SELECTED = False
        
        self.setStyleSheet("border-bottom: 1px solid #859892;")
        self.setFixedSize(scale.scale_x(330), scale.scale_y(98))
        
        self.CARD_LAYOUT = widgets.QHBoxLayout()
        self.CARD_LAYOUT.setContentsMargins(scale.scale_x(8),scale.scale_y(8),scale.scale_x(8),scale.scale_y(8))
        
        self.setLayout(self.CARD_LAYOUT)
        
        self.FRAME1 = widgets.QFrame(parent = self)
        self.FRAME1.setFixedSize(scale.scale_x(200), scale.scale_y(82))
        self.FRAME1.setStyleSheet("border: none; background-color: transparent;")
        self.FRAME1_LAYOUT = widgets.QVBoxLayout()
        self.FRAME1.setLayout(self.FRAME1_LAYOUT)
        
       
        self.FRAME1_LABEL1 = widgets.QLabel(text = self.CITY_TEXT, parent = self.FRAME1)
        self.FRAME1_LABEL1.setFixedSize(scale.scale_x(200), scale.scale_y(28))
        self.FRAME1_LABEL1.setStyleSheet("font-family: 'Roboto';font-weight: 500; color: white;")
        scale.setFontSize(self.FRAME1_LABEL1,24)
        
        self.FRAME1_LABEL2 = widgets.QLabel(text = self.TIME_STR, parent = self.FRAME1)
        self.FRAME1_LABEL2.setStyleSheet(" font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME1_LABEL2.setFixedSize(scale.scale_x(105), scale.scale_y(14))
        scale.setFontSize(self.FRAME1_LABEL2,12)
        
        self.FRAME1_LABEL3 = widgets.QLabel(text = self.frame1_label3, parent = self.FRAME1)
        self.FRAME1_LABEL3.setStyleSheet(" font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME1_LABEL3.setFixedSize(scale.scale_x(105), scale.scale_y(14))
        scale.setFontSize(self.FRAME1_LABEL3,12)
        
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL1)
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL2)
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL3)

        self.FRAME2 = widgets.QFrame(parent = self)
        self.FRAME2.setFixedSize(scale.scale_x(110), scale.scale_y(82))
        self.FRAME2.setStyleSheet("border: none; background-color: transparent;")
        
        self.FRAME2_LAYOUT = widgets.QVBoxLayout()
        self.FRAME2_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.FRAME2_LAYOUT.setContentsMargins(0,0,0,0)
        self.FRAME2.setLayout(self.FRAME2_LAYOUT)
        
        self.FRAME22 = widgets.QFrame(parent = self.FRAME2)
        self.FRAME22.setFixedSize(scale.scale_x(85), scale.scale_y(52))
        self.FRAME22.setStyleSheet("border: none; background-color: transparent;")
        
        self.FRAME22_LAYOUT = widgets.QHBoxLayout()
        self.FRAME22_LAYOUT.setContentsMargins(0,0,0,0)
        self.FRAME22_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.FRAME22_LAYOUT.setSpacing(scale.scale_x(3))
        self.FRAME22.setLayout(self.FRAME22_LAYOUT)
        
        self.FRAME2_LABEL1 = widgets.QLabel(text = f"{int(self.REQUEST_DATA["main"]["temp"])}", parent = self.FRAME22)
        self.FRAME2_LABEL1.setStyleSheet("font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        scale.setFontSize(self.FRAME2_LABEL1,44)
        self.FRAME2_LABEL1.setFixedHeight(scale.scale_y(52))
        self.FRAME22_LAYOUT.addWidget(self.FRAME2_LABEL1, alignment= core.Qt.AlignmentFlag.AlignRight and core.Qt.AlignmentFlag.AlignTop)
        
        self.FRAME2_LABEL11 = widgets.QLabel(text = "°", parent = self.FRAME22)
        self.FRAME2_LABEL11.setStyleSheet(" font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        scale.setFontSize(self.FRAME2_LABEL11,39)
        self.FRAME2_LABEL11.setFixedHeight(scale.scale_y(44))
        self.FRAME2_LABEL11.setAlignment(core.Qt.AlignmentFlag.AlignBottom)
        self.FRAME22_LAYOUT.addWidget(self.FRAME2_LABEL11, alignment= core.Qt.AlignmentFlag.AlignLeft )
        
        self.FRAME2_LABEL2 = widgets.QLabel(text = self.max_min_temp, parent = self.FRAME2)
        self.FRAME2_LABEL2.setStyleSheet("font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        scale.setFontSize(self.FRAME2_LABEL2,12)
        self.FRAME2_LABEL2.setFixedSize(scale.scale_x(110), scale.scale_y(14))
        self.FRAME2_LABEL2.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        self.FRAME2_LAYOUT.addWidget(self.FRAME22, alignment = core.Qt.AlignmentFlag.AlignRight)
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
        
    def week_day_translate(self)  :   
        days = (("Monday","Понеділок"),("Tuesday","Вівторок"),("Wednesday","Середа"),("Thursday","Четвер"),("Friday","П'ятниця"),("Saturday","Субота"),("Sunday","Неділя")) 
        for day in days:
            if day[0].lower() == self.DAY_STR.lower():
                self.UA_DAY_STR = day[1].capitalize()
        return self.UA_DAY_STR
    def select(self):
        self.DIAGRAMM_ICON_LIST = []
        self.DIAGRAMM_LIST = []
        self.VERTICAL_CARD_LIST = []
        self.SUNMOVE_CARDS_LIST = []
        self.language = self.language_widget.LANGUAGE
        self.REQUEST_DATA = request(self.CITY_NAME, "current")
        self.day_request_data = request(self.CITY_NAME, "daily")
        self.data_time()
        self.week_day_translate()
        if self.language == "Українська":
            try:
                self.CITY_TEXT =  self.GEOCODING_DATA[0]["local_names"]["uk"]  
            except:
                self.CITY_TEXT = self.CITY_NAME
            self.frame1_label3 = self.REQUEST_DATA["weather"][0]["description"].capitalize()
            self.max_min_temp = f"Макс.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Мін.:{int(self.REQUEST_DATA["main"]["temp_min"])}°"
            self.now_text_label = "Зараз"
            self.sunrise_card_label = "Схід сонця"
            self.sunset_card_label = "Захід сонця"
            self.day_str = self.UA_DAY_STR
        elif self.language == "English" :
            self.CITY_TEXT = self.CITY_NAME
            self.frame1_label3 = self.REQUEST_DATA["weather"][0]["main"].capitalize()
            self.max_min_temp = f"Max.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Min.:{int(self.REQUEST_DATA["main"]["temp_min"])}°"
            self.now_text_label = "Now"
            self.sunrise_card_label = "Sunrise"
            self.sunset_card_label = "Sunset"
            self.day_str = self.DAY_STR
        
        weather_container = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER")
        
        clear_layout(weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT)
        clear_layout(weather_container.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT)
        clear_layout(weather_container.FORECAST_DIAGRAM_ITSELF_LAYOUT)
        # Цикл для получения данных о погоде в течение дня и отображения их в виде диаграммы и скролла с часами, температурой и иконкой погоды
        for self.INDEX in range(len(self.day_request_data["list"])):
                self.hour_data = self.day_request_data["list"][self.INDEX]
                hour_temp = self.hour_data["main"]["temp"]
                
                hour_time = datetime.fromtimestamp(self.hour_data["dt"]+ self.day_request_data["city"]["timezone"], timezone.utc).hour 
                if self.INDEX <= 21:
                    self.weather_forecast_icon = widgets.QLabel(parent = weather_container.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME)
                    self.DIAGRAMM_ICON_LIST.append(self.weather_forecast_icon)
                    self.weather_forecast_icon.setFixedSize(scale.scale_x(16), scale.scale_y(16))
                    forecast_icon = gui.QPixmap(f"media/title_bar/scrollbar_weather_icons/{self.hour_data["weather"][0]["icon"]}.png")
                    
                    if not forecast_icon.isNull():
                        scaled_pixmap = forecast_icon.scaled(scale.scale_x(16), scale.scale_y(16), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                        self.weather_forecast_icon.setPixmap(scaled_pixmap)
                        
                    weather_container.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT.addWidget(self.weather_forecast_icon, alignment = core.Qt.AlignmentFlag.AlignCenter)
                    
                    for i in range(3):
                        if hour_temp <= -10:
                            self.heightt = 0
                        else:  
                            self.heightt = 3 * int(hour_temp +10)
                        self.diagramma = widgets.QFrame(parent = weather_container.FORECAST_DIAGRAM_ITSELF_FRAME)
                        self.diagramma.base_height = self.heightt
                        self.diagramma.setFixedWidth(scale.scale_x(8))
                        self.diagramma.setFixedHeight(scale.scale_y(self.heightt))
                        self.DIAGRAMM_LIST.append(self.diagramma)
                        
                        self.diagramma.setStyleSheet("""background: qlineargradient(y1:0, y2:1, stop:0 #FFDF56 stop:1 #87CEFA);""")
                        
                        weather_container.FORECAST_DIAGRAM_ITSELF_LAYOUT.addWidget(self.diagramma, alignment = core.Qt.AlignmentFlag.AlignBottom)
                
                if self.INDEX == 0:
                    self.TEXT_LABEL = self.now_text_label
                
                
                
                if hour_time > 24:
                    hour_time -=24
                elif hour_time < 0:
                    hour_time +=24
                

                if self.INDEX + 1 < len(self.day_request_data["list"]):
                    next_hour = datetime.fromtimestamp(self.day_request_data["list"][self.INDEX + 1]["dt"] + self.day_request_data["city"]["timezone"], timezone.utc).hour
                    
                    if next_hour > 24:
                        next_hour -=24
                    elif next_hour <= 0 :
                        next_hour += 24    
                else:
                    next_hour = None
              
                
                vertical_card = Vertical_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME)
                vertical_card.hour_data = self.hour_data
                self.VERTICAL_CARD_LIST.append(vertical_card)
                if self.TEXT_LABEL:
                    vertical_card.TIME_LABEL.setText(f"{self.TEXT_LABEL}")
                    if self.TEXT_LABEL == self.now_text_label:
                        self.FIRST_VERTICAL_CARD = vertical_card
                    self.TEXT_LABEL = None
                else:
                    vertical_card.TIME_LABEL.setText(f"{hour_time}")
                self.pixmap_scroll_card = gui.QPixmap(f"media/title_bar/scrollbar_weather_icons/{self.hour_data["weather"][0]["icon"]}.png")
               
                if not self.pixmap_scroll_card.isNull():
                    scaled_pixmap = self.pixmap_scroll_card.scaled(scale.scale_x(24),scale.scale_y(24), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                    vertical_card.WEATHER_LABEL.setPixmap(scaled_pixmap)
                    
                vertical_card.TEMPERATURE_LABEL.setText(f"{int(hour_temp)}°")
                weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT.addWidget(vertical_card)
                
                if next_hour is not None and self.SUNRISE_TIME.hour >= hour_time and self.SUNRISE_TIME.hour < next_hour:
                    sunrise_card = Sun_Move_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME)
                    self.SUNMOVE_CARDS_LIST.append(sunrise_card)
                    if self.TEXT_LABEL:
                        sunrise_card.TIME_LABEL.setText(f"{self.TEXT_LABEL}") 
                        self.TEXT_LABEL = None
                    else:
                        sunrise_card.TIME_LABEL.setText(f"{self.SUNRISE_TIME.strftime('%H:%M')}") 
                    sunrise_pixmap = gui.QPixmap(f"media/title_bar/sunmove_icons/sunrise.png")
                    
                    if not sunrise_pixmap.isNull():
                        scaled_pixmap = sunrise_pixmap.scaled(sunrise_card.ICON_LABEL.size(), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                        sunrise_card.ICON_LABEL.setPixmap(scaled_pixmap)
                    
                    sunrise_card.TEXT_LABEL.setText(self.sunrise_card_label)
                    weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT.addWidget(sunrise_card)
                
                elif next_hour is not None and self.SUNSET_TIME.hour >= hour_time and self.SUNSET_TIME.hour < next_hour:
                    sunset_card = Sun_Move_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME)
                    self.SUNMOVE_CARDS_LIST.append(sunset_card)
                    if self.TEXT_LABEL:
                        sunset_card.TIME_LABEL.setText(f"{self.TEXT_LABEL}")
                        self.TEXT_LABEL = None
                    else:
                        sunset_card.TIME_LABEL.setText(f"{self.SUNSET_TIME.strftime('%H:%M')}")
                    
                    
                    sunset_pixmap = gui.QPixmap(f"media/title_bar/sunmove_icons/sunset.png")
                    if not sunset_pixmap.isNull():
                        scaled_pixmap = sunset_pixmap.scaled(scale.scale_x(24), scale.scale_y(24), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                        sunset_card.ICON_LABEL.setPixmap(scaled_pixmap)
                        
                    sunset_card.TEXT_LABEL.setText(self.sunset_card_label)    
                    weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT.addWidget(sunset_card) 
                
                self.TEXT_LABEL = None
            
        
        weather_container.LEFT_CITY_LABEL.setText(self.CITY_TEXT)
       
        weather_container.LEFT_WEATHER_LABEL.setText(f"{int(self.REQUEST_DATA["main"]["temp"])}")
            
        weather_container.LEFT_WEATHER_LABEL11.setText("°")
            
        weather_container.LEFT_DESCRIPTION_LABEL1.setText(self.frame1_label3)
            
        weather_container.LEFT_DESCRIPTION_LABEL2.setText(self.max_min_temp)
            
        weather_icons_pack = self.window().findChild(widgets.QFrame, "APPICONS").WEATHER_ICONS_PACK
        
        pixmap = gui.QPixmap(f"media/title_bar/weather_icons/weather_icons_{weather_icons_pack}/{self.REQUEST_DATA["weather"][0]["icon"]}.png")

        if not pixmap.isNull():
            scaled = pixmap.scaled(scale.scale_x(76), scale.scale_y(76), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
            weather_container.LEFT_WEATHER_ICON.setPixmap(scaled)
            # Запись в правую часть контейнера погоды данных о погоде с запроса API при каждом клике на карточку
            
        weather_container.RIGHT_DATA_LABEL1.setText(self.day_str)
            
        weather_container.RIGHT_DATA_LABEL2.setText(self.DATE)
            
        weather_container.RIGHT_CLOCK_LABEL.setText(self.TIME_STR)
            
            
        self.CLOCK = gui.QPixmap(f"media/title_bar/clock.svg")
        if not self.CLOCK.isNull():
            scaled_pixmap = self.CLOCK.scaled(scale.scale_x(168), scale.scale_y(168), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
            
            weather_container.RIGHT_CLOCK_FRAME.setPixmap(scaled_pixmap)
            
            
            # Обновление данных на карточке, которая была выбрана
        self.FRAME1_LABEL2.setText(self.TIME_STR)
        self.FRAME1_LABEL3.setText(self.frame1_label3)
        self.FRAME2_LABEL1.setText(f"{int(self.REQUEST_DATA["main"]["temp"])}")
        self.FRAME2_LABEL2.setText(self.max_min_temp)
            
        for card in Cards.CARDS_LIST:
            if card.SELECTED:
                card.setStyleSheet("background-color: transparent; border-radius:0px;border-bottom: 1px solid #859892;")
                card.SELECTED = False

        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border-radius: 8px;border-bottom: 1px solid #859892;")
        self.SELECTED = True
            
    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton :
            close_drop_menu(self.window())
        if event.button() == core.Qt.MouseButton.LeftButton and self.SELECTED == False:
    
            self.select()

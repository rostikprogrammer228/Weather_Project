import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from utils import request
from datetime import datetime, timezone, timedelta

class Cards(widgets.QFrame):
   
    CARDS_LIST = []
    def __init__(self, parent, city_name):
        self.CITY_NAME = city_name
        super().__init__(parent)
        
        self.REQUEST_DATA = request(self.CITY_NAME)
        
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
        
        self.FRAME2_LABEL1 = widgets.QLabel(text = f"{int(self.REQUEST_DATA['main']['temp']-273)}°", parent = self.FRAME2)
        self.FRAME2_LABEL1.setStyleSheet("font-size: 44px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME2_LABEL1.setFixedSize(67,52 )
        
        
        self.FRAME2_LABEL2 = widgets.QLabel(text = f"Макс.:{int(self.REQUEST_DATA['main']['temp_max']-273)}°, Мін.:{int(self.REQUEST_DATA['main']['temp_min']-273)}°", parent = self.FRAME2)
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
        tz = timezone(timedelta(seconds=city_timezone))
        
        current_time = datetime.now(tz)
        self.TIME_STR = current_time.strftime("%H:%M")
        self.DAY_STR = current_time.strftime("%A")
        self.DATE = current_time.strftime("%d.%m.%Y")

        sunrise = self.REQUEST_DATA["sys"]["sunrise"] + city_timezone
        self.SUNRISE_TIME = datetime.fromtimestamp(sunrise).strftime("%H:%M")
        
        sunset = self.REQUEST_DATA["sys"]["sunset"] + city_timezone
        self.SUNSET_TIME = datetime.fromtimestamp(sunset).strftime("%H:%M")
        

    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton and self.SELECTED == False:
            self.REQUEST_DATA = request(self.CITY_NAME)
            self.data_time()
            
            weather_container = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER")
            # city
            weather_container.LEFT_CITY_LABEL.setText(self.REQUEST_DATA["name"])
            # temperature
            weather_container.LEFT_WEATHER_LABEL.setText(f"{int(self.REQUEST_DATA['main']['temp']-273)}°")
            # description
            weather_container.LEFT_DESCRIPTION_LABEL1.setText(self.REQUEST_DATA["weather"][0]["description"].capitalize())
            # max min temp
            weather_container.LEFT_DESCRIPTION_LABEL2.setText(f"Макс.:{int(self.REQUEST_DATA['main']['temp_max']-273)}°, Мін.:{int(self.REQUEST_DATA['main']['temp_min']-273)}°")
            
            pixmap = None
            if self.TIME_STR >= self.SUNRISE_TIME and self.TIME_STR < self.SUNSET_TIME:
                if self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Clear":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/sunny_day.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Thunderstorm":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/rain_and_thunderstorm_day.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Drizzle":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/rainy_day.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Rain":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/Cloudy_with_rain_day.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Snow":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/snowy_day.svg")
                elif self.REQUEST_DATA["weather"][0]["description"].capitalize() == "Mist":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/mist_day.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Clouds":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/cloudy_day2.svg")

            elif self.TIME_STR >= self.SUNSET_TIME and self.TIME_STR < self.SUNRISE_TIME:
                if self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Clear":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/main_night.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Drizzle":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/rainy_day.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Rain":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/rainy_night.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Snow":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/snowy_night.svg")
                elif self.REQUEST_DATA["weather"][0]["description"].capitalize() == "Mist":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/mist_day.svg")
                elif self.REQUEST_DATA["weather"][0]["main"].capitalize() == "Clouds":
                    pixmap = gui.QPixmap(f"media/title_bar/weather_icons/cloudy_night.svg")

            if pixmap is not None:
                pixmap = pixmap.scaled(84, 87, core.Qt.AspectRatioMode.IgnoreAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                weather_container.LEFT_WEATHER_ICON.setPixmap(pixmap)

            weather_container.RIGHT_DATA_LABEL1.setText(self.DAY_STR.capitalize())
            
            weather_container.RIGHT_DATA_LABEL2.setText(self.DATE)
            
            weather_container.RIGHT_CLOCK_LABEL.setText(self.TIME_STR)
            
            weather_container.RIGHT_CLOCK_FRAME.setPixmap(gui.QPixmap(f"media/title_bar/clock.svg"))
            
            
            
            self.FRAME1_LABEL2.setText(self.TIME_STR)
            self.FRAME1_LABEL3.setText(self.REQUEST_DATA["weather"][0]["description"].capitalize())
            self.FRAME2_LABEL1.setText(f"{int(self.REQUEST_DATA['main']['temp']-273)}°")
            self.FRAME2_LABEL2.setText(f"Макс.:{int(self.REQUEST_DATA['main']['temp_max']-273)}°, Мін.:{int(self.REQUEST_DATA['main']['temp_min']-273)}°")
            
            for card in Cards.CARDS_LIST:
                if card.SELECTED:
                    card.setStyleSheet("background-color: transparent; border-radius: 8px;")
                    card.SELECTED = False

            self.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border-radius: 8px;")
            self.SELECTED = True
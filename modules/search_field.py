import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import json
import os
from utils import clear_layout
from .search_field_button import SearchFieldCityButton
from utils import close_drop_menu
from utils import request
from utils import scale
class SearchField(widgets.QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.ERROR = False
        self.CITY_SEARCHED_COUNTER = 0
        self.setObjectName("SEARCH_FIELD")
        self.LINE_CHOOSED = False
        self.setFixedSize(200, 22)
        self.setPlaceholderText("Пошук")
        scale.setFontSize(self,17)
        try:
            with open("json/cities.json") as file:
                data = json.load(file)
                self.counties = data["data"]
        except (FileNotFoundError, json.JSONDecodeError):
            return
        
        self.DROP_DOWN_FRAME = widgets.QFrame(parent = self.window().central_widget)
        self.DROP_DOWN_FRAME.setGeometry(scale.scale_x(918), scale.scale_y(55), scale.scale_x(261), scale.scale_y(200))
        
        self.DROP_DOWN_FRAME.setStyleSheet(f"background-color: #2c2c2c; border-radius: 10px;")
        self.DROP_DOWN_FRAME.hide()
        
        
        
        self.DROP_DOWN_SCROLL_AREA= widgets.QScrollArea(parent = self.DROP_DOWN_FRAME)
        self.DROP_DOWN_SCROLL_AREA.setFixedSize(scale.scale_x(261), scale.scale_y(200))
        self.DROP_DOWN_SCROLL_AREA.setWidgetResizable(True)
        self.DROP_DOWN_SCROLL_AREA.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.DROP_DOWN_SCROLL_AREA.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.DROP_DOWN_SCROLL_AREA.setStyleSheet("background-color: transparent; border: none;")
        
        
        self.DROP_DOWN_SCROLL_AREA_FRAME = widgets.QFrame(parent = self.DROP_DOWN_SCROLL_AREA)
        self.DROP_DOWN_SCROLL_AREA_FRAME.setStyleSheet("background-color: transparent; border-radius: 10px;")
        self.DROP_DOWN_SCROLL_AREA.setWidget(self.DROP_DOWN_SCROLL_AREA_FRAME)
        
        
        self.DROP_DOWN_LAYOUT = widgets.QVBoxLayout(self.DROP_DOWN_SCROLL_AREA_FRAME)
        self.DROP_DOWN_LAYOUT.setContentsMargins(7,5,0,5)
        self.DROP_DOWN_LAYOUT.setSpacing(0)
        self.DROP_DOWN_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
                        
        self.DROP_DOWN_SCROLL_AREA_FRAME.setLayout(self.DROP_DOWN_LAYOUT)
        
        self.setStyleSheet("background-color: transparent; border-radius: 0px; color: white; font-family: 'Roboto'; font-weight: 400; ")
        scale.setFontSize(self,17)
        self.language_widget = self.window().findChild(widgets.QFrame, "WEATHER_CONTAINER")
        self.textChanged.connect(self.text_changed)
        
        self.setAlignment(core.Qt.AlignmentFlag.AlignLeft and core.Qt.AlignmentFlag.AlignVCenter)

    def city_chosen(self, city_name: str):
        main_window = self.window()
        our_weather_container = main_window.findChild(widgets.QFrame, "WEATHER_CONTAINER")
        
        if our_weather_container:
            our_weather_container.ADD_BUTTON.show()
            our_weather_container.ADD_BUTTON_ICON.show()
            our_weather_container.ADD_BUTTON_LABEL.show()
        
        self.CITY_NAME = city_name
        
        self.textChanged.disconnect(self.text_changed)
        self.setText(city_name)
        self.textChanged.connect(self.text_changed)
        self.DROP_DOWN_FRAME.hide()

    def text_changed(self):
        main_window = self.window()
        self.DROP_DOWN_FRAME.show()
        our_weather_container = main_window.findChild(widgets.QFrame, "WEATHER_CONTAINER")
        if our_weather_container:
            our_weather_container.ADD_BUTTON.hide()
            our_weather_container.ADD_BUTTON_LABEL.hide()
            our_weather_container.ADD_BUTTON_ICON.hide()
        
        self.LINE_TEXT = self.text()
        search_frame = main_window.findChild(widgets.QFrame, "SEARCH_FRAME")
        if self.LINE_TEXT.strip():
            if search_frame:
                search_frame.clear_button.show()
            
            clear_layout(self.DROP_DOWN_LAYOUT)
            self.language = our_weather_container.LANGUAGE
            if self.language == "Українська":
                self.drop_down_label = "Результати пошуку"
            elif self.language == "English" :
                self.drop_down_label = "Search result"
            self.DROP_DOWN_LABEL = widgets.QLabel(parent = self.DROP_DOWN_FRAME, text = self.drop_down_label)
            self.DROP_DOWN_LABEL.setStyleSheet("background-color: transparent; border: none; color: rgba(255,255,255,0.5); font-family: 'Roboto'; font-weight: 400;")
            scale.setFontSize(self.DROP_DOWN_LABEL,14)
            self.DROP_DOWN_LAYOUT.addWidget(self.DROP_DOWN_LABEL)
            
            self.CITY_SEARCHED_COUNTER = 0
            if search_frame is None:
                return
           
            
            
            
            if self.LINE_TEXT.strip():  
                for country in self.counties:
                    for city in country["cities"]:
                        if city.lower().startswith(self.LINE_TEXT.lower()):
                            self.CITY_SEARCHED_COUNTER += 1
                            if self.CITY_SEARCHED_COUNTER > 15:
                                break
                            self.city_name = city                           
                            self.city_button = SearchFieldCityButton(parent=self.DROP_DOWN_SCROLL_AREA_FRAME, text=self.city_name, width = 261, height = 32)
                            self.city_button.clicked.connect(lambda clicked, name=self.city_name: self.city_chosen(name))
                            self.DROP_DOWN_LAYOUT.addWidget(self.city_button)
                        if city.lower() == self.LINE_TEXT.lower():
                            our_weather_container.ADD_BUTTON.show()
                            our_weather_container.ADD_BUTTON_ICON.show()
                            our_weather_container.ADD_BUTTON_LABEL.show()                                                
                    if self.CITY_SEARCHED_COUNTER >= 15:
                        break
        
        else:
            self.DROP_DOWN_FRAME.hide()
            if search_frame:
                search_frame.clear_button.hide()                
    def mousePressEvent(self, event):
        if event.button() == core.Qt.MouseButton.LeftButton :
            try:
                self.window().findChild(widgets.QFrame, "DROP_COUNTRY_MODAL").DROP_DOWN_FRAME.hide()
                self.window().findChild(widgets.QFrame, "DROP_CITY_MODAL").DROP_DOWN_FRAME.hide()
            except :
                pass
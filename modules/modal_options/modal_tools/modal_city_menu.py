import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import json
import os
from utils import clear_layout
from ...search_field_button import SearchFieldCityButton
from utils import close_drop_menu

class ModalCityMenu(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.CITY_NAME = None  # Инициализируем
        self.country = None  # Инициализируем
        self.CITY_TEXT = ""  # Инициализируем
        self.city_name = ""  # Инициализируем
        self.DROP_DOWN_FRAME = None
        self.setObjectName("DROP_CITY_MODAL")
        self.CHOOSED = False
        self.DROP_MENU_SHOW = False
        self.setFixedSize(239, 32)
        
        try:
            with open("json/cities.json") as file:
                data = json.load(file)
                self.countries = data["data"]
        except (FileNotFoundError, json.JSONDecodeError):
            return
        
        self.setStyleSheet("background-color: white")
        
        self.DROP_LAYOUT = widgets.QHBoxLayout()
        self.DROP_LAYOUT.setSpacing(5)
        self.DROP_LAYOUT.setContentsMargins(10, 8, 10, 8)
        self.DROP_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.DROP_LAYOUT)
        
        self.CITY_LINEEDIT = widgets.QLineEdit(parent = self)
        self.CITY_LINEEDIT.setPlaceholderText("Виберіть місто")
        self.CITY_LINEEDIT.setFixedSize(198,16)
        self.CITY_LINEEDIT.setStyleSheet("background-color: transparent;border-radius: 0px; color: #71717A; font-family: 'Roboto'; font-weight: 400; font-size: 12px;")
        self.DROP_LAYOUT.addWidget(self.CITY_LINEEDIT)
        self.CITY_LINEEDIT.setReadOnly(True)
        
        self.ARROW_BUTTON = widgets.QPushButton(parent = self, icon = gui.QIcon("media/title_bar/additional_elements/arrowdown.png"))
        self.ARROW_BUTTON.setFixedSize(16,16)
        self.ARROW_BUTTON.clicked.connect(self.arrow_clicked)
        self.DROP_LAYOUT.addWidget(self.ARROW_BUTTON)
       
        self.DROP_DOWN_FRAME = widgets.QFrame(parent = self.window())   
        self.DROP_DOWN_FRAME.setGeometry(613, 361, 239, 186)
        self.DROP_DOWN_FRAME.setStyleSheet("background-color: #676767; border-radius: 10px;")
        self.DROP_DOWN_FRAME.hide()
        
        
        self.DROP_DOWN_SCROLL_AREA= widgets.QScrollArea(parent = self.DROP_DOWN_FRAME)
        self.DROP_DOWN_SCROLL_AREA.setStyleSheet("background-color: transparent; border: none;")
        self.DROP_DOWN_SCROLL_AREA.setFixedSize(239, 186)
        self.DROP_DOWN_SCROLL_AREA.setWidgetResizable(True)
        
        self.DROP_DOWN_SCROLL_AREA.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.DROP_DOWN_SCROLL_AREA.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        
        self.DROP_DOWN_SCROLL_AREA_FRAME = widgets.QFrame(parent = self.DROP_DOWN_SCROLL_AREA)
        self.DROP_DOWN_SCROLL_AREA_FRAME.setStyleSheet("background-color: transparent; border-radius: 10px;")
                    
        self.DROP_DOWN_LAYOUT = widgets.QVBoxLayout(self.DROP_DOWN_SCROLL_AREA_FRAME)
        self.DROP_DOWN_LAYOUT.setContentsMargins(8,8,0,8)
        self.DROP_DOWN_LAYOUT.setSpacing(0)
        self.DROP_DOWN_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
        self.DROP_DOWN_SCROLL_AREA_FRAME.setLayout(self.DROP_DOWN_LAYOUT)
        self.DROP_DOWN_SCROLL_AREA.setWidget(self.DROP_DOWN_SCROLL_AREA_FRAME)
        
        self.CITY_LINEEDIT.textChanged.connect(self.text_changed)
        
    def city_chosen(self, city_name: str):
        
        self.CITY_NAME = city_name
        
        self.CITY_LINEEDIT.textChanged.disconnect(self.text_changed)
        self.CITY_LINEEDIT.setText(city_name)
        if self.DROP_DOWN_FRAME:
            self.DROP_DOWN_FRAME.hide()
            self.DROP_MENU_SHOW = False
        self.CITY_LINEEDIT.textChanged.connect(self.text_changed)
        
        
        
    def text_changed(self):
        search_field = self.window().findChild(widgets.QLineEdit, "SEARCH_FIELD")
        country_modal = self.window().findChild(widgets.QFrame, "DROP_COUNTRY_MODAL")
        
        # Безопасная проверка для search_field.DROP_DOWN_FRAME
        if (search_field and hasattr(search_field, 'DROP_DOWN_FRAME') and 
            search_field.DROP_DOWN_FRAME and isinstance(search_field.DROP_DOWN_FRAME, widgets.QFrame)):
            search_field.DROP_DOWN_FRAME.hide()
        
        self.CITY_NAME = None
        
        # Получаем выбранную страну
        if country_modal and hasattr(country_modal, 'COUNTRY_NAME'):
            self.country = country_modal.COUNTRY_NAME
        else:
            self.country = None
        
        if not self.country:
            if self.DROP_DOWN_FRAME:
                self.DROP_DOWN_FRAME.hide()
                self.DROP_MENU_SHOW = False
            return
        
        self.CITY_TEXT = self.CITY_LINEEDIT.text()
        clear_layout(self.DROP_DOWN_LAYOUT)
        
        for json_country in self.countries:
            if self.country == json_country["country"]:
                for city in json_country["cities"]:
                    if not self.CITY_TEXT.strip() or city.lower().startswith(self.CITY_TEXT.lower()):
                        self.city_name = city
                        self.city_button = SearchFieldCityButton(parent=self.DROP_DOWN_SCROLL_AREA_FRAME, text=self.city_name, width = 231, height = 22)
                        self.city_button.clicked.connect(lambda clicked, name=self.city_name: self.city_chosen(name))
                        self.DROP_DOWN_LAYOUT.addWidget(self.city_button)
                    if self.CITY_TEXT.strip() and city.lower() == self.CITY_TEXT.lower():
                        self.CITY_NAME = self.city_name
                        if self.DROP_DOWN_FRAME:
                            self.DROP_DOWN_FRAME.hide()
                            self.DROP_MENU_SHOW = False
        
        if self.DROP_DOWN_LAYOUT.count() > 0 and self.DROP_DOWN_FRAME:
            self.DROP_DOWN_FRAME.show()
            self.DROP_MENU_SHOW = True
        elif self.DROP_DOWN_FRAME:
            self.DROP_DOWN_FRAME.hide()
            self.DROP_MENU_SHOW = False


    def arrow_clicked(self):
        if not self.DROP_DOWN_FRAME:
            return
        
        if self.DROP_MENU_SHOW:
            self.DROP_DOWN_FRAME.hide()
            self.DROP_MENU_SHOW = False
            return
        
        clear_layout(self.DROP_DOWN_LAYOUT)
        try:
            country_modal = self.window().findChild(widgets.QFrame, "DROP_COUNTRY_MODAL")
            if country_modal and hasattr(country_modal, 'COUNTRY_NAME'):
                self.country = country_modal.COUNTRY_NAME
            
            if not self.country:
                return
            
            for json_country in self.countries:
                if self.country == json_country["country"]:
                    for city in json_country["cities"]:
                        self.city_name = city
                        self.city_button = SearchFieldCityButton(parent=self.DROP_DOWN_SCROLL_AREA_FRAME, text=self.city_name, width = 231, height = 22)
                        self.city_button.clicked.connect(lambda clicked, name=self.city_name: self.city_chosen(name))
                        self.DROP_DOWN_LAYOUT.addWidget(self.city_button)
            if self.DROP_DOWN_LAYOUT.count() > 0:
                self.DROP_DOWN_FRAME.show()
                self.DROP_MENU_SHOW = True
        except:
            pass    
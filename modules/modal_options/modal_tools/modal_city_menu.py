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
        self.DROP_DOWN_FRAME = None
        self.setObjectName("DROP_CITY_MODAL")
        self.CHOOSED = False
        
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
        
        self.ARROW_LABLE = widgets.QLabel(parent = self)
        self.ARROW_LABLE.setFixedSize(16,16)
        arrow_pixmap = gui.QPixmap(f"media/title_bar/additional_elements/arrowdown.png")
        if not arrow_pixmap.isNull():
            scaled_pixmap = arrow_pixmap.scaled(16, 16, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
            self.ARROW_LABLE.setPixmap(scaled_pixmap)
        
        self.DROP_LAYOUT.addWidget(self.ARROW_LABLE)
       
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
        self.DROP_DOWN_FRAME.hide()
        self.CITY_LINEEDIT.textChanged.connect(self.text_changed)
        
        
        
    def text_changed(self):
        self.window().findChild(widgets.QLineEdit, "SEARCH_FIELD").DROP_DOWN_FRAME.hide()
        self.CITY_NAME = None
        if self.window().findChild(widgets.QFrame,"DROP_COUNTRY_MODAL").COUNTRY_LINEEDIT.text() != "Виберіть країну" :
            self.CITY_TEXT = self.CITY_LINEEDIT.text()
            
            
            clear_layout(self.DROP_DOWN_LAYOUT)

            
            
            if self.CITY_TEXT.strip():
                for json_country in self.countries:
                    if self.country == json_country["country"]:
                        for city in json_country["cities"]:
                            if city.lower().startswith(self.CITY_TEXT.lower()):
                                self.city_name = city
                                self.city_button = SearchFieldCityButton(parent=self.DROP_DOWN_SCROLL_AREA_FRAME, text=self.city_name, width = 231, height = 22)
                                self.city_button.clicked.connect(lambda clicked, name=self.city_name: self.city_chosen(name))
                                self.DROP_DOWN_LAYOUT.addWidget(self.city_button)
                            if city.lower() == self.CITY_TEXT.lower():
                                self.CITY_NAME = self.city_name
                                self.DROP_DOWN_FRAME.hide()
                self.DROP_DOWN_FRAME.show()                
        else:  
            self.DROP_DOWN_FRAME.hide()      

    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton and self.window().findChild(widgets.QFrame,"DROP_COUNTRY_MODAL").COUNTRY_CHOOSED:
            try:
                self.country = self.window().findChild(widgets.QFrame,"DROP_COUNTRY_MODAL").COUNTRY_NAME
            except:
                pass
            self.CITY_LINEEDIT.setReadOnly(False)
            self.CITY_LINEEDIT.setFocus()
            for json_country in self.countries:
                    if self.country == json_country["country"]:
                        for city in json_country["cities"]:
                            self.city_name = city
                            self.city_button = SearchFieldCityButton(parent=self.DROP_DOWN_SCROLL_AREA_FRAME, text=self.city_name, width = 231, height = 22) 
                            self.city_button.clicked.connect(lambda clicked, name=self.city_name: self.city_chosen(name))
                            self.DROP_DOWN_LAYOUT.addWidget(self.city_button)
            self.DROP_DOWN_FRAME.show()
            
                            
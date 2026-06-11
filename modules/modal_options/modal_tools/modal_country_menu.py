import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import json
import os
from utils import clear_layout
from ...search_field_button import SearchFieldCityButton
from utils import close_drop_menu

class ModalCountryMenu(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.COUNTRY_LABEL = None
        self.setObjectName("DROP_COUNTRY_MODAL")
        self.CHOOSED = False
        self.COUNTRY_CHOOSED = False
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
        
        self.COUNTRY_LINEEDIT = widgets.QLineEdit(parent = self)
        self.COUNTRY_LINEEDIT.setPlaceholderText("Виберіть країну")
        self.COUNTRY_LINEEDIT.setFixedSize(198,16)
        self.COUNTRY_LINEEDIT.setStyleSheet("background-color: transparent;border-radius: 0px; color: #71717A; font-family: 'Roboto'; font-weight: 400; font-size: 12px;")
        self.DROP_LAYOUT.addWidget(self.COUNTRY_LINEEDIT)
        
        self.ARROW_LABLE = widgets.QLabel(parent = self)
        self.ARROW_LABLE.setFixedSize(16,16)
        arrow_pixmap = gui.QPixmap(f"media/title_bar/additional_elements/arrowdown.png")
        if not arrow_pixmap.isNull():
            scaled_pixmap = arrow_pixmap.scaled(16, 16, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
            self.ARROW_LABLE.setPixmap(scaled_pixmap)
        
        self.DROP_LAYOUT.addWidget(self.ARROW_LABLE)
        
        self.DROP_DOWN_FRAME = widgets.QFrame(parent = self.window())   
        self.DROP_DOWN_FRAME.setGeometry(613, 291, 239, 186)
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
        
        self.COUNTRY_LINEEDIT.textChanged.connect(self.text_changed)
        
    def country_chosen(self, country_name: str):
        self.window().findChild(widgets.QFrame,"DROP_CITY_MODAL").CITY_LINEEDIT.setText("")
        
        self.COUNTRY_LINEEDIT.textChanged.disconnect(self.text_changed)
        self.COUNTRY_LINEEDIT.setText(country_name)
        self.COUNTRY_LINEEDIT.textChanged.connect(self.text_changed)
        
        self.COUNTRY_NAME = country_name
        self.DROP_DOWN_FRAME.hide()
        self.COUNTRY_CHOOSED = True
        
    def text_changed(self):
        self.window().findChild(widgets.QFrame,"DROP_CITY_MODAL").DROP_DOWN_FRAME.hide()
        self.window().findChild(widgets.QLineEdit, "SEARCH_FIELD").DROP_DOWN_FRAME.hide()
        self.DROP_DOWN_FRAME.show()
        self.COUNTRY_CHOOSED = False
        
        
        self.COUNTRY_TEXT = self.COUNTRY_LINEEDIT.text()
        if self.COUNTRY_TEXT.strip():
            clear_layout(self.DROP_DOWN_LAYOUT)
            try:
                with open("json/cities.json") as file:
                    data = json.load(file)
                    self.countries = data["data"]
            except (FileNotFoundError, json.JSONDecodeError):
                return
            
            if self.COUNTRY_TEXT.strip():
                for country in self.countries:
                    self.country_name = country["country"]
                    if self.country_name.lower().startswith(self.COUNTRY_TEXT.lower()):
                        self.country_button = SearchFieldCityButton(parent=self.DROP_DOWN_SCROLL_AREA_FRAME, text= self.country_name, width = 231, height = 22)
                        self.country_button.clicked.connect(lambda clicked, name=self.country_name: self.country_chosen(name))
                        self.DROP_DOWN_LAYOUT.addWidget(self.country_button)
    
                    if self.country_name.lower() == self.COUNTRY_TEXT.lower():
                        self.COUNTRY_NAME = self.country_name
                        self.COUNTRY_CHOOSED = True
                
        else:
            self.DROP_DOWN_FRAME.hide()
    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton:
            for country in self.countries:
                    self.country_name = country["country"]
                    self.country_button = SearchFieldCityButton(parent=self.DROP_DOWN_SCROLL_AREA_FRAME, text=self.country_name, width = 231, height = 22) 
                    self.country_button.clicked.connect(lambda clicked, name=self.country_name: self.country_chosen(name))
                    self.DROP_DOWN_LAYOUT.addWidget(self.country_button)
            self.DROP_DOWN_FRAME.show()
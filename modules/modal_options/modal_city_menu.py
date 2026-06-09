import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import json
import os
from utils import clear_layout
from ..search_field_button import SearchFieldCityButton

class ModalCityMenu(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.setObjectName("DROP_CITY_MODAL")
        self.CHOOSED = False
        self.setFixedSize(239, 32)
        
        self.setStyleSheet("background-color: white")
        
        self.DROP_LAYOUT = widgets.QHBoxLayout()
        self.DROP_LAYOUT.setSpacing(5)
        self.DROP_LAYOUT.setContentsMargins(10, 8, 10, 8)
        self.DROP_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.DROP_LAYOUT)
        
        self.CITY_LABEL = widgets.QLabel(parent = self, text = "Виберіть місто")
        self.CITY_LABEL.setFixedSize(198,16)
        self.CITY_LABEL.setStyleSheet("background-color: transparent;border-radius: 0px; color: #71717A; font-family: 'Roboto'; font-weight: 400; font-size: 12px;")
        self.DROP_LAYOUT.addWidget(self.CITY_LABEL)
        
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
        self.DROP_DOWN_LAYOUT.setSpacing(6)
        self.DROP_DOWN_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
        self.DROP_DOWN_SCROLL_AREA_FRAME.setLayout(self.DROP_DOWN_LAYOUT)
        self.DROP_DOWN_SCROLL_AREA.setWidget(self.DROP_DOWN_SCROLL_AREA_FRAME)
        
        

    def city_chosen(self, city_name: str):
        main_window = self.window()
   
        self.CITY_LABEL.setText(city_name)
        self.DROP_DOWN_FRAME.hide()

    def menu_pressed(self):
        main_window = self.window()
        self.DROP_DOWN_FRAME.show()
    
        clear_layout(self.DROP_DOWN_LAYOUT)
       
        
        
        try:
            with open("json/cities.json") as file:
                data = json.load(file)
                countries = data["data"]
        except (FileNotFoundError, json.JSONDecodeError):
            return
        
        for country in countries:
            for city in country["cities"]:
                city_name = city
                city_button = SearchFieldCityButton(parent=self.DROP_DOWN_SCROLL_AREA_FRAME, text=city_name, width = 231, height = 16)
                city_button.clicked.connect(lambda clicked, name=city_name: self.city_chosen(name))
                self.DROP_DOWN_LAYOUT.addWidget(city_button)
                
        self.DROP_DOWN_FRAME.hide()             
    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton:
            self.menu_pressed()
            self.DROP_DOWN_FRAME.show()
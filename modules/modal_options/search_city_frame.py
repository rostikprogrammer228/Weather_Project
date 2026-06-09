import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
import PyQt6.QtWebEngineWidgets as WebEngine
import folium 
import io

from .modal_city_menu import ModalCityMenu

class SearchCity(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setFixedSize(158,35)
        self.setStyleSheet("background-color: transparent")
        self.LAYOUT = widgets.QVBoxLayout()
        self.LAYOUT.setContentsMargins(8, 8, 0, 8)
        self.setLayout(self.LAYOUT)
        
        self.LABEL = widgets.QLabel(text = "Пошук міста")
        self.LABEL.setFixedWidth(150)
        self.LABEL.setStyleSheet("color: white; font-size: 16px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        self.LAYOUT.addWidget(self.LABEL)
    
    def create_frame(self):
        
        modal_window = self.window().findChild(widgets.QWidget, "MODAL_WINDOW")
        
        self.SETTINGS_CONTEINER_RIGHT = widgets.QFrame(parent = modal_window.SETTINGS_CONTEINER)
        self.SETTINGS_CONTEINER_RIGHT.setStyleSheet("background-color: transparent")
        self.SETTINGS_CONTEINER_RIGHT.setFixedSize(544, 578)
        modal_window.SETTINGS_CONTEINER_LAYOUT.addWidget(self.SETTINGS_CONTEINER_RIGHT)
        
        self.SETTINGS_CONTEINER_RIGHT_LAYOUT = widgets.QVBoxLayout()
        self.SETTINGS_CONTEINER_RIGHT_LAYOUT.setContentsMargins(0,0,0,56)
        self.SETTINGS_CONTEINER_RIGHT_LAYOUT.setSpacing(24)
        self.SETTINGS_CONTEINER_RIGHT.setLayout(self.SETTINGS_CONTEINER_RIGHT_LAYOUT)
        self.SETTINGS_CONTEINER_RIGHT_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)  
        
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME = widgets.QFrame(parent = self.SETTINGS_CONTEINER_RIGHT)
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME.setStyleSheet("background-color: rgba(0,0,0,0.2)")
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME.setFixedSize(544, 301)
        self.SETTINGS_CONTEINER_RIGHT_LAYOUT.addWidget(self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME)
        
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME_LAYOUT.setSpacing(0)
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignBottom)  
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME.setLayout(self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME_LAYOUT)
        
        
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME = widgets.QFrame(parent = self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME)
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME.setStyleSheet("background-color: transparent")
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME.setFixedSize(239, 301)
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME_LAYOUT.addWidget(self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME)
        
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME_LAYOUT.setSpacing(24)
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME.setLayout(self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME_LAYOUT)
        
        
        self.SEARCH_CITY_LABEL = widgets.QLabel(parent = self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME,text = "Пошук міста")
        self.SEARCH_CITY_LABEL.setFixedSize(239,21)
        self.SEARCH_CITY_LABEL.setStyleSheet("color: white; font-size: 18px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 400;")
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME_LAYOUT.addWidget(self.SEARCH_CITY_LABEL,alignment= core.Qt.AlignmentFlag.AlignTop)
        
        
        self.SEARCH_CHOOSING = widgets.QFrame(parent = self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME)
        self.SEARCH_CHOOSING.setFixedSize(239, 194)
        self.SEARCH_CHOOSING.setStyleSheet("background-color: transparent")
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME_LAYOUT.addWidget(self.SEARCH_CHOOSING)
        
        self.SEARCH_CHOOSING_LAYOUT = widgets.QVBoxLayout()
        self.SEARCH_CHOOSING.setLayout(self.SEARCH_CHOOSING_LAYOUT)
        self.SEARCH_CHOOSING_LAYOUT.setContentsMargins(0,0,0,0)
        self.SEARCH_CHOOSING_LAYOUT.setSpacing(16)
        
       
        
        self.COUNTRY_CHOOSING_FRAME = widgets.QFrame(parent = self.SEARCH_CHOOSING)
        self.COUNTRY_CHOOSING_FRAME.setFixedSize(239,54)
        self.COUNTRY_CHOOSING_FRAME.setStyleSheet("background-color: transparent")
        self.SEARCH_CHOOSING_LAYOUT.addWidget(self.COUNTRY_CHOOSING_FRAME)
        
        self.COUNTRY_CHOOSING_LAYOUT = widgets.QVBoxLayout()
        self.COUNTRY_CHOOSING_LAYOUT.setContentsMargins(0,0,0,0)
        self.COUNTRY_CHOOSING_LAYOUT.setSpacing(8)
        self.COUNTRY_CHOOSING_FRAME.setLayout(self.COUNTRY_CHOOSING_LAYOUT)
        
        
        self.COUNTRY_LABEL = widgets.QLabel(parent = self.SEARCH_CHOOSING,text = "Країна" )
        self.COUNTRY_LABEL.setStyleSheet("color: white; font-size: 14px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        self.COUNTRY_LABEL.setFixedSize(239,14)
        self.COUNTRY_CHOOSING_LAYOUT.addWidget(self.COUNTRY_LABEL)
       
        # country_drop_down_menu
        
        self.CITY_CHOOSING_FRAME = widgets.QFrame(parent = self.SEARCH_CHOOSING)
        self.CITY_CHOOSING_FRAME.setFixedSize(239,54)
        self.CITY_CHOOSING_FRAME.setStyleSheet("background-color: transparent")
        self.SEARCH_CHOOSING_LAYOUT.addWidget(self.CITY_CHOOSING_FRAME)
        
        self.CITY_CHOOSING_LAYOUT = widgets.QVBoxLayout()
        self.CITY_CHOOSING_LAYOUT.setContentsMargins(0,0,0,0)
        self.CITY_CHOOSING_LAYOUT.setSpacing(8)
        self.CITY_CHOOSING_FRAME.setLayout(self.CITY_CHOOSING_LAYOUT)
        
        self.CITY_LABEL = widgets.QLabel(parent = self.SEARCH_CHOOSING,text = "Місто" )
        self.CITY_LABEL.setStyleSheet("color: white; font-size: 14px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        self.CITY_LABEL.setFixedSize(239,14)
        self.CITY_CHOOSING_LAYOUT.addWidget(self.CITY_LABEL)
        
        city_drop_down_menu = ModalCityMenu(self.CITY_CHOOSING_FRAME)
        self.CITY_CHOOSING_LAYOUT.addWidget(city_drop_down_menu)
        
        
        self.COORDINATE_FRAME = widgets.QFrame(parent = self.SEARCH_CHOOSING)
        self.COORDINATE_FRAME.setFixedSize(239,54)
        self.COORDINATE_FRAME.setStyleSheet("background-color: transparent")
        self.SEARCH_CHOOSING_LAYOUT.addWidget(self.COORDINATE_FRAME)
        
        self.COORDINATE_LAYOUT = widgets.QVBoxLayout()
        self.COORDINATE_LAYOUT.setContentsMargins(0,0,0,0)
        self.COORDINATE_LAYOUT.setSpacing(8)
        self.COORDINATE_FRAME.setLayout(self.COORDINATE_LAYOUT)
        
        self.COORDINATE_LABEL1 = widgets.QLabel(parent = self.COORDINATE_FRAME, text = "Координати")
        self.COORDINATE_LABEL1.setStyleSheet("color: white; font-size: 14px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        self.COORDINATE_LABEL1.setFixedSize(239, 14)
        self.COORDINATE_LAYOUT.addWidget(self.COORDINATE_LABEL1)
        
        self.COORDINATE_LABEL2_FRAME = widgets.QFrame(self.COORDINATE_FRAME)
        self.COORDINATE_LABEL2_FRAME.setFixedSize(239, 32)
        self.COORDINATE_LABEL2_FRAME.setStyleSheet("background-color: white; border-radius: 4px;")
        self.COORDINATE_LAYOUT.addWidget(self.COORDINATE_LABEL2_FRAME)
        
        self.COORDINATE_LABEL2_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.COORDINATE_LABEL2_FRAME_LAYOUT.setContentsMargins(10,8,10,8)   
        self.COORDINATE_LABEL2_FRAME_LAYOUT.setSpacing(0)
        self.COORDINATE_LABEL2_FRAME.setLayout(self.COORDINATE_LABEL2_FRAME_LAYOUT)
        
        self.COORDINATE_LABEL2 = widgets.QLabel(parent = self.COORDINATE_FRAME, text = " (WGS 84,UTM,MGRS)")
        self.COORDINATE_LABEL2.setStyleSheet("color: #71717A; font-size: 12px;")
        self.COORDINATE_LABEL2.setFixedSize(219, 16)
        self.COORDINATE_LABEL2_FRAME_LAYOUT.addWidget(self.COORDINATE_LABEL2)
        
        
        
        
        self.SAVE_BUTTON = widgets.QPushButton(self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME, text = "Зберегти")
        self.SAVE_BUTTON.setFixedSize(105, 38)
        self.SAVE_BUTTON.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px")
        self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME_LAYOUT.addWidget(self.SAVE_BUTTON)
        
        self.MAP_CONTAINER_FRAME = widgets.QFrame(parent = self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME)
        self.MAP_CONTAINER_FRAME.setFixedSize(305, 301)
        self.MAP_CONTAINER_FRAME.setStyleSheet("background-color: transparent;")
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME_LAYOUT.addWidget(self.MAP_CONTAINER_FRAME, core.Qt.AlignmentFlag.AlignBottom)
        
        self.MAP_CONTAINER_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.MAP_CONTAINER_FRAME_LAYOUT.setContentsMargins(16, 45,0, 0)
        self.MAP_CONTAINER_FRAME_LAYOUT.setSpacing(0)
        self.MAP_CONTAINER_FRAME.setLayout(self.MAP_CONTAINER_FRAME_LAYOUT)
        
        self.MAP_FRAME = widgets.QFrame(self.MAP_CONTAINER_FRAME)
        self.MAP_FRAME.setFixedSize(289,256)
        self.MAP_CONTAINER_FRAME_LAYOUT.addWidget( self.MAP_FRAME)
        
        data = io.BytesIO()
        map = folium.Map(location = (50, 50))
        map.save(data, close_file = False)
        
        web_engine_view = WebEngine.QWebEngineView(parent = self.MAP_FRAME)
        web_engine_view.setFixedSize(289,256)
        
        html = data.getvalue().decode()
        web_engine_view.setHtml(html)
        
        
        
        
        
        
        
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME = widgets.QFrame(parent = self.SETTINGS_CONTEINER_RIGHT)
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME.setStyleSheet("background-color: transparent")
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME.setFixedSize(544, 197)
        self.SETTINGS_CONTEINER_RIGHT_LAYOUT.addWidget(self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME)
        
        
        
        
        
        
        
        
        
    def mousePressEvent(self, event):
        if event.button() == core.Qt.MouseButton.LeftButton:
            self.create_frame()
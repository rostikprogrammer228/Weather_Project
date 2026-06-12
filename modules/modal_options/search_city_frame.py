import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
import PyQt6.QtWebEngineWidgets as WebEngine
import folium 
import io
from utils import clear_layout

from .modal_tools.modal_city_menu import ModalCityMenu
from .modal_tools.modal_country_menu import ModalCountryMenu
from .modal_tools.city_lables import CityListLable

class SearchCity(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.CHOOSED = False
        self.MODAL_WINDOW = self.window().findChild(widgets.QWidget,"MODAL_WINDOW")
        self.WEATHER_CONTAINER = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER")
        self.CARD = self.window().findChild(widgets.QFrame, "CARD")
        self.setObjectName("SEARCHCITY")
        
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
        self.CHOOSED = True
        self.SETTINGS_LAYOUT = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT
        self.SETTINGS_FRAME = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT
        
        self.SETTINGS_LAYOUT.setContentsMargins(0,0,0,56)
        self.SETTINGS_LAYOUT.setSpacing(24)
        
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME = widgets.QFrame(parent = self.SETTINGS_FRAME)
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME.setStyleSheet("background-color: transparent")
        self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME.setFixedSize(544, 301)
        self.SETTINGS_LAYOUT.addWidget(self.SETTINGS_CONTEINER_RIGHT_TOP_FRAME)
        
        
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
        self.COUNTRY_CHOOSING_LAYOUT.setSpacing(4)
        self.COUNTRY_CHOOSING_FRAME.setLayout(self.COUNTRY_CHOOSING_LAYOUT)
        
        
        self.COUNTRY_LABEL = widgets.QLabel(parent = self.SEARCH_CHOOSING,text = "Країна" )
        self.COUNTRY_LABEL.setStyleSheet("color: white; font-size: 14px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        self.COUNTRY_LABEL.setFixedSize(239,18)
        self.COUNTRY_CHOOSING_LAYOUT.addWidget(self.COUNTRY_LABEL)
       
        # country_drop_down_menu
         
        self.country_drop_down_menu = ModalCountryMenu(self.COUNTRY_CHOOSING_FRAME)
        self.COUNTRY_CHOOSING_LAYOUT.addWidget(self.country_drop_down_menu)
        
        
        self.CITY_CHOOSING_FRAME = widgets.QFrame(parent = self.SEARCH_CHOOSING)
        self.CITY_CHOOSING_FRAME.setFixedSize(239,54)
        self.CITY_CHOOSING_FRAME.setStyleSheet("background-color: transparent")
        self.SEARCH_CHOOSING_LAYOUT.addWidget(self.CITY_CHOOSING_FRAME)
        
        self.CITY_CHOOSING_LAYOUT = widgets.QVBoxLayout()
        self.CITY_CHOOSING_LAYOUT.setContentsMargins(0,0,0,0)
        self.CITY_CHOOSING_LAYOUT.setSpacing(4)
        self.CITY_CHOOSING_FRAME.setLayout(self.CITY_CHOOSING_LAYOUT)
        
        self.CITY_LABEL = widgets.QLabel(parent = self.SEARCH_CHOOSING,text = "Місто" )
        self.CITY_LABEL.setStyleSheet("color: white; font-size: 14px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        self.CITY_LABEL.setFixedSize(239,18)
        self.CITY_CHOOSING_LAYOUT.addWidget(self.CITY_LABEL)
        
        self.city_drop_down_menu = ModalCityMenu(self.CITY_CHOOSING_FRAME)
        self.CITY_CHOOSING_LAYOUT.addWidget(self.city_drop_down_menu)
        
        
        self.COORDINATE_FRAME = widgets.QFrame(parent = self.SEARCH_CHOOSING)
        self.COORDINATE_FRAME.setFixedSize(239,54)
        self.COORDINATE_FRAME.setStyleSheet("background-color: transparent")
        self.SEARCH_CHOOSING_LAYOUT.addWidget(self.COORDINATE_FRAME)
        
        self.COORDINATE_LAYOUT = widgets.QVBoxLayout()
        self.COORDINATE_LAYOUT.setContentsMargins(0,0,0,0)
        self.COORDINATE_LAYOUT.setSpacing(4)
        self.COORDINATE_FRAME.setLayout(self.COORDINATE_LAYOUT)
        
        self.COORDINATE_LABEL1 = widgets.QLabel(parent = self.COORDINATE_FRAME, text = "Координати")
        self.COORDINATE_LABEL1.setStyleSheet("color: white; font-size: 14px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        self.COORDINATE_LABEL1.setFixedSize(239, 18)
        self.COORDINATE_LAYOUT.addWidget(self.COORDINATE_LABEL1)
        
        self.COORDINATE_LABEL2_FRAME = widgets.QFrame(self.COORDINATE_FRAME)
        self.COORDINATE_LABEL2_FRAME.setFixedSize(239, 32)
        self.COORDINATE_LABEL2_FRAME.setStyleSheet("background-color: white; border-radius: 4px;")
        self.COORDINATE_LAYOUT.addWidget(self.COORDINATE_LABEL2_FRAME)
        
        self.COORDINATE_LABEL2_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.COORDINATE_LABEL2_FRAME_LAYOUT.setContentsMargins(10,8,10,8)   
        self.COORDINATE_LABEL2_FRAME_LAYOUT.setSpacing(0)
        self.COORDINATE_LABEL2_FRAME.setLayout(self.COORDINATE_LABEL2_FRAME_LAYOUT)
        
        self.COORDINATE_LABEL2 = widgets.QLabel(parent = self.COORDINATE_FRAME, text = "(WGS 84,UTM,MGRS)")
        self.COORDINATE_LABEL2.setStyleSheet("color: #71717A; font-size: 12px;")
        self.COORDINATE_LABEL2.setFixedSize(219, 16)
        self.COORDINATE_LABEL2_FRAME_LAYOUT.addWidget(self.COORDINATE_LABEL2)
        
        
        
      
        self.SAVE_BUTTON = widgets.QPushButton(self.SETTINGS_CONTEINER_RIGHT_TOP_CHOOSE_FRAME, text = "Зберегти")
        self.SAVE_BUTTON.clicked.connect(lambda clicked: self.WEATHER_CONTAINER.add_city_card(True))
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
        
        self.MAP_WEB_VIEW = WebEngine.QWebEngineView(parent = self.MAP_FRAME)
        self.MAP_WEB_VIEW.setFixedSize(289,256)
        self.update_map_coordinates(
            0,0
        )
        
        
        
        
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME = widgets.QFrame(parent = self.SETTINGS_FRAME)
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME.setStyleSheet("background-color: transparent;")
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME.setFixedSize(544, 197)
        self.SETTINGS_LAYOUT.addWidget(self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME)
        
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME_LAYOUT.setSpacing(16)
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME.setLayout(self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME_LAYOUT)
        
        self.BOTTOM_FRAME_LABEL = widgets.QLabel(text = "Додані міста")
        self.BOTTOM_FRAME_LABEL.setFixedSize(544, 21)
        self.BOTTOM_FRAME_LABEL.setStyleSheet("color: white; font-size: 18px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 400;")
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME_LAYOUT.addWidget(self.BOTTOM_FRAME_LABEL)
        
        self.CITY_LIST = widgets.QFrame(parent = self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME)
        self.CITY_LIST.setFixedSize(544, 160)
        self.CITY_LIST.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 8px;")
        self.SETTINGS_CONTEINER_RIGHT_BOTTOM_FRAME_LAYOUT.addWidget(self.CITY_LIST)
        
        self.CITY_LIST_LAYOUT = widgets.QHBoxLayout()
        self.CITY_LIST_LAYOUT.setContentsMargins(16, 16, 16, 16)
        self.CITY_LIST.setLayout(self.CITY_LIST_LAYOUT)
        
        self.CITY_LIST_SCROLL_PARENT = widgets.QFrame(self.CITY_LIST)
        self.CITY_LIST_SCROLL_PARENT.setFixedSize(512, 128)
        self.CITY_LIST_SCROLL_PARENT.setStyleSheet("background-color: transparent; border: none;")
        self.CITY_LIST_LAYOUT.addWidget(self.CITY_LIST_SCROLL_PARENT)
        
        self.CITY_LIST_SCROLL_AREA = widgets.QScrollArea(parent = self.CITY_LIST_SCROLL_PARENT)
        self.CITY_LIST_SCROLL_AREA.setStyleSheet("background-color: transparent; border: none;")
        self.CITY_LIST_SCROLL_AREA.setFixedSize(512, 128)
        self.CITY_LIST_SCROLL_AREA.setWidgetResizable(True)
        
        self.CITY_LIST_SCROLL_AREA.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CITY_LIST_SCROLL_AREA.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        
        self.CITY_LIST_SCROLL_AREA_FRAME = widgets.QFrame(parent = self.CITY_LIST_SCROLL_AREA)
        self.CITY_LIST_SCROLL_AREA_FRAME.setStyleSheet("background-color: transparent; border-radius: 8px;")
        self.CITY_LIST_SCROLL_AREA.setWidget(self.CITY_LIST_SCROLL_AREA_FRAME)
        
        self.CITY_LIST_SCROLL_AREA_FRAME_LAYOUT = widgets.QVBoxLayout(self.CITY_LIST_SCROLL_AREA_FRAME)
        self.CITY_LIST_SCROLL_AREA_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.CITY_LIST_SCROLL_AREA_FRAME_LAYOUT.setSpacing(0)
        self.CITY_LIST_SCROLL_AREA_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
        self.CITY_LIST_SCROLL_AREA_FRAME.setLayout(self.CITY_LIST_SCROLL_AREA_FRAME_LAYOUT)

        # Заполняем список городов из сохранённой коллекции
        for setting_card in self.WEATHER_CONTAINER.LIST_OF_SETTINGS_CARDS:
            CityListLable(parent=self.CITY_LIST_SCROLL_AREA_FRAME, city_name=setting_card)
        
        
        
    def update_map_coordinates(self, lat, lon):
        try:
            data = io.BytesIO()
            folium_map = folium.Map(location=(lat, lon))
            folium_map.save(data, close_file=False)
            html = data.getvalue().decode()
            if hasattr(self, 'MAP_WEB_VIEW'):
                self.MAP_WEB_VIEW.setHtml(html)
            self.COORDINATE_LABEL2.setText(f"{lat:.4f}, {lon:.4f}")
        except Exception as e:
            print("Map update failed:", e)

    def mousePressEvent(self, event):
        self.list_of_options_frames = self.MODAL_WINDOW.LIST_OF_OPTIONS_FRAMES
        if event.button() == core.Qt.MouseButton.LeftButton and self.CHOOSED == False:
            # Сначала обновляем статус других фреймов
            for option in self.list_of_options_frames:
                if option.CHOOSED:
                    option.setStyleSheet("background-color: transparent; border-radius: 0px")
                    option.CHOOSED = False
            
            # Потом очищаем layout
            clear_layout(self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT)
            # И создаем новый фрейм
            self.create_frame()
            self.CHOOSED = True
            self.setStyleSheet("background-color : rgba(0,0,0,0.2); border-radius : 4px")       
        
 
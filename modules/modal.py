import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
import PyQt6.QtWebEngineWidgets as WebEngine
import folium 
import io
from .modal_options.search_city_frame import SearchCity
from .modal_options.app_size_frame import AppSize
from .modal_options.app_language_frame import AppLanguage
from .modal_options.app_icons_frame import AppIcons

class ModalWindow(widgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.hide()
        
        self.setObjectName("MODAL_WINDOW")
        
        # Получаем главное окно (объект)
        main_window = self.window()
        
        
        self.setGeometry(391, 106,790, 688)
        self.setAttribute(core.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgb(54, 54, 54); border-radius: 10px;")

        self.MODAL_LAYOUT = widgets.QVBoxLayout()
        self.MODAL_LAYOUT.setContentsMargins(24,24,24,24)
        self.MODAL_LAYOUT.setSpacing(34)
        self.MODAL_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.MODAL_LAYOUT)
        
        self.HEADER_FRAME = widgets.QFrame(parent = self)
        self.HEADER_FRAME.setFixedSize(742, 28)
        self.HEADER_FRAME.setStyleSheet("background-color: transparent")
        self.MODAL_LAYOUT.addWidget(self.HEADER_FRAME)
        
        self.HEADER_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.HEADER_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.HEADER_FRAME_LAYOUT.setSpacing(550)
        self.HEADER_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.HEADER_FRAME.setLayout(self.HEADER_FRAME_LAYOUT)
        
        self.HEADER_FRAME_LABEL = widgets.QLabel("Налаштування", parent = self.HEADER_FRAME)   
        self.HEADER_FRAME_LABEL.setStyleSheet("color: white; font-size: 24px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.HEADER_FRAME_LABEL.setFixedSize(168,28)

        self.HEADER_FRAME_LAYOUT.addWidget(self.HEADER_FRAME_LABEL, alignment = core.Qt.AlignmentFlag.AlignRight)
        
        self.CLOSE_BUTTON = widgets.QPushButton(parent = self.HEADER_FRAME)
        self.CLOSE_BUTTON.setStyleSheet("background-color: transparent")
        self.CLOSE_BUTTON.setFixedSize(24, 24)
        self.CLOSE_ICON = gui.QIcon("media/title_bar/close.png")
        self.CLOSE_BUTTON.setIcon(self.CLOSE_ICON)
        
        self.CLOSE_BUTTON.clicked.connect(self.hide_function)
        self.HEADER_FRAME_LAYOUT.addWidget(self.CLOSE_BUTTON, alignment = core.Qt.AlignmentFlag.AlignLeft)
        
        
        
        self.SETTINGS_CONTEINER = widgets.QFrame(parent = self)
        self.SETTINGS_CONTEINER.setStyleSheet("background-color: transparent")
        self.SETTINGS_CONTEINER.setFixedSize(742, 578)
        self.MODAL_LAYOUT.addWidget(self.SETTINGS_CONTEINER)
        
        self.SETTINGS_CONTEINER_LAYOUT = widgets.QHBoxLayout()
        self.SETTINGS_CONTEINER_LAYOUT.setContentsMargins(0,0,0,0)
        self.SETTINGS_CONTEINER_LAYOUT.setSpacing(24)
        self.SETTINGS_CONTEINER.setLayout(self.SETTINGS_CONTEINER_LAYOUT)
        
        self.SETTINGS_CONTEINER_LEFT = widgets.QFrame(parent = self.SETTINGS_CONTEINER)
        self.SETTINGS_CONTEINER_LEFT.setStyleSheet("background-color: transparent; border-radius:0; border-right: 1px solid rgba(255,255,255,0.2)")
        self.SETTINGS_CONTEINER_LEFT.setFixedSize(174, 578)
        self.SETTINGS_CONTEINER_LAYOUT.addWidget(self.SETTINGS_CONTEINER_LEFT)
        
        self.SETTINGS_CONTEINER_LEFT_LAYOUT = widgets.QVBoxLayout()
        self.SETTINGS_CONTEINER_LEFT_LAYOUT.setContentsMargins(0,0,16,438)
        self.SETTINGS_CONTEINER_LEFT_LAYOUT.setSpacing(0)
        self.SETTINGS_CONTEINER_LEFT_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.SETTINGS_CONTEINER_LEFT.setLayout(self.SETTINGS_CONTEINER_LEFT_LAYOUT)
        
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME = widgets.QFrame(parent = self.SETTINGS_CONTEINER_LEFT)
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME.setFixedSize(158,140)
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME.setStyleSheet("background-color: transparent; border: none")
        self.SETTINGS_CONTEINER_LEFT_LAYOUT.addWidget(self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME)
        
        self.SEARCH_CITY_FRAME = SearchCity(parent = self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME)
        self.APP_SIZE_FRAME = AppSize(parent = self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME)
        self.APP_LANGUAGE_FRAME = AppLanguage(parent = self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME)
        self.APP_ICONS_FRAME = AppIcons(parent = self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME)
        
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT = widgets.QVBoxLayout()
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT.setContentsMargins(0,0,0,0)
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT.setSpacing(0)
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME.setLayout(self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT)
        
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT.addWidget(self.SEARCH_CITY_FRAME)
        self.SEARCH_CITY_FRAME.create_frame()
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT.addWidget(self.APP_SIZE_FRAME)
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT.addWidget(self.APP_LANGUAGE_FRAME)
        self.SETTINGS_CONTEINER_LEFT_OPTIONS_LAYOUT.addWidget(self.APP_ICONS_FRAME)
    def hide_function(self) :
        self.hide()
        self.window().findChild(widgets.QFrame,"DROP_CITY_MODAL").DROP_DOWN_FRAME.hide()
       
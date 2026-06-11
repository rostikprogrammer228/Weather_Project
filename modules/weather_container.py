import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
from utils import request,json_write, close_drop_menu
from .horizontal_scroll import Horizontal_Scroll
from .search_frame import SearchFrame
from .cards import Cards
from .modal import ModalWindow
from .modal_options.modal_tools.city_lables import CityListLable

class WeatherContainer(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.LIST_OF_SETTINGS_CARDS = []
        self.setObjectName("WEATHER_CONTAINER")
        self.MODAL_WINDOW = ModalWindow(parent = self.window())
        self.setFixedSize(828, 800)
        
        self.WEATHER_CONTEINER_LAYOUT = widgets.QVBoxLayout(self)
        self.WEATHER_CONTEINER_LAYOUT.setContentsMargins(0,0,0,0)
        self.WEATHER_CONTEINER_LAYOUT.setSpacing(20)
        self.WEATHER_CONTEINER_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.WEATHER_CONTEINER_LAYOUT)
        
        
        # В weather frame
        self.TOP_FRAME = widgets.QFrame(self)
        self.TOP_FRAME.setFixedSize(790, 36)
        self.TOP_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.TOP_FRAME, alignment = core.Qt.AlignmentFlag.AlignHCenter)
        
        self.TOP_FRAME_LAYOUT = widgets.QHBoxLayout(self.TOP_FRAME)
        self.TOP_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.TOP_FRAME_LAYOUT.setSpacing(278)
        self.TOP_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.TOP_FRAME.setLayout(self.TOP_FRAME_LAYOUT)
        
        # В TOP_FRAME
        self.TOP_SETTINGS_FRAME = widgets.QFrame(self.TOP_FRAME)
        self.TOP_SETTINGS_FRAME.setFixedSize(144, 36)
        self.TOP_SETTINGS_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")

        self.TOP_SETTINGS_FRAME_LAYOUT = widgets.QHBoxLayout(self.TOP_SETTINGS_FRAME)
        self.TOP_SETTINGS_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.TOP_SETTINGS_FRAME_LAYOUT.setSpacing(10)
        self.TOP_SETTINGS_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        self.TOP_FRAME_LAYOUT.addWidget(self.TOP_SETTINGS_FRAME, alignment = core.Qt.AlignmentFlag.AlignLeft)
        
        # В TOP_SETTINGS_FRAME
        self.TOP_SETTINGS_FRAME_BUTTON = widgets.QPushButton(parent = self.TOP_SETTINGS_FRAME, icon = gui.QIcon("media/title_bar/additional_elements/settings.png"))
        self.TOP_SETTINGS_FRAME_BUTTON.setFixedSize(36,36)
        self.TOP_SETTINGS_FRAME_BUTTON.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px;")
        self.TOP_SETTINGS_FRAME_BUTTON.clicked.connect(self.MODAL_WINDOW.show_modal)
        self.TOP_SETTINGS_FRAME_LAYOUT.addWidget(self.TOP_SETTINGS_FRAME_BUTTON, alignment = core.Qt.AlignmentFlag.AlignLeft)   
        
        # В TOP_SETTINGS_FRAME
        self.TOP_SETTINGS_FRAME_LABEL = widgets.QLabel(parent = self.TOP_SETTINGS_FRAME, text = "Налаштування")
        self.TOP_SETTINGS_FRAME_LABEL.setFixedSize(98,16)
        self.TOP_SETTINGS_FRAME_LABEL.setStyleSheet("color: white; font-size: 14px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")

        self.TOP_SETTINGS_FRAME_LAYOUT.addWidget(self.TOP_SETTINGS_FRAME_LABEL, alignment = core.Qt.AlignmentFlag.AlignRight)

        
        
        # В TOP_FRAME
        self.TOP_ADD_SEARCH_FRAME = widgets.QFrame(self.TOP_FRAME)
        self.TOP_ADD_SEARCH_FRAME.setFixedSize(368, 36)
        self.TOP_ADD_SEARCH_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.TOP_FRAME_LAYOUT.addWidget(self.TOP_ADD_SEARCH_FRAME)
        
        self.TOP_ADD_SEARCH_FRAME_LAYOUT = widgets.QHBoxLayout(self.TOP_ADD_SEARCH_FRAME)
        self.TOP_ADD_SEARCH_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.TOP_ADD_SEARCH_FRAME_LAYOUT.setSpacing(10)
        self.TOP_ADD_SEARCH_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        self.TOP_ADD_SEARCH_FRAME.setLayout(self.TOP_ADD_SEARCH_FRAME_LAYOUT)
        
        self.ADD_FRAME = widgets.QFrame(self.TOP_ADD_SEARCH_FRAME)
        self.ADD_FRAME.setStyleSheet("background-color: transparent; border-radius: 4px;")
        self.ADD_FRAME.setFixedSize(97, 36)
        
        self.ADD_FRAME_LAYOUT = widgets.QHBoxLayout(self.ADD_FRAME)
        self.ADD_FRAME_LAYOUT.setContentsMargins(8,7,8,7)
        self.ADD_FRAME_LAYOUT.setSpacing(7)
        self.ADD_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        self.ADD_FRAME.setLayout(self.ADD_FRAME_LAYOUT)
        
        self.ADD_BUTTON = widgets.QPushButton(self.ADD_FRAME)
        self.ADD_BUTTON.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
        self.ADD_BUTTON.setFixedSize(97,36)
        self.ADD_BUTTON.clicked.connect(lambda clicked: self.add_city_card(False))
        
        
        
        self.ADD_BUTTON_ICON = widgets.QLabel(self.ADD_FRAME)
        self.ADD_BUTTON_ICON.setFixedSize(16,22)
        
        add_pixmap = gui.QPixmap(f"media/title_bar/additional_elements/plus_circle.png")
        if not add_pixmap.isNull():
            scaled_pixmap = add_pixmap.scaled(16, 16, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
            self.ADD_BUTTON_ICON.setPixmap(scaled_pixmap)
        
        self.ADD_BUTTON_ICON.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.ADD_BUTTON_ICON.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.ADD_FRAME_LAYOUT.addWidget(self.ADD_BUTTON_ICON, alignment = core.Qt.AlignmentFlag.AlignLeft)
        
        self.ADD_BUTTON_LABEL = widgets.QLabel(self.ADD_FRAME, text = "Додати")
        self.ADD_BUTTON_LABEL.setFixedSize(58, 22)
        self.ADD_BUTTON_LABEL.setStyleSheet("color: white; font-size: 17px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 400;")
        self.ADD_BUTTON_LABEL.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.ADD_FRAME_LAYOUT.addWidget(self.ADD_BUTTON_LABEL, alignment = core.Qt.AlignmentFlag.AlignRight)
        
        self.ADD_BUTTON.hide()
        self.ADD_BUTTON_LABEL.hide()
        self.ADD_BUTTON_ICON.hide()
        
        self.SEARCH_FRAME = SearchFrame(self.TOP_FRAME)
        self.TOP_ADD_SEARCH_FRAME_LAYOUT.addWidget(self.ADD_FRAME, alignment = core.Qt.AlignmentFlag.AlignLeft)
        self.TOP_ADD_SEARCH_FRAME_LAYOUT.addWidget(self.SEARCH_FRAME, alignment = core.Qt.AlignmentFlag.AlignRight)
        
        # Внутри weather frame
        self.MAIN_FRAME = widgets.QFrame(self)
        self.MAIN_FRAME.setFixedSize(788, 677)
        self.MAIN_FRAME.setStyleSheet("border-radius: 17px;")
        self.WEATHER_CONTEINER_LAYOUT.addWidget(self.MAIN_FRAME, alignment = core.Qt.AlignmentFlag.AlignHCenter)
        
        self.MAIN_FRAME_LAYOUT = widgets.QVBoxLayout(self.MAIN_FRAME)
        self.MAIN_FRAME.setLayout(self.MAIN_FRAME_LAYOUT)
        self.MAIN_FRAME_LAYOUT.setSpacing(10)
        self.MAIN_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        
        
        # Внутри main frame
        self.MOMENT_WEATHER_FRAME = widgets.QFrame(self.MAIN_FRAME)
        self.MOMENT_WEATHER_FRAME.setFixedSize(788, 303)
        self.MOMENT_WEATHER_FRAME.setStyleSheet("border-radius: 17px;")
        self.MAIN_FRAME_LAYOUT.addWidget(self.MOMENT_WEATHER_FRAME) 
        
        self.MOMENT_WEATHER_LAYOUT = widgets.QHBoxLayout(self.MOMENT_WEATHER_FRAME)
        self.MOMENT_WEATHER_FRAME.setLayout(self.MOMENT_WEATHER_LAYOUT)
        self.MOMENT_WEATHER_LAYOUT.setContentsMargins(0,0,0,0)
        self.MOMENT_WEATHER_LAYOUT.setSpacing(10)
        
        # Внутри moment weather frame
        self.LEFT_MOMENT_FRAME = widgets.QFrame(self.MOMENT_WEATHER_FRAME)
        self.LEFT_MOMENT_FRAME.setFixedSize(390, 303)
        self.LEFT_MOMENT_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 10px;")
        self.MOMENT_WEATHER_LAYOUT.addWidget(self.LEFT_MOMENT_FRAME)
        
        self.LEFT_MOMENT_LAYOUT = widgets.QVBoxLayout(self.LEFT_MOMENT_FRAME)
        self.LEFT_MOMENT_FRAME.setLayout(self.LEFT_MOMENT_LAYOUT)
        self.LEFT_MOMENT_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.LEFT_MOMENT_LAYOUT.setContentsMargins(0,0,0,0)
        self.LEFT_MOMENT_LAYOUT.setSpacing(16)
        # Внутри left moment frame
        self.LEFT_MOMENT_TOP_FRAME = widgets.QFrame(self.LEFT_MOMENT_FRAME)
        self.LEFT_MOMENT_TOP_FRAME.setFixedSize(358, 27)
        self.LEFT_MOMENT_TOP_FRAME.setStyleSheet("background-color: transparent;")
        self.LEFT_MOMENT_LAYOUT.addWidget(self.LEFT_MOMENT_TOP_FRAME,alignment = core.Qt.AlignmentFlag.AlignCenter)
        # Внутри left moment weather frame
        self.LEFT_CITY_LABEL = widgets.QLabel(self.LEFT_MOMENT_FRAME)
        self.LEFT_CITY_LABEL.setStyleSheet("font-family: 'Roboto';font-weight: 500; color: white; font-size: 44px; border-radius: 0px; background-color: transparent;")
        self.LEFT_CITY_LABEL.setFixedSize(390, 52)
        self.LEFT_CITY_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.LEFT_MOMENT_LAYOUT.addWidget(self.LEFT_CITY_LABEL, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        # Внутри left moment weather frame
        self.LEFT_WEATHER_FRAME = widgets.QFrame(self.LEFT_MOMENT_FRAME)
        self.LEFT_WEATHER_FRAME.setFixedSize(197,87)
        self.LEFT_WEATHER_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent;")
        self.LEFT_MOMENT_LAYOUT.addWidget(self.LEFT_WEATHER_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)

        self.LEFT_WEATHER_LAYOUT = widgets.QHBoxLayout(self.LEFT_WEATHER_FRAME)
        self.LEFT_WEATHER_FRAME.setLayout(self.LEFT_WEATHER_LAYOUT)
        self.LEFT_WEATHER_LAYOUT.setSpacing(0)
        self.LEFT_WEATHER_LAYOUT.setContentsMargins(0,0,0,0)
        self.LEFT_WEATHER_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        # Внутри left weather frame
        self.LEFT_WEATHER_ICON = widgets.QLabel(self.LEFT_WEATHER_FRAME)
        self.LEFT_WEATHER_ICON.setFixedSize(84, 87)
        self.LEFT_WEATHER_ICON_SIZE = core.QSize(76, 76)
        self.LEFT_WEATHER_ICON.setStyleSheet("border-radius: 0px; background-color: transparent;")
        
        self.LEFT_WEATHER_ICON.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.LEFT_WEATHER_ICON.setScaledContents(False)
        self.LEFT_WEATHER_LAYOUT.addWidget(self.LEFT_WEATHER_ICON)
        # Внутри left weather frame
        
        self.LEFT_WEATHER_LABLE_FRAME = widgets.QFrame(self.LEFT_WEATHER_FRAME)
        self.LEFT_WEATHER_LABLE_FRAME.setFixedSize(113, 87)
        self.LEFT_WEATHER_LAYOUT.addWidget(self.LEFT_WEATHER_LABLE_FRAME)
        
        self.LEFT_WEATHER_LABLE_LAYOUT = widgets.QHBoxLayout()
        self.LEFT_WEATHER_LABLE_LAYOUT.setContentsMargins(0,0,0,0)
        self.LEFT_WEATHER_LABLE_LAYOUT.setSpacing(7)
        self.LEFT_WEATHER_LABLE_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.LEFT_WEATHER_LABLE_FRAME.setLayout(self.LEFT_WEATHER_LABLE_LAYOUT)
        
        self.LEFT_WEATHER_LABEL = widgets.QLabel(self.LEFT_WEATHER_LABLE_FRAME)
        self.LEFT_WEATHER_LABEL.setStyleSheet("color: white; font-size: 74px;border-radius: 0px;background-color: transparent;font-family: 'Roboto';font-weight: 500;")
        self.LEFT_WEATHER_LABEL.setFixedSize(80, 87)
        self.LEFT_WEATHER_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignRight | core.Qt.AlignmentFlag.AlignTop)
        self.LEFT_WEATHER_LABLE_LAYOUT.addWidget(self.LEFT_WEATHER_LABEL)

        self.LEFT_WEATHER_LABEL11 = widgets.QLabel(self.LEFT_WEATHER_LABLE_FRAME)
        self.LEFT_WEATHER_LABEL11.setFixedSize(25, 65)
        self.LEFT_WEATHER_LABEL11.setStyleSheet("color: white; font-size: 60px;border-radius: 0px;background-color: transparent;font-family: 'Roboto';font-weight: 500;")
        self.LEFT_WEATHER_LABEL11.setAlignment(core.Qt.AlignmentFlag.AlignBottom)
        self.LEFT_WEATHER_LABLE_LAYOUT.addWidget(self.LEFT_WEATHER_LABEL11)

        # Внутри left moment weather frame
        self.LEFT_DESCRIPTION_FRAME = widgets.QFrame(self.LEFT_MOMENT_FRAME)
        self.LEFT_DESCRIPTION_FRAME.setFixedSize(259, 57)
        self.LEFT_DESCRIPTION_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent;")
        self.LEFT_MOMENT_LAYOUT.addWidget(self.LEFT_DESCRIPTION_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.LEFT_DESCRIPTION_LAYOUT = widgets.QVBoxLayout(self.LEFT_DESCRIPTION_FRAME)
        self.LEFT_DESCRIPTION_FRAME.setLayout(self.LEFT_DESCRIPTION_LAYOUT)
        self.LEFT_DESCRIPTION_LAYOUT.setContentsMargins(0,0,0,0)
        self.LEFT_DESCRIPTION_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignHCenter)

        # Внутри left description frame
        self.LEFT_DESCRIPTION_LABEL1 = widgets.QLabel(self.LEFT_DESCRIPTION_FRAME)
        self.LEFT_DESCRIPTION_LABEL1.setFixedSize(259, 28)
        self.LEFT_DESCRIPTION_LABEL1.setStyleSheet("color: white; font-size: 24px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.LEFT_DESCRIPTION_LABEL1.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.LEFT_DESCRIPTION_LAYOUT.addWidget(self.LEFT_DESCRIPTION_LABEL1, alignment = core.Qt.AlignmentFlag.AlignVCenter)

        # Внутри left description frame
        self.LEFT_DESCRIPTION_LABEL2 = widgets.QLabel(self.LEFT_DESCRIPTION_FRAME)
        self.LEFT_DESCRIPTION_LABEL2.setFixedSize(259, 19)
        self.LEFT_DESCRIPTION_LABEL2.setStyleSheet("color: rgba(255, 255, 255, 0.8); font-size: 16px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.LEFT_DESCRIPTION_LABEL2.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.LEFT_DESCRIPTION_LAYOUT.addWidget(self.LEFT_DESCRIPTION_LABEL2, alignment = core.Qt.AlignmentFlag.AlignVCenter)

        # Внутри moment weather frame
        self.RIGHT_MOMENT_FRAME = widgets.QFrame(self.MOMENT_WEATHER_FRAME)
        self.RIGHT_MOMENT_FRAME.setFixedSize(390, 303)
        self.RIGHT_MOMENT_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 17px;")
        self.MOMENT_WEATHER_LAYOUT.addWidget(self.RIGHT_MOMENT_FRAME)

        self.RIGHT_MOMENT_LAYOUT = widgets.QVBoxLayout(self.RIGHT_MOMENT_FRAME)
        self.RIGHT_MOMENT_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.RIGHT_MOMENT_FRAME.setLayout(self.RIGHT_MOMENT_LAYOUT)
        self.RIGHT_MOMENT_LAYOUT.setContentsMargins(0,0,0,0)
        self.RIGHT_MOMENT_LAYOUT.setSpacing(16)
        
        # Внутри right moment frame
        self.RIGHT_TODAY_FRAME = widgets.QFrame(self.RIGHT_MOMENT_FRAME)
        self.RIGHT_TODAY_FRAME.setFixedSize(358, 27)
        self.RIGHT_TODAY_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent; border-bottom: 1px solid #b4b4b4;")
        self.RIGHT_MOMENT_LAYOUT.addWidget(self.RIGHT_TODAY_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.RIGHT_TODAY_LAYOUT = widgets.QHBoxLayout(self.RIGHT_TODAY_FRAME)
        self.RIGHT_TODAY_FRAME.setLayout(self.RIGHT_TODAY_LAYOUT)
        self.RIGHT_TODAY_LAYOUT.setContentsMargins(0,0,0,0)
        self.RIGHT_TODAY_LAYOUT.setSpacing(0)
        self.RIGHT_TODAY_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
        # Внутри right moment frame
        self.RIGHT_TODAY_LABEL = widgets.QLabel(self.RIGHT_MOMENT_FRAME, text = "Сьогодні")
        self.RIGHT_TODAY_LABEL.setFixedSize(67, 19)
        self.RIGHT_TODAY_LABEL.setStyleSheet("color: white; font-size: 16px; border-radius: 0px;background-color: transparent; border: none; font-family: 'Roboto';font-weight: 500;")
        self.RIGHT_TODAY_LAYOUT.addWidget(self.RIGHT_TODAY_LABEL, alignment = core.Qt.AlignmentFlag.AlignLeft) 
        
        self.RIGHT_DATA_FRAME = widgets.QFrame(self.RIGHT_MOMENT_FRAME)
        self.RIGHT_DATA_FRAME.setFixedSize(358, 44)
        self.RIGHT_DATA_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent;")
        self.RIGHT_MOMENT_LAYOUT.addWidget(self.RIGHT_DATA_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.RIGHT_DATA_LAYOUT = widgets.QHBoxLayout(self.RIGHT_DATA_FRAME)
        self.RIGHT_DATA_FRAME.setLayout(self.RIGHT_DATA_LAYOUT)
        self.RIGHT_DATA_LAYOUT.setContentsMargins(0,0,0,0)
        self.RIGHT_DATA_LAYOUT.setSpacing(116)
        self.RIGHT_DATA_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        # Внутри right data frame
        self.RIGHT_DATA_LABEL1 = widgets.QLabel(self.RIGHT_DATA_FRAME)
        self.RIGHT_DATA_LABEL1.setFixedSize(123, 28)
        self.RIGHT_DATA_LABEL1.setStyleSheet("color: white; font-size: 24px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.RIGHT_DATA_LAYOUT.addWidget(self.RIGHT_DATA_LABEL1, alignment = core.Qt.AlignmentFlag.AlignLeft)
        
        # Внутри right data frame
        self.RIGHT_DATA_LABEL2 = widgets.QLabel(self.RIGHT_DATA_FRAME)
        self.RIGHT_DATA_LABEL2.setFixedSize(123, 28)
        self.RIGHT_DATA_LABEL2.setStyleSheet("color: white; font-size: 24px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.RIGHT_DATA_LAYOUT.addWidget(self.RIGHT_DATA_LABEL2, alignment = core.Qt.AlignmentFlag.AlignRight)
        
        # Внутри right moment frame
        self.RIGHT_CLOCK_FRAME = widgets.QLabel(self.RIGHT_MOMENT_FRAME)
        self.RIGHT_CLOCK_FRAME.setFixedSize(168,168)
        self.RIGHT_CLOCK_FRAME.setStyleSheet("border-radius: 0px;background-color: transparent;")
        self.RIGHT_MOMENT_LAYOUT.addWidget(self.RIGHT_CLOCK_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.RIGHT_CLOCK_LAYOUT = widgets.QHBoxLayout(self.RIGHT_CLOCK_FRAME)
        self.RIGHT_CLOCK_FRAME.setLayout(self.RIGHT_CLOCK_LAYOUT)
        self.RIGHT_CLOCK_LAYOUT.setContentsMargins(0,0,0,0)
        self.RIGHT_CLOCK_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.RIGHT_CLOCK_LAYOUT.setSpacing(0)
        
        # Внутри right clock frame
        self.RIGHT_CLOCK_LABEL = widgets.QLabel(self.RIGHT_CLOCK_FRAME)
        self.RIGHT_CLOCK_LABEL.setFixedSize(74,34)
        self.RIGHT_CLOCK_LABEL.setStyleSheet("color: white; font-size: 29px; border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 500;")
        self.RIGHT_CLOCK_LAYOUT.addWidget(self.RIGHT_CLOCK_LABEL)
        
        # weather scroll bar
        # Внутри main frame
        self.DAY_WEATHER_FRAME = widgets.QFrame(self.MAIN_FRAME) 
        self.DAY_WEATHER_FRAME.setFixedSize(788, 157)
        self.DAY_WEATHER_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 10px;")
        self.MAIN_FRAME_LAYOUT.addWidget(self.DAY_WEATHER_FRAME)
        
        self.DAY_WEATHER_FRAME_LAYOUT = widgets.QVBoxLayout(self.DAY_WEATHER_FRAME)
        self.DAY_WEATHER_FRAME.setLayout(self.DAY_WEATHER_FRAME_LAYOUT)
        self.DAY_WEATHER_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.DAY_WEATHER_FRAME_LAYOUT.setContentsMargins(0,16,0,16)
        self.DAY_WEATHER_FRAME_LAYOUT.setSpacing(16)
        
        self.DAY_WEATHER_TOP_LABEL = widgets.QLabel(self.DAY_WEATHER_FRAME, text = "Очікуваний прогноз погоди на 5 днів")
        self.DAY_WEATHER_TOP_LABEL.setFixedSize(756, 27)
        self.DAY_WEATHER_TOP_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignVCenter and core.Qt.AlignmentFlag.AlignLeft) 
        self.DAY_WEATHER_FRAME_LAYOUT.addWidget(self.DAY_WEATHER_TOP_LABEL, alignment = core.Qt.AlignmentFlag.AlignCenter)
        self.DAY_WEATHER_TOP_LABEL.setStyleSheet("border-radius: 0px; background-color: transparent; font-family: 'Roboto'; font-weight: 500; color: #FFFFFF; font-size: 16px; border-bottom: 1px solid #b4b4b4;")
        
        self.DAY_WEATHER_MAIN_SCROLL_FRAME = widgets.QFrame(self.DAY_WEATHER_FRAME)
        self.DAY_WEATHER_MAIN_SCROLL_FRAME.setFixedSize(756, 82)
        self.DAY_WEATHER_MAIN_SCROLL_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        
        self.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT = widgets.QHBoxLayout(self.DAY_WEATHER_MAIN_SCROLL_FRAME)
        self.DAY_WEATHER_MAIN_SCROLL_FRAME.setLayout(self.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT)
        
        self.DAY_WEATHER_FRAME_LAYOUT.addWidget(self.DAY_WEATHER_MAIN_SCROLL_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT.setSpacing(24)
        self.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        self.SCROLL_LEFT_BUTTON = widgets.QPushButton(self.DAY_WEATHER_MAIN_SCROLL_FRAME, text = "<")
        self.SCROLL_LEFT_BUTTON.setFixedSize(16, 16)
        self.SCROLL_LEFT_BUTTON.clicked.connect(self.scroll_left)
        self.SCROLL_LEFT_BUTTON.setStyleSheet("background-color: transparent; border-radius: 0px;")
        
        self.SCROLL_RIGHT_BUTTON = widgets.QPushButton(self.DAY_WEATHER_MAIN_SCROLL_FRAME, text = ">")
        self.SCROLL_RIGHT_BUTTON.setFixedSize(16, 16)
        self.SCROLL_RIGHT_BUTTON.clicked.connect(self.scroll_right)
        self.SCROLL_RIGHT_BUTTON.setStyleSheet("background-color: transparent; border-radius: 0px;")
        
        self.DAY_WEATHER_SCROLL_PARENT = widgets.QFrame(parent = self.DAY_WEATHER_MAIN_SCROLL_FRAME)
        self.DAY_WEATHER_SCROLL_PARENT.setFixedSize(656, 82)
        
        self.DAY_WEATHER_SCROLL_PARENT.setStyleSheet("background-color: transparent; border-radius: 0px;")
        
        
        self.DAY_WEATHER_SCROLL_AREA = Horizontal_Scroll(parent = self.DAY_WEATHER_SCROLL_PARENT)
        self.DAY_WEATHER_SCROLL_AREA.setWidgetResizable(True)
        self.DAY_WEATHER_SCROLL_AREA.setFixedSize(656, 82)  
        self.DAY_WEATHER_SCROLL_AREA.setStyleSheet("background-color: transparent;")

        self.DAY_WEATHER_SCROLL_FRAME = widgets.QFrame(parent = self.DAY_WEATHER_SCROLL_AREA)
        self.DAY_WEATHER_SCROLL_AREA.setWidget(self.DAY_WEATHER_SCROLL_FRAME)
        self.DAY_WEATHER_SCROLL_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")  
        
        self.DAY_WEATHER_SCROLL_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.DAY_WEATHER_SCROLL_FRAME.setLayout(self.DAY_WEATHER_SCROLL_FRAME_LAYOUT)
        
        self.DAY_WEATHER_SCROLL_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.DAY_WEATHER_SCROLL_FRAME_LAYOUT.setSpacing(17)
        self.DAY_WEATHER_SCROLL_FRAME_LAYOUT.setContentsMargins(0,0,16,0)
        
        self.DAY_WEATHER_SCROLL_AREA.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.DAY_WEATHER_SCROLL_AREA.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        
        
        self.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT.addWidget(self.SCROLL_LEFT_BUTTON, alignment = core.Qt.AlignmentFlag.AlignLeft) 
        self.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT.addWidget(self.DAY_WEATHER_SCROLL_PARENT, alignment = core.Qt.AlignmentFlag.AlignCenter)
        self.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT.addWidget(self.SCROLL_RIGHT_BUTTON, alignment = core.Qt.AlignmentFlag.AlignRight)

        
        
        
        # Диаграма
        # Внутри main frame
        self.DIAGRAM_WEATHER_FRAME = widgets.QFrame(self.MAIN_FRAME)
        self.DIAGRAM_WEATHER_FRAME.setFixedSize(788, 197)
        self.DIAGRAM_WEATHER_FRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 10px;")
        self.MAIN_FRAME_LAYOUT.addWidget(self.DIAGRAM_WEATHER_FRAME)
        
        self.DIAGRAM_FRAME_LAYOUT = widgets.QVBoxLayout(self.DIAGRAM_WEATHER_FRAME)
        self.DIAGRAM_WEATHER_FRAME.setLayout(self.DIAGRAM_FRAME_LAYOUT)
        self.DIAGRAM_FRAME_LAYOUT.setContentsMargins(16,16,16,16)
        self.DIAGRAM_FRAME_LAYOUT.setSpacing(0)
        # Внутри diagram weather frame
        self.MAIN_DIAGRAM_FRAME = widgets.QFrame(self.DIAGRAM_WEATHER_FRAME)
        self.MAIN_DIAGRAM_FRAME.setFixedSize(756,165)
        self.MAIN_DIAGRAM_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.DIAGRAM_FRAME_LAYOUT.addWidget(self.MAIN_DIAGRAM_FRAME)

        self.MAIN_DIAGRAM_FRAME_LAYOUT = widgets.QVBoxLayout(self.MAIN_DIAGRAM_FRAME)
        self.MAIN_DIAGRAM_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.MAIN_DIAGRAM_FRAME_LAYOUT.setSpacing(8)
        self.MAIN_DIAGRAM_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.MAIN_DIAGRAM_FRAME.setLayout(self.MAIN_DIAGRAM_FRAME_LAYOUT)
        
        # Внутри main diagram frame
        self.DIAGRAM_LABEL = widgets.QLabel(self.MAIN_DIAGRAM_FRAME, text = "Прогноз на 36 годин")
        self.DIAGRAM_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignVCenter and core.Qt.AlignmentFlag.AlignLeft)
        self.DIAGRAM_LABEL.setFixedSize(756, 27)
        self.DIAGRAM_LABEL.setStyleSheet("border-radius: 0px; background-color: transparent; font-family: 'Roboto'; font-weight: 500; color: #FFFFFF; font-size: 16px; border-bottom: 1px solid #b4b4b4;")
        self.MAIN_DIAGRAM_FRAME_LAYOUT.addWidget(self.DIAGRAM_LABEL, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        # Внутри main diagram frame
        self.FORECAST_DIAGRAM_FRAME = widgets.QFrame(self.MAIN_DIAGRAM_FRAME)
        self.FORECAST_DIAGRAM_FRAME.setFixedSize(758, 130)
        self.FORECAST_DIAGRAM_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.MAIN_DIAGRAM_FRAME_LAYOUT.addWidget(self.FORECAST_DIAGRAM_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.FORECAST_DIAGRAM_FRAME_LAYOUT = widgets.QVBoxLayout(self.FORECAST_DIAGRAM_FRAME)
        self.FORECAST_DIAGRAM_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.FORECAST_DIAGRAM_FRAME_LAYOUT.setSpacing(0)
        self.FORECAST_DIAGRAM_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.FORECAST_DIAGRAM_FRAME.setLayout(self.FORECAST_DIAGRAM_FRAME_LAYOUT)

        # Внутри forecast diagram frame
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME = widgets.QFrame(self.FORECAST_DIAGRAM_FRAME)
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME.setFixedSize(758, 20)
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        
        self.FORECAST_DIAGRAM_FRAME_LAYOUT.addWidget(self.FORECAST_DIAGRAM_ICON_PARENT_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME_LAYOUT = widgets.QHBoxLayout(self.FORECAST_DIAGRAM_ICON_PARENT_FRAME)
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME_LAYOUT.setSpacing(0)
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME.setLayout(self.FORECAST_DIAGRAM_ICON_PARENT_FRAME_LAYOUT)

        # Внутри forecast diagram icon parent frame  
        
        self.FORECAST_DIAGRAM_ICON_FRAME = widgets.QFrame(self.FORECAST_DIAGRAM_FRAME)
        self.FORECAST_DIAGRAM_ICON_FRAME.setFixedSize(730, 20)
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME_LAYOUT.addWidget(self.FORECAST_DIAGRAM_ICON_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT = widgets.QHBoxLayout(self.FORECAST_DIAGRAM_ICON_FRAME)
        self.FORECAST_DIAGRAM_ICON_FRAME.setLayout(self.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT)
        self.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT
        self.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT.setSpacing(19)
        
        # Внутри forecast diagram icon parent frame
        self.FORECAST_DIAGRAM_ICON_PARENT_CORNER_FRAME = widgets.QFrame(self.FORECAST_DIAGRAM_ICON_PARENT_FRAME)
        self.FORECAST_DIAGRAM_ICON_PARENT_CORNER_FRAME.setFixedSize(32,20)
        self.FORECAST_DIAGRAM_ICON_PARENT_CORNER_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.FORECAST_DIAGRAM_ICON_PARENT_FRAME_LAYOUT.addWidget(self.FORECAST_DIAGRAM_ICON_PARENT_CORNER_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)

        # Внутри forecast diagram frame
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME = widgets.QFrame(self.FORECAST_DIAGRAM_FRAME)
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME.setFixedSize(758, 110)
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.FORECAST_DIAGRAM_FRAME_LAYOUT.addWidget(self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME_LAYOUT = widgets.QHBoxLayout(self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME)
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME_LAYOUT.setSpacing(0)
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME.setLayout(self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME_LAYOUT)
        # Внутри forecast diagram and temperature frame
        
        self.FORECAST_DIAGRAM_ITSELF_FRAME = widgets.QFrame(self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME)
        self.FORECAST_DIAGRAM_ITSELF_FRAME.setFixedSize(728, 110)
        self.FORECAST_DIAGRAM_ITSELF_FRAME.setStyleSheet("background-image: url('media/title_bar/additional_elements/spreadsheet.png');")
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME_LAYOUT.addWidget(self.FORECAST_DIAGRAM_ITSELF_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)
        
        self.FORECAST_DIAGRAM_ITSELF_LAYOUT = widgets.QHBoxLayout(self.FORECAST_DIAGRAM_ITSELF_FRAME)
        self.FORECAST_DIAGRAM_ITSELF_LAYOUT.setContentsMargins(1,0,3,0)
        self.FORECAST_DIAGRAM_ITSELF_LAYOUT.setSpacing(3)
        self.FORECAST_DIAGRAM_ITSELF_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignBottom)
        self.FORECAST_DIAGRAM_ITSELF_FRAME.setLayout(self.FORECAST_DIAGRAM_ITSELF_LAYOUT)
        # Внутри forecast diagram and temperature frame
        
        self.FORECAST_TEMPERATURE_ITSELF_LABEL = widgets.QLabel(parent = self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME,text ="25°\n20°\n15°\n10°\n5°\n0°\n-5°\n-10°")
        self.FORECAST_TEMPERATURE_ITSELF_LABEL.setStyleSheet(f"border-radius: 0px; background-color: transparent; font-family: 'Roboto'; font-weight: 400; color: #FFFFFF; font-size: 12px;")
        self.FORECAST_TEMPERATURE_ITSELF_LABEL.setFixedSize(30, 110)
        self.FORECAST_TEMPERATURE_ITSELF_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignVCenter)
        self.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME_LAYOUT.addWidget(self.FORECAST_TEMPERATURE_ITSELF_LABEL, alignment = core.Qt.AlignmentFlag.AlignCenter)

    def scroll_left(self):
        hbar = self.DAY_WEATHER_SCROLL_AREA.horizontalScrollBar()
        hbar.setValue(hbar.minimum())

    def scroll_right(self):
        hbar = self.DAY_WEATHER_SCROLL_AREA.horizontalScrollBar()
        hbar.setValue(hbar.maximum())
    
    def add_city_card(self,settings_clicked):
        
        our_search_field = self.window().findChild(widgets.QLineEdit, "SEARCH_FIELD")
        our_left_container = self.window().findChild(widgets.QFrame, "Left_container")
        modal_city_menu = self.window().findChild(widgets.QFrame, "DROP_CITY_MODAL")
        search_city = self.window().findChild(widgets.QFrame,"SEARCHCITY")
        self.DROP_COUNTRY_MODAL = self.window().findChild(widgets.QFrame,"DROP_COUNTRY_MODAL")
        try:
            
            
            if settings_clicked == False:    
                city_card = Cards(parent = our_left_container.scroll_frame, city_name = our_search_field.text())
                
                if hasattr(search_city, 'CITY_LIST_SCROLL_AREA_FRAME') and search_city.CHOOSED:
                    settings_city_card = CityListLable(parent= search_city.CITY_LIST_SCROLL_AREA_FRAME,city_name = our_search_field.text())
                    self.LIST_OF_SETTINGS_CARDS.append(our_search_field.text())
                    search_city.update_map_coordinates(
                        city_card.REQUEST_DATA["coord"]["lat"],
                        city_card.REQUEST_DATA["coord"]["lon"]
                    )
                our_left_container.scroll_frame_layout.addWidget(city_card, alignment = core.Qt.AlignmentFlag.AlignHCenter)
                city_card.select()
                our_search_field.clear()
                self.ADD_BUTTON.hide()
                self.ADD_BUTTON_LABEL.hide()
                self.ADD_BUTTON_ICON.hide()
            elif settings_clicked and modal_city_menu.CITY_NAME and self.DROP_COUNTRY_MODAL.COUNTRY_NAME:
                if modal_city_menu.CITY_LINEEDIT.text() != "" :
                    city_card = Cards(parent = our_left_container.scroll_frame, city_name = modal_city_menu.CITY_NAME)
                    
                    if hasattr(search_city, 'CITY_LIST_SCROLL_AREA_FRAME') and search_city.CHOOSED:
                        settings_city_card = CityListLable(parent= search_city.CITY_LIST_SCROLL_AREA_FRAME,city_name = modal_city_menu.CITY_NAME)
                        self.LIST_OF_SETTINGS_CARDS.append(modal_city_menu.CITY_NAME)
                        search_city.update_map_coordinates(
                            city_card.REQUEST_DATA["coord"]["lat"],
                            city_card.REQUEST_DATA["coord"]["lon"]
                        )
                    our_left_container.scroll_frame_layout.addWidget(city_card, alignment = core.Qt.AlignmentFlag.AlignHCenter)
                    city_card.select()
                    close_drop_menu(self.window())
        except Exception as e:
            print(e)

import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
import PyQt6.QtWebEngineWidgets as WebEngine

import folium 
import io

from .cards import Cards

class LeftContainer(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.COUNTER = 1
        self.setFixedSize(370, 828)
        
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
        
        leftcontainer_layout = widgets.QVBoxLayout()
        self.setLayout(leftcontainer_layout)
        leftcontainer_layout.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        leftcontainer_layout.setContentsMargins(0,0,0,0)
        
        leftcontainer_layout.setSpacing(0)
        
        leftcontainer_header = widgets.QFrame(self)
        leftcontainer_header.setFixedSize(370, 44)
        
        header_layout = widgets.QHBoxLayout()
        header_layout.setAlignment(core.Qt.AlignmentFlag.AlignRight)
        leftcontainer_header.setLayout(header_layout)
        
        leftcontainer_layout.addWidget(leftcontainer_header)    
            
        self.CHANGE_THEME_BUTTON = widgets.QPushButton(parent = leftcontainer_header)
        
        self.CHANGE_THEME_BUTTON.setFixedSize(54,24)
        self.CHANGE_THEME_BUTTON.setIconSize(self.CHANGE_THEME_BUTTON.size())
        
        self.CHANGE_THEME_BUTTON.setStyleSheet("border : none;background-color: transparent;")
        
        change_theme_icon = gui.QIcon("media/title_bar/light_theme.svg")
        self.CHANGE_THEME_BUTTON.setIcon(change_theme_icon)
        
        self.CHANGE_THEME_BUTTON.clicked.connect(self.change_button)
        
        header_layout.addWidget(self.CHANGE_THEME_BUTTON)
        
        
        frame = widgets.QFrame(parent = self)
        frame.setFixedSize(370, 756)

        leftcontainer_layout.addWidget(frame)

        scroll_area = widgets.QScrollArea(parent = frame)
        
        scroll_frame = widgets.QFrame(parent = scroll_area)
        
        scroll_frame_layout = widgets.QVBoxLayout()
        scroll_frame.setLayout(scroll_frame_layout)
        
        scroll_frame_layout.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
        scroll_area.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        

        scroll_area.setFixedSize(370, 730)
        scroll_area.setStyleSheet("background-color: transparent;")
        
        scroll_area.setWidget(scroll_frame)
        scroll_area.setWidgetResizable(True)
        
        leftcontainer_layout.addWidget(frame)
        
        for number in range(30):
            card = Cards(parent = scroll_frame)
            scroll_frame_layout.addWidget(card, alignment = core.Qt.AlignmentFlag.AlignHCenter)
    
    def change_button(self):
        
        if self.COUNTER % 2 == 0:
            icon = gui.QIcon("media/title_bar/dark_theme.svg")
            self.CHANGE_THEME_BUTTON.setIcon(icon)
        else:
            icon = gui.QIcon("media/title_bar/light_theme.svg")
            self.CHANGE_THEME_BUTTON.setIcon(icon)
        self.COUNTER += 1
    
        
        
        
        
        
        # self.open_modal_button = widgets.QPushButton(parent = self, text = "Открыть окно")
        # self.open_modal_button.setGeometry(50,50,150,40)
        # self.open_modal_button.clicked.connect(self.open_modal)

    # def open_modal(self):
    #     # Получаем главное окно (объект)
    #     main_window = self.window()
        
    #     self.MODAL = widgets.QWidget(main_window)
    #     self.MODAL.setGeometry(10,10, 790, 688)
    #     self.MODAL.setStyleSheet("background-color: white")
    #     modal_layout = widgets.QVBoxLayout()
    #     modal_layout.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
    #     # Объекты выравнивания
    #     # core.Qt.AlignmentFlag.AlignTop
        
    #     self.MODAL.setLayout(modal_layout)
        
    #     header_frame = widgets.QFrame(parent = self.MODAL)
    #     frame_layout = widgets.QHBoxLayout()
    #     frame_layout.setAlignment(core.Qt.AlignmentFlag.AlignRight)
    #     header_frame.setLayout(frame_layout)
    #     header_frame.setFixedSize(742, 28)
    #     modal_layout.addWidget(header_frame)
    #     header_frame.setStyleSheet("background-color: cyan")
        
    #     close_button = widgets.QPushButton(parent = header_frame)
    #     frame_layout.addWidget(close_button)
    #     close_button.setFixedSize(24, 24)
        
    #     icon = QtGui.QIcon("media/close.svg")
    #     close_button.setIcon(icon)
    #     close_button.clicked.connect(self.MODAL.hide)
        
    #     data = io.BytesIO()

    #     map = folium.Map(location = (50, 50))
    #     #save() - сохраняет данные карты в дате обьекта
    #     #close_file - =False(оставляем дата обьекта открытым для будущих обновлений карты)
    #     map.save(data,close_file = False)

    #     self.MODAL.show()
    #     web_engine_view = WebEngine.QWebEngineView(parent = self.MODAL)
    #     web_engine_view.setFixedSize(289,256)
    #     modal_layout.addWidget(web_engine_view)
        
    #     html = data.getvalue().decode()
        
    #     web_engine_view.setHtml(html)
        

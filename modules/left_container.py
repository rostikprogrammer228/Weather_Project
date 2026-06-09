import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
import PyQt6.QtWebEngineWidgets as WebEngine
import folium 
import io

from utils import request
from .cards import Cards

class LeftContainer(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.COUNTER = 0
        
        self.setObjectName("Left_container")
        
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
        
        self.scroll_frame = widgets.QFrame(parent = scroll_area)
        
        self.scroll_frame_layout = widgets.QVBoxLayout()
        self.scroll_frame.setLayout(self.scroll_frame_layout)
        
        self.scroll_frame_layout.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
        scroll_area.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        

        scroll_area.setFixedSize(370, 730)
        scroll_area.setStyleSheet("background-color: transparent;")
        
        scroll_area.setWidget(self.scroll_frame)
        scroll_area.setWidgetResizable(True)
        
        leftcontainer_layout.addWidget(frame)
        
        
        
       
   
    def change_button(self):
        our_content_container = self.window().findChild(widgets.QFrame, "Content_container")
        if self.COUNTER % 2 == 0:
            icon = gui.QIcon("media/title_bar/dark_theme.svg")
            self.CHANGE_THEME_BUTTON.setIcon(icon)
            our_content_container.setStyleSheet("""
            #Content_container {
                background: qlineargradient(
                    x1:0 y1:1,
                    x2:1 y2:0,
                    stop:0 #191970 stop:1 #8A2BE2
                    );
            }
        """)
        else:
            icon = gui.QIcon("media/title_bar/light_theme.svg")
            our_content_container.setStyleSheet("""
            #Content_container {
                background: qlineargradient(
                    x1:0 y1:1,
                    x2:1 y2:0,
                    stop:0 #87CEFA stop:1 #FFDF56
                    );
            }
        """)
            self.CHANGE_THEME_BUTTON.setIcon(icon)
        self.COUNTER += 1
    

        
        


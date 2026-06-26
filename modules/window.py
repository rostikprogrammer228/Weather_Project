import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui


from .app import application
from .left_container import LeftContainer
from .weather_container import WeatherContainer
from utils import close_drop_menu
from .header import Header
class MainWindow(widgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setObjectName("Window")
        
        self.setWindowFlags(core.Qt.WindowType.FramelessWindowHint)
        self.COUNTER = 0
        self.window_width = 1200
        self.window_height = 800

        self.screen = application.primaryScreen()
        self.screen_size = self.screen.size()

        self.screen_width = self.screen_size.width()
        self.screen_height = self.screen_size.height()

        self.center_x = (self.screen_width // 2) - (self.window_width // 2)
        self.center_y = (self.screen_height // 2) - (self.window_height // 2)

        self.setGeometry(self.center_x, self.center_y, self.window_width, self.window_height)
        self.setWindowTitle("Project")
        
        self.content_container = widgets.QFrame(parent = self)
        
        
        
        self.content_layout = widgets.QVBoxLayout()
        self.content_layout.setSpacing(0)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_container.setLayout(self.content_layout)
        
        self.content_container.setFixedSize(self.window_width, self.window_height)
        
        
        
        self.HEADER = Header(parent = self.content_container)
        self.content_layout.addWidget(self.HEADER)
        
        
        self.central_widget = widgets.QWidget(self.content_container)
        self.central_widget.setFixedSize(1200,800)
        self.content_layout.addWidget(self.central_widget)
        
        self.content_container.setObjectName("Content_container")
        
        self.content_container.setStyleSheet("""
            #Content_container {
                background: qlineargradient(
                    x1:0 y1:1,
                    x2:1 y2:0,
                    stop:0 #87CEFA stop:1 #FFDF56
                    );
            }
        """)
        
        self.center_widget_layout = widgets.QHBoxLayout()
        self.center_widget_layout.setSpacing(0)
        self.center_widget_layout.setContentsMargins(0, 0, 0, 0)
        
        
        self.central_widget.setLayout(self.center_widget_layout)
        
        self.LEFT_CONTAINER = LeftContainer(parent = self.central_widget)
        self.WEATHER_CONTAINER = WeatherContainer(parent = self.central_widget)
       
        self.center_widget_layout.addWidget(self.LEFT_CONTAINER)
        self.center_widget_layout.addWidget(self.WEATHER_CONTAINER)

    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton:
            close_drop_menu(self)
   
        
main_window = MainWindow()
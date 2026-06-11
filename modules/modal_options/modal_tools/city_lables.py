import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core

class CityListLable(widgets.QFrame):
    def __init__(self, parent, city_name):
        super().__init__(parent)
        
        self.CITY_LIST_LAYOUT = self.window().findChild(widgets.QFrame,"SEARCHCITY")

        
        
        
        self.setFixedSize(512, 32)
        self.setStyleSheet("background-color: transparent; border: none;")
        self.CITY_LIST_LAYOUT.CITY_LIST_SCROLL_AREA_FRAME_LAYOUT.addWidget(self)
        
        self.CITY_LAYOUT = widgets.QHBoxLayout()
        self.CITY_LAYOUT.setContentsMargins(0, 8, 0, 8)
        self.CITY_LAYOUT.setSpacing(0)
        self.setLayout(self.CITY_LAYOUT)
        
        self.CITY_LABEL = widgets.QLabel(parent = self, text = city_name)
        self.CITY_LABEL.setFixedSize(496, 20)
        self.CITY_LABEL.setStyleSheet("color: white; font-size: 14px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 400;")
        self.CITY_LAYOUT.addWidget(self.CITY_LABEL)
        
        self.DELETE_BUTTON = widgets.QPushButton(self)
        self.DELETE_BUTTON.setFixedSize(16, 16)
        self.DELETE_BUTTON.setStyleSheet("background-color: transparent; border: none;")
        
        self.DELETE_ICON = gui.QIcon("media/title_bar/additional_elements/trash.png")
        self.DELETE_BUTTON.setIcon(self.DELETE_ICON)
        # self.DELETE_BUTTON.clicked.connect(self.delete)
        self.CITY_LAYOUT.addWidget(self.DELETE_BUTTON)
        
        
    def delete(self):
        pass
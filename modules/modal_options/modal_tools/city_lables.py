import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core

from utils.clear_layout  import clear_layout
from modules.cards import Cards
from utils.clear_weather_frame import clear_weather_frame
from utils import scale
class CityListLable(widgets.QFrame):
    def __init__(self, parent, city_name):
        super().__init__(parent)
        
        self.CITY_LIST_LAYOUT = self.window().findChild(widgets.QFrame,"SEARCHCITY")

        
        
        
        self.setFixedSize(scale.scale_x(512), scale.scale_y(32))
        self.setStyleSheet("background-color: transparent; border: none;")
        self.CITY_LIST_LAYOUT.CITY_LIST_SCROLL_AREA_FRAME_LAYOUT.addWidget(self)
        
        self.CITY_LAYOUT = widgets.QHBoxLayout()
        self.CITY_LAYOUT.setContentsMargins(0, scale.scale_y(8), 0, scale.scale_y(8))
        self.CITY_LAYOUT.setSpacing(0)
        self.setLayout(self.CITY_LAYOUT)
        
        self.CITY_LABEL = widgets.QLabel(parent = self, text = city_name)
        self.CITY_LABEL.setFixedSize(scale.scale_x(496), scale.scale_y(20))
        self.CITY_LABEL.setStyleSheet("color: white;border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 400;")
        scale.setFontSize(self.CITY_LABEL,14)
        self.CITY_LAYOUT.addWidget(self.CITY_LABEL)
        
        self.DELETE_BUTTON = widgets.QPushButton(self)
        self.DELETE_BUTTON.setFixedSize(scale.scale_x(16), scale.scale_y(16))
        self.DELETE_BUTTON.setStyleSheet("background-color: transparent; border: none;")
        
        self.DELETE_ICON = gui.QPixmap("media/title_bar/additional_elements/trash.png")
        if not self.DELETE_ICON.isNull():
                scaled_pixmap = self.DELETE_ICON.scaled(scale.scale_x(16),scale.scale_y(16), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
        self.DELETE_BUTTON.setIcon(gui.QIcon(scaled_pixmap))
        self.DELETE_BUTTON.clicked.connect(self.delete)
        self.CITY_LAYOUT.addWidget(self.DELETE_BUTTON)
        
        self.CITY_NAME = city_name
        
    def delete(self):
        main_window = self.window()
        if not main_window:
            return

        weather_container = main_window.findChild(widgets.QFrame, "WEATHER_CONTAINER")
        left_container = main_window.findChild(widgets.QFrame, "Left_container")

        if weather_container and hasattr(weather_container, 'LIST_OF_SETTINGS_CARDS'):
            try:
                weather_container.LIST_OF_SETTINGS_CARDS.remove(self.CITY_NAME)
            except ValueError:
                pass

        if left_container and hasattr(left_container, 'scroll_frame_layout'):
            for index in range(left_container.scroll_frame_layout.count() - 1, -1, -1):
                item = left_container.scroll_frame_layout.itemAt(index)
                if not item:
                    continue
                widget = item.widget()
                if widget and getattr(widget, 'CITY_NAME', None) == self.CITY_NAME:
                    left_container.scroll_frame_layout.removeWidget(widget)
                    if widget in Cards.CARDS_LIST:
                        Cards.CARDS_LIST.remove(widget)
                    widget.setParent(None)
                    widget.deleteLater()
                    break

        clear_weather_frame(weather_container = weather_container)

        parent_layout = self.parent().layout() if self.parent() else None
        if parent_layout:
            parent_layout.removeWidget(self)
        self.setParent(None)
        self.deleteLater()
        
        

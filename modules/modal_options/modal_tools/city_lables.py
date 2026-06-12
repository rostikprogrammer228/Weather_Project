import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core

from utils import clear_layout
from modules.cards import Cards

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

        if weather_container:
            if hasattr(weather_container, 'LEFT_CITY_LABEL'):
                weather_container.LEFT_CITY_LABEL.setText("")
            if hasattr(weather_container, 'LEFT_WEATHER_LABEL'):
                weather_container.LEFT_WEATHER_LABEL.setText("")
            if hasattr(weather_container, 'LEFT_WEATHER_LABEL11'):
                weather_container.LEFT_WEATHER_LABEL11.setText("")
            if hasattr(weather_container, 'LEFT_DESCRIPTION_LABEL1'):
                weather_container.LEFT_DESCRIPTION_LABEL1.setText("")
            if hasattr(weather_container, 'LEFT_DESCRIPTION_LABEL2'):
                weather_container.LEFT_DESCRIPTION_LABEL2.setText("")
            if hasattr(weather_container, 'LEFT_WEATHER_ICON'):
                weather_container.LEFT_WEATHER_ICON.clear()
            if hasattr(weather_container, 'RIGHT_DATA_LABEL1'):
                weather_container.RIGHT_DATA_LABEL1.setText("")
            if hasattr(weather_container, 'RIGHT_DATA_LABEL2'):
                weather_container.RIGHT_DATA_LABEL2.setText("")
            if hasattr(weather_container, 'RIGHT_CLOCK_LABEL'):
                weather_container.RIGHT_CLOCK_LABEL.setText("")
            if hasattr(weather_container, 'RIGHT_CLOCK_FRAME'):
                weather_container.RIGHT_CLOCK_FRAME.clear()
            if hasattr(weather_container, 'DAY_WEATHER_SCROLL_FRAME_LAYOUT'):
                clear_layout(weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT)
            if hasattr(weather_container, 'FORECAST_DIAGRAM_ICON_FRAME_LAYOUT'):
                clear_layout(weather_container.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT)
            if hasattr(weather_container, 'FORECAST_DIAGRAM_ITSELF_LAYOUT'):
                clear_layout(weather_container.FORECAST_DIAGRAM_ITSELF_LAYOUT)

        parent_layout = self.parent().layout() if self.parent() else None
        if parent_layout:
            parent_layout.removeWidget(self)
        self.setParent(None)
        self.deleteLater()
        
        
    # main_window = self.window()
    #     if main_window:
    #         weather_container = main_window.findChild(widgets.QFrame, "WEATHER_CONTAINER")
    #         left_container = main_window.findChild(widgets.QFrame, "Left_container")
    #         if weather_container and hasattr(weather_container, 'LIST_OF_SETTINGS_CARDS'):
    #             weather_container.LIST_OF_SETTINGS_CARDS = [name for name in weather_container.LIST_OF_SETTINGS_CARDS if name != self.CITY_NAME]
    #         if left_container and hasattr(left_container, 'scroll_frame_layout'):
    #             for index in range(left_container.scroll_frame_layout.count() - 1, -1, -1):
    #                 item = left_container.scroll_frame_layout.itemAt(index)
    #                 if item:
    #                     widget = item.widget()
    #                     if widget and getattr(widget, 'CITY_NAME', None) == self.CITY_NAME:
    #                         left_container.scroll_frame_layout.removeWidget(widget)
    #                         widget.setParent(None)
    #                         widget.deleteLater()
    #     parent_layout = self.parent().layout() if self.parent() else None
    #     if parent_layout:
    #         parent_layout.removeWidget(self)
    #     self.setParent(None)
    #     self.deleteLater()
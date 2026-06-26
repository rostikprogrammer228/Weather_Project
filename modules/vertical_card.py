import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core
from utils import scale
class Vertical_Card(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        self.setObjectName("Vertical_card")
        self.setFixedSize(scale.scale_x(45),scale.scale_y(82))
        self.VCARD_LAYOUT = widgets.QVBoxLayout()
        self.setLayout(self.VCARD_LAYOUT)
        self.VCARD_LAYOUT.setSpacing(scale.scale_y(10))
        self.VCARD_LAYOUT.setContentsMargins(0,0,0,0)
        self.VCARD_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        self.TIME_LABEL = widgets.QLabel()
        self.TIME_LABEL.setFixedSize(scale.scale_x(45),scale.scale_y(19))
        self.TIME_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.TIME_LABEL.setStyleSheet("color: white; border-radius: 0px;background-color: transparent; font-family: 'Roboto'; font-weight: 500;")
        scale.setFontSize(self.TIME_LABEL,16)
        self.WEATHER_LABEL = widgets.QLabel()
        self.WEATHER_LABEL.setFixedSize(scale.scale_x(24),scale.scale_y(24))
        self.WEATHER_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        self.TEMPERATURE_LABEL = widgets.QLabel()
        self.TEMPERATURE_LABEL.setFixedSize(scale.scale_x(25),scale.scale_y(19))
        self.TEMPERATURE_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.TEMPERATURE_LABEL.setStyleSheet("color: white; border-radius: 0px;background-color: transparent; font-family: 'Roboto'; font-weight: 500;")
        scale.setFontSize(self.TEMPERATURE_LABEL,16)
        self.VCARD_LAYOUT.addWidget(self.TIME_LABEL,alignment= core.Qt.AlignmentFlag.AlignCenter )
        self.VCARD_LAYOUT.addWidget(self.WEATHER_LABEL,alignment= core.Qt.AlignmentFlag.AlignCenter)
        self.VCARD_LAYOUT.addWidget(self.TEMPERATURE_LABEL,alignment= core.Qt.AlignmentFlag.AlignCenter)
    
    
    
    
    
    
    
    
    
    
    
    

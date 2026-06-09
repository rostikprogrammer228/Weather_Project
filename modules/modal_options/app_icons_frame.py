import PyQt6.QtWidgets as widgets

class AppIcons(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setFixedSize(158,35)
        self.setStyleSheet("background-color: transparent")
        self.LAYOUT = widgets.QVBoxLayout()
        self.LAYOUT.setContentsMargins(8, 8, 0, 8)
        self.setLayout(self.LAYOUT)
        
        self.LABEL = widgets.QLabel(text = "Списки зображень")
        self.LABEL.setFixedWidth(150)
        self.LABEL.setStyleSheet("color: white; font-size: 16px; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        self.LAYOUT.addWidget(self.LABEL)
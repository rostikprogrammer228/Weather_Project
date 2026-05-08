import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui

class Header(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.setStyleSheet("background-color: white")
        self.setFixedSize(self.window().width(), 40)
        
        layout = widgets.QHBoxLayout()
        
        layout.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        
        self.setLayout(layout)
        
        close_button = widgets.QPushButton(parent = self)
        close_icon = gui.QIcon("media/title_bar/Close_Button_Hover.svg")
        close_button.setIcon(close_icon)
        close_button.setStyleSheet("border: none")

        layout.addWidget(close_button)
        
        close_button.clicked.connect(self.window().close)
        
        minimize_button = widgets.QPushButton(parent= self)
        minimize_icon = gui.QIcon("media/title_bar/Minimize_Button.svg")
        minimize_button.setIcon(minimize_icon)
        layout.addWidget(minimize_button)
        minimize_button.setStyleSheet("border: none")
        
        minimize_button.clicked.connect(self.window().showMinimized)
        
        
        max_button = widgets.QPushButton(parent = self)
        max_close_icon = gui.QIcon("media/title_bar/Maximize_Button_Hover.svg")
        max_button.setIcon(max_close_icon)
        layout.addWidget(max_button)
        max_button.setStyleSheet("border: none")
        
        max_button.clicked.connect(self.window().showMaximized)


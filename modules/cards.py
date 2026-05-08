import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core

class Cards(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("border-bottom: 1px solid #859892;")
        self.setFixedSize(315, 82)
        
        card_layout = widgets.QHBoxLayout()
        card_layout.setContentsMargins(0,0,0,0)
        
        self.setLayout(card_layout)

        frame1 = widgets.QFrame(parent = self)
        frame1.setFixedSize(105, 82)
        frame1.setStyleSheet("border: none;")
        
        frame1_layout = widgets.QVBoxLayout()
        frame1.setLayout(frame1_layout)
        
        fr1_label1 = widgets.QLabel(text = "Cityname", parent = frame1)
        fr1_label2 = widgets.QLabel(text ="Time", parent = frame1)
        fr1_label3 = widgets.QLabel(text = "Weather", parent = frame1)

        frame1_layout.addWidget(fr1_label1)
        frame1_layout.addWidget(fr1_label2)
        frame1_layout.addWidget(fr1_label3)
        

        frame2 = widgets.QFrame(parent = self)
        frame2.setFixedSize(105, 82)
        frame2.setStyleSheet("border: none;")
        
        frame2_layout = widgets.QVBoxLayout()
        frame2.setLayout(frame2_layout)
        
        fr2_label1 = widgets.QLabel(text = "Temperature", parent = frame2)
        fr2_label2 = widgets.QLabel(text = "Max, Min", parent = frame2)
        
        frame2_layout.addWidget(fr2_label1)
        frame2_layout.addWidget(fr2_label2)
        
        card_layout.addWidget(frame1)
        card_layout.addStretch(1)
        card_layout.addWidget(frame2)
        
        
        
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from utils import clear_layout,close_drop_menu
from utils import scale
from ..app import application
from ..cards import Cards
from utils import change_size
class AppSize(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("APPSIZE")
        self.CHOOSED = False
        self.MODAL_WINDOW = self.window().findChild(widgets.QWidget,"MODAL_WINDOW")
        self.setFixedSize(158,35)
        self.setStyleSheet("background-color: transparent")
        self.LAYOUT = widgets.QVBoxLayout()
        self.LAYOUT.setContentsMargins(8, 8, 0, 8)
        self.setLayout(self.LAYOUT)
        self.SIZE_TEXT = None
        self.BUTTON_GROUP = None
        self.LABEL1 = widgets.QLabel(text = "Розмір додакту")
        self.LABEL1.setFixedWidth(150)
        self.LABEL1.setStyleSheet("color: white;border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        scale.setFontSize(self.LABEL1,16)
        self.LAYOUT.addWidget(self.LABEL1)
        
    def create_frame(self):
        self.SETTINGS_LAYOUT = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT
        self.SETTINGS_FRAME = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT
        
        
        self.SETTINGS_LAYOUT.setContentsMargins(0, 0, scale.scale_x(305), scale.scale_y(359))
        self.SETTINGS_LAYOUT.setSpacing(0)
        
        self.language = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER").LANGUAGE
        if self.language == "Українська":
            self.choose_size_label = "Оберіть розмір додатку"
            self.save_button_label = "Зберегти"
        elif self.language == "English" :
            self.choose_size_label  = "Select app size"
            self.save_button_label = "Save"
        
        
        self.SIZE_FRAME = widgets.QFrame(parent = self.SETTINGS_FRAME)
        self.SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(219))
        self.SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        self.SETTINGS_LAYOUT.addWidget(self.SIZE_FRAME )
        
        self.SIZE_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SIZE_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.SIZE_FRAME_LAYOUT.setSpacing(scale.scale_y(24))
        self.SIZE_FRAME.setLayout(self.SIZE_FRAME_LAYOUT)

        self.CHOOSE_SIZE_LABEL = widgets.QLabel(text = self.choose_size_label)
        self.CHOOSE_SIZE_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.CHOOSE_SIZE_LABEL.setFixedSize(scale.scale_x(239), scale.scale_y(21))
        self.CHOOSE_SIZE_LABEL.setStyleSheet("color: white; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 400;")
        scale.setFontSize(self.CHOOSE_SIZE_LABEL,18)

        self.SIZE_FRAME_LAYOUT.addWidget(self.CHOOSE_SIZE_LABEL)

        
        self.LIST_OF_SIZE_FRAME = widgets.QFrame()
        self.LIST_OF_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(112))
        self.LIST_OF_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        self.SIZE_FRAME_LAYOUT.addWidget(self.LIST_OF_SIZE_FRAME)

        self.LIST_OF_SIZE_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.LIST_OF_SIZE_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.LIST_OF_SIZE_FRAME_LAYOUT.setSpacing(scale.scale_y(16))
        self.LIST_OF_SIZE_FRAME.setLayout(self.LIST_OF_SIZE_FRAME_LAYOUT)

        self.FIRST_SIZE_FRAME = widgets.QFrame(parent = self.LIST_OF_SIZE_FRAME)
        self.FIRST_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        self.FIRST_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        
        self.LIST_OF_SIZE_FRAME_LAYOUT.addWidget(self.FIRST_SIZE_FRAME)
        
        self.STYLESHEET = """
            QRadioButton {
                color: white;
                border-radius: 0px;
                background-color: transparent;
                font-family: Roboto;
                font-weight: 400;
            }

            QRadioButton::indicator {
                
                image: url(media/title_bar/additional_elements/idle_radiobutton.png)
            }

            QRadioButton::indicator:checked {
                
                image: url(media/title_bar/additional_elements/selected_radiobutton.png)
            }
            """
            
        self.FIRST_SIZE_BUTTON = widgets.QRadioButton(parent = self.FIRST_SIZE_FRAME, text = "1200x800")
        self.FIRST_SIZE_BUTTON.setStyleSheet(self.STYLESHEET)
        self.FIRST_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        scale.setFontSize(self.FIRST_SIZE_BUTTON,14)
        
        self.SECOND_SIZE_FRAME = widgets.QFrame(parent = self.LIST_OF_SIZE_FRAME)
        self.SECOND_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        self.SECOND_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        
        self.LIST_OF_SIZE_FRAME_LAYOUT.addWidget(self.SECOND_SIZE_FRAME)

        self.SECOND_SIZE_BUTTON = widgets.QRadioButton(parent = self.SECOND_SIZE_FRAME, text = "1440x1024")
        self.SECOND_SIZE_BUTTON.setStyleSheet(self.STYLESHEET)
        self.SECOND_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        scale.setFontSize(self.SECOND_SIZE_BUTTON,14)
        
        self.THIRD_SIZE_FRAME = widgets.QFrame(parent = self.LIST_OF_SIZE_FRAME)
        self.THIRD_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        self.THIRD_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        
        self.LIST_OF_SIZE_FRAME_LAYOUT.addWidget(self.THIRD_SIZE_FRAME)

        self.THIRD_SIZE_BUTTON = widgets.QRadioButton(parent = self.THIRD_SIZE_FRAME, text = "1512x982")
        self.THIRD_SIZE_BUTTON.setStyleSheet(self.STYLESHEET)
        self.THIRD_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        scale.setFontSize(self.THIRD_SIZE_BUTTON,14)
        
        self.FOURTH_SIZE_FRAME = widgets.QFrame(parent = self.LIST_OF_SIZE_FRAME)
        self.FOURTH_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        self.FOURTH_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        
        self.LIST_OF_SIZE_FRAME_LAYOUT.addWidget(self.FOURTH_SIZE_FRAME)

        self.FOURTH_SIZE_BUTTON = widgets.QRadioButton(parent = self.FOURTH_SIZE_FRAME, text = "1728x1117")
        self.FOURTH_SIZE_BUTTON.setStyleSheet(self.STYLESHEET)
        self.FOURTH_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        scale.setFontSize(self.FOURTH_SIZE_BUTTON,14)


        self.BUTTON_GROUP = widgets.QButtonGroup()
        self.BUTTON_GROUP.addButton(self.FIRST_SIZE_BUTTON)
        self.BUTTON_GROUP.addButton(self.SECOND_SIZE_BUTTON)
        self.BUTTON_GROUP.addButton(self.THIRD_SIZE_BUTTON)
        self.BUTTON_GROUP.addButton(self.FOURTH_SIZE_BUTTON)
        
        for button in self.BUTTON_GROUP.buttons():
            button.setChecked(button.text() == self.SIZE_TEXT)
        self.SAVE_BUTTON = widgets.QPushButton(self.SIZE_FRAME, text = self.save_button_label)
        window = self.window()
        self.SAVE_BUTTON.clicked.connect(lambda: change_size(window, False))
        self.SAVE_BUTTON.setFixedSize(scale.scale_x(105), scale.scale_y(38))
        self.SAVE_BUTTON.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px; color: white;font-family: 'Roboto'; font-weight: 400;")
        scale.setFontSize(self.SAVE_BUTTON,14)
        self.SIZE_FRAME_LAYOUT.addWidget(self.SAVE_BUTTON)
        
    
                
        
        
        
    def mousePressEvent(self, event):
        self.list_of_options_frames = self.MODAL_WINDOW.LIST_OF_OPTIONS_FRAMES
        if event.button() == core.Qt.MouseButton.LeftButton and self.CHOOSED == False:
            close_drop_menu(self.window())
            clear_layout(self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT)
            self.create_frame()
            for option in self.list_of_options_frames :
                if option.CHOOSED:
                    option.setStyleSheet("background-color: transparent; border-radius: 0px")
                    option.CHOOSED = False
            self.CHOOSED = True
            self.setStyleSheet("background-color : rgba(0,0,0,0.2); border-radius : 4px")
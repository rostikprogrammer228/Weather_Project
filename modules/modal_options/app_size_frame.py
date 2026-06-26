import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from utils import clear_layout,close_drop_menu
from utils import scale
from ..app import application
from ..cards import Cards

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
        self.SAVE_BUTTON.clicked.connect(self.change_size)
        self.SAVE_BUTTON.setFixedSize(scale.scale_x(105), scale.scale_y(38))
        self.SAVE_BUTTON.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px; color: white;font-family: 'Roboto'; font-weight: 400;")
        scale.setFontSize(self.SAVE_BUTTON,14)
        self.SIZE_FRAME_LAYOUT.addWidget(self.SAVE_BUTTON)
        
    def change_size(self):
        
        main_window = self.window()
        weather_container = main_window.findChild(widgets.QFrame, "WEATHER_CONTAINER")
        search_field = main_window.findChild(widgets.QLineEdit, "SEARCH_FIELD")
        search_city = main_window.findChild(widgets.QFrame, "SEARCHCITY")
        app_icons = main_window.findChild(widgets.QFrame, "APPICONS")
        app_language = main_window.findChild(widgets.QFrame, "APPLANGUAGE")
        country_menu = main_window.findChild(widgets.QFrame, "CONTRYMENU")
        city_menu = main_window.findChild(widgets.QFrame, "CITYMENU")
        modal_window = main_window.findChild(widgets.QWidget, "MODAL_WINDOW")
        search_frame = main_window.findChild(widgets.QFrame, "SEARCH_FRAME")
        left_container = main_window.findChild(widgets.QFrame, "Left_container")
        
        
        if self.BUTTON_GROUP.checkedButton():
            size_text = self.BUTTON_GROUP.checkedButton().text()
            self.SIZE_TEXT = size_text
            window_width, window_height = map(int, size_text.split("x"))
            screen = application.primaryScreen()
            screen_size = screen.size()
            screen_width = screen_size.width()
            screen_height = screen_size.height()
            center_x = (screen_width // 2) - (window_width // 2)
            center_y = (screen_height // 2) - (window_height // 2)

            main_window.setGeometry(center_x, center_y, window_width, window_height)
            
            scale.update_size(window_width,window_height)
            main_window.HEADER.setFixedSize(self.window().width(), 40)
            weather_container.setFixedSize(scale.scale_x(828), scale.scale_y(760))
            weather_container.WEATHER_CONTEINER_LAYOUT.setSpacing(scale.scale_y(20))
            weather_container.TOP_FRAME_LAYOUT.setSpacing(scale.scale_x(278))
            weather_container.TOP_SETTINGS_FRAME_LAYOUT.setSpacing(scale.scale_x(10))
            weather_container.TOP_ADD_SEARCH_FRAME_LAYOUT.setSpacing(scale.scale_x(10))
            weather_container.ADD_FRAME_LAYOUT.setContentsMargins(scale.scale_x(8),scale.scale_y(7),scale.scale_x(8),scale.scale_y(7))
            weather_container.ADD_FRAME_LAYOUT.setSpacing(scale.scale_x(7))
            weather_container.MAIN_FRAME_LAYOUT.setSpacing(scale.scale_y(10))
            weather_container.MOMENT_WEATHER_LAYOUT.setSpacing(scale.scale_x(10))
            weather_container.LEFT_MOMENT_LAYOUT.setSpacing(scale.scale_y(16))
            weather_container.LEFT_WEATHER_LAYOUT.setSpacing(scale.scale_x(8))
            weather_container.LEFT_WEATHER_LABLE_LAYOUT.setSpacing(scale.scale_x(7))
            weather_container.RIGHT_MOMENT_LAYOUT.setSpacing(scale.scale_y(16))
            weather_container.RIGHT_DATA_LAYOUT.setSpacing(scale.scale_x(116))
            weather_container.DAY_WEATHER_FRAME_LAYOUT.setContentsMargins(0,scale.scale_y(16),0,scale.scale_y(16))
            weather_container.DAY_WEATHER_FRAME_LAYOUT.setSpacing(scale.scale_y(16))
            weather_container.DAY_WEATHER_MAIN_SCROLL_FRAME_LAYOUT.setSpacing(scale.scale_x(24))
            weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT.setSpacing(scale.scale_x(17))
            weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT.setContentsMargins(0,0,scale.scale_x(16),0)
            weather_container.DIAGRAM_FRAME_LAYOUT.setContentsMargins(scale.scale_x(16),scale.scale_y(16),scale.scale_x(16),scale.scale_y(16))
            weather_container.MAIN_DIAGRAM_FRAME_LAYOUT.setSpacing(scale.scale_y(8))
            weather_container.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT.setSpacing(scale.scale_x(19))
            weather_container.FORECAST_DIAGRAM_ITSELF_LAYOUT.setContentsMargins(scale.scale_x(1),0,scale.scale_x(3),0)
            weather_container.FORECAST_DIAGRAM_ITSELF_LAYOUT.setSpacing(scale.scale_x(3))
            weather_container.TOP_FRAME.setFixedSize(scale.scale_x(790), scale.scale_y(36))
            weather_container.TOP_FRAME_LAYOUT.setSpacing(scale.scale_x(278))
            weather_container.TOP_SETTINGS_FRAME.setFixedSize(scale.scale_x(144), scale.scale_y(36))
            weather_container.TOP_SETTINGS_FRAME_BUTTON.setFixedSize(scale.scale_x(36), scale.scale_y(36))
            weather_container.TOP_SETTINGS_FRAME_BUTTON.setIconSize(core.QSize(scale.scale_x(16), scale.scale_y(16)))
            weather_container.TOP_SETTINGS_FRAME_LABEL.setFixedSize(scale.scale_x(98), scale.scale_y(20))
            scale.setFontSize(weather_container.TOP_SETTINGS_FRAME_LABEL,14)
            weather_container.TOP_ADD_SEARCH_FRAME.setFixedSize(scale.scale_x(368), scale.scale_y(36))
            weather_container.ADD_FRAME.setFixedSize(scale.scale_x(97), scale.scale_y(36))
            weather_container.ADD_BUTTON.setFixedSize(scale.scale_x(97), scale.scale_y(36))
            weather_container.ADD_BUTTON_ICON.setFixedSize(scale.scale_x(16), scale.scale_y(22))
            add_pixmap = gui.QPixmap(f"media/title_bar/additional_elements/plus_circle.png")
            if not add_pixmap.isNull():
                scaled_pixmap = add_pixmap.scaled(scale.scale_x(16), scale.scale_y(16), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                weather_container.ADD_BUTTON_ICON.setPixmap(scaled_pixmap)
            
            weather_container.ADD_BUTTON_LABEL.setFixedSize(scale.scale_x(58), scale.scale_y(22))
            scale.setFontSize(weather_container.ADD_BUTTON_LABEL,17)
            weather_container.MAIN_FRAME.setFixedSize(scale.scale_x(788), scale.scale_y(677))
            weather_container.MOMENT_WEATHER_FRAME.setFixedSize(scale.scale_x(788), scale.scale_y(303))
            weather_container.LEFT_MOMENT_FRAME.setFixedSize(scale.scale_x(390), scale.scale_y(303))
            weather_container.LEFT_MOMENT_TOP_FRAME.setFixedSize(scale.scale_x(358), scale.scale_y(27))
            weather_container.LEFT_CITY_LABEL.setFixedSize(scale.scale_x(390), scale.scale_y(52))
            scale.setFontSize(weather_container.LEFT_CITY_LABEL,44)
            weather_container.LEFT_WEATHER_FRAME.setFixedSize(scale.scale_x(197), scale.scale_y(87))
            weather_container.LEFT_WEATHER_ICON.setFixedSize(scale.scale_x(76), scale.scale_y(87))
            scale.setFontSize(weather_container.LEFT_WEATHER_LABEL,74)
            weather_container.LEFT_WEATHER_LABEL11.setFixedSize(scale.scale_x(25), scale.scale_y(65))
            scale.setFontSize(weather_container.LEFT_WEATHER_LABEL11,60)
            weather_container.LEFT_DESCRIPTION_FRAME.setFixedSize(scale.scale_x(259), scale.scale_y(57))
            weather_container.LEFT_DESCRIPTION_LABEL1.setFixedSize(scale.scale_x(259), scale.scale_y(28))
            scale.setFontSize(weather_container.LEFT_DESCRIPTION_LABEL1,24)
            weather_container.LEFT_DESCRIPTION_LABEL2.setFixedSize(scale.scale_x(259), scale.scale_y(19))
            scale.setFontSize(weather_container.LEFT_DESCRIPTION_LABEL2,16)
            weather_container.RIGHT_MOMENT_FRAME.setFixedSize(scale.scale_x(390), scale.scale_y(303))
            weather_container.RIGHT_TODAY_FRAME.setFixedSize(scale.scale_x(358), scale.scale_y(27))
            weather_container.RIGHT_TODAY_LABEL.setFixedSize(scale.scale_x(67), scale.scale_y(19))
            scale.setFontSize(weather_container.LEFT_DESCRIPTION_LABEL2,16)
            scale.setFontSize(weather_container.RIGHT_TODAY_LABEL,16)
            weather_container.RIGHT_DATA_FRAME.setFixedSize(scale.scale_x(358), scale.scale_y(44))
            weather_container.RIGHT_DATA_LABEL1.setFixedSize(scale.scale_x(123), scale.scale_y(28))
            scale.setFontSize(weather_container.RIGHT_DATA_LABEL1,24)
            weather_container.RIGHT_DATA_LABEL2.setFixedSize(scale.scale_x(123), scale.scale_y(28))
            scale.setFontSize(weather_container.RIGHT_DATA_LABEL2,24)
            weather_container.RIGHT_CLOCK_FRAME.setFixedSize(scale.scale_x(168), scale.scale_y(168))
            weather_container.RIGHT_CLOCK_LABEL.setFixedSize(scale.scale_x(74), scale.scale_y(34))
            scale.setFontSize(weather_container.RIGHT_CLOCK_LABEL,29)
            weather_container.DAY_WEATHER_FRAME.setFixedSize(scale.scale_x(788), scale.scale_y(157))
            weather_container.DAY_WEATHER_TOP_LABEL.setFixedSize(scale.scale_x(756), scale.scale_y(27))
            scale.setFontSize(weather_container.DAY_WEATHER_TOP_LABEL,16)
            weather_container.DAY_WEATHER_MAIN_SCROLL_FRAME.setFixedSize(scale.scale_x(756), scale.scale_y(82))
            weather_container.SCROLL_LEFT_BUTTON.setFixedSize(scale.scale_x(16), scale.scale_y(16))
            weather_container.SCROLL_RIGHT_BUTTON.setFixedSize(scale.scale_x(16), scale.scale_y(16))
            weather_container.DAY_WEATHER_SCROLL_PARENT.setFixedSize(scale.scale_x(656), scale.scale_y(82))
            weather_container.DAY_WEATHER_SCROLL_AREA.setFixedSize(scale.scale_x(656), scale.scale_y(82))
            weather_container.DIAGRAM_WEATHER_FRAME.setFixedSize(scale.scale_x(788), scale.scale_y(197))
            weather_container.MAIN_DIAGRAM_FRAME.setFixedSize(scale.scale_x(756), scale.scale_y(165))
            weather_container.DIAGRAM_LABEL.setFixedSize(scale.scale_x(756), scale.scale_y(27))
            scale.setFontSize(weather_container.DIAGRAM_LABEL,16)
            weather_container.FORECAST_DIAGRAM_FRAME.setFixedSize(scale.scale_x(758), scale.scale_y(130))
            weather_container.FORECAST_DIAGRAM_ICON_PARENT_FRAME.setFixedSize(scale.scale_x(758), scale.scale_y(20))
            weather_container.FORECAST_DIAGRAM_ICON_FRAME.setFixedSize(scale.scale_x(730), scale.scale_y(20))
            weather_container.FORECAST_DIAGRAM_ICON_PARENT_CORNER_FRAME.setFixedSize(scale.scale_x(32), scale.scale_y(20))
            weather_container.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME.setFixedSize(scale.scale_x(758), scale.scale_y(110))
            weather_container.FORECAST_DIAGRAM_ITSELF_FRAME.setFixedSize(scale.scale_x(728), scale.scale_y(110))
            weather_container.FORECAST_TEMPERATURE_ITSELF_FRAME.setFixedSize(scale.scale_x(27), scale.scale_y(110))
            weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL1.setFixedSize(scale.scale_x(27), scale.scale_y(14))
            scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL1,12)
            weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL2.setFixedSize(scale.scale_x(27), scale.scale_y(14))
            scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL2,12)
            weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL3.setFixedSize(scale.scale_x(27), scale.scale_y(14))
            scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL3,12)
            weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL4.setFixedSize(scale.scale_x(27), scale.scale_y(14))
            scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL4,12)
            weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL5.setFixedSize(scale.scale_x(27), scale.scale_y(14))
            scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL5,12)
            weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL6.setFixedSize(scale.scale_x(27), scale.scale_y(14))
            scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL6,12)
            weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL7.setFixedSize(scale.scale_x(27), scale.scale_y(14))
            scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL7,12)
            weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL8.setFixedSize(scale.scale_x(27), scale.scale_y(14))
            scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL8,12)
            
            central_widget = main_window.central_widget
            if central_widget:
                central_widget.setFixedSize(window_width, window_height)

            content_container = main_window.findChild(widgets.QFrame, "Content_container")
            if content_container:
                content_container.setFixedSize(window_width, window_height)

            for cardd in Cards.CARDS_LIST:
                if cardd:
                    cardd.CARD_LAYOUT.setContentsMargins(scale.scale_x(8),scale.scale_y(8),scale.scale_x(8),scale.scale_y(8))
                    cardd.setFixedSize(scale.scale_x(330), scale.scale_y(98))
                    cardd.FRAME1.setFixedSize(scale.scale_x(200), scale.scale_y(82))
                    cardd.FRAME1_LABEL1.setFixedSize(scale.scale_x(200), scale.scale_y(28))
                    scale.setFontSize(cardd.FRAME1_LABEL1,24)
                    cardd.FRAME1_LABEL2.setFixedSize(scale.scale_x(105), scale.scale_y(14))
                    scale.setFontSize(cardd.FRAME1_LABEL2,14)
                    cardd.FRAME1_LABEL3.setFixedSize(scale.scale_x(105), scale.scale_y(14))
                    scale.setFontSize(cardd.FRAME1_LABEL3,14)
                    cardd.FRAME2.setFixedSize(scale.scale_x(110), scale.scale_y(82))
                    cardd.FRAME22.setFixedSize(scale.scale_x(85), scale.scale_y(52))
                    cardd.FRAME2_LABEL1.setFixedHeight(scale.scale_y(52))
                    scale.setFontSize(cardd.FRAME2_LABEL1,44)
                    cardd.FRAME2_LABEL11.setFixedHeight(scale.scale_y(44))
                    scale.setFontSize(cardd.FRAME2_LABEL11,39)
                    cardd.FRAME2_LABEL2.setFixedSize(scale.scale_x(110), scale.scale_y(14))
                    scale.setFontSize(cardd.FRAME2_LABEL2,12)
                    

                    if cardd.SELECTED:
                        
                        weather_icons_pack = self.window().findChild(widgets.QFrame, "APPICONS").WEATHER_ICONS_PACK
                        pixmap = gui.QPixmap(f"media/title_bar/weather_icons/weather_icons_{weather_icons_pack}/{cardd.REQUEST_DATA["weather"][0]["icon"]}.png")
                        if not pixmap.isNull():
                            scaled = pixmap.scaled(scale.scale_x(76), scale.scale_y(76), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                            weather_container.LEFT_WEATHER_ICON.setPixmap(scaled)
                        self.CLOCK = gui.QPixmap(f"media/title_bar/clock.svg")
                        if not self.CLOCK.isNull():
                            scaled_pixmap = self.CLOCK.scaled(scale.scale_x(168), scale.scale_y(168), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                            weather_container.RIGHT_CLOCK_FRAME.setPixmap(scaled_pixmap)
                        if hasattr(cardd, "DIAGRAMM_LIST"):
                            for diagramm in cardd.DIAGRAMM_LIST:
                                diagramm.setFixedWidth(scale.scale_x(8))
                                diagramm.setFixedHeight(scale.scale_y(diagramm.base_height))
                        if cardd and hasattr(cardd, "SUNMOVE_CARDS_LIST"):
                            for sun_card in cardd.SUNMOVE_CARDS_LIST:
                                if sun_card:
                                    if sun_card:
                                        sun_card.setFixedSize(scale.scale_x(90), scale.scale_y(82))
                                        ###
                                        sun_card.TIME_LABEL.setFixedSize(scale.scale_x(90), scale.scale_y(19))
                                        scale.setFontSize(sun_card.TIME_LABEL,16)
                                        sun_card.ICON_LABEL.setFixedSize(scale.scale_x(90), scale.scale_y(24))
                                        
                                        if sun_card.TEXT_LABEL.text() == "Схід сонця" or sun_card.TEXT_LABEL.text() == "Sunrise":
                                            sun_pixmap = gui.QPixmap(f"media/title_bar/sunmove_icons/sunrise.png")
                                        elif sun_card.TEXT_LABEL.text() == "Захід сонця" or sun_card.TEXT_LABEL.text() == "Sunset":
                                            sun_pixmap = gui.QPixmap(f"media/title_bar/sunmove_icons/sunset.png")
                                        if not sun_pixmap.isNull():
                                            scaled_pixmap = sun_pixmap.scaled(scale.scale_x(24), scale.scale_y(24), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                                            sun_card.ICON_LABEL.setPixmap(scaled_pixmap)
                                        sun_card.TEXT_LABEL.setFixedSize(scale.scale_x(90), scale.scale_y(19))
                                        scale.setFontSize(sun_card.TEXT_LABEL,16)
                        if cardd and hasattr(cardd, "VERTICAL_CARD_LIST"):
                            for i, vert_card in enumerate(cardd.VERTICAL_CARD_LIST):
                                if not vert_card:
                                    continue

                                vert_card.setFixedSize(scale.scale_x(45), scale.scale_y(82))
                                vert_card.TIME_LABEL.setFixedSize(scale.scale_x(45), scale.scale_y(19))
                                scale.setFontSize(vert_card.TIME_LABEL, 16)

                                vert_card.WEATHER_LABEL.setFixedSize(scale.scale_x(24), scale.scale_y(24))

                                pixmap_scroll_card = gui.QPixmap(
                                    f"media/title_bar/scrollbar_weather_icons/"
                                    f"{vert_card.hour_data['weather'][0]['icon']}.png"
                                )

                                if not pixmap_scroll_card.isNull():
                                    scaled_pixmap = pixmap_scroll_card.scaled(
                                        scale.scale_x(24),
                                        scale.scale_y(24),
                                        core.Qt.AspectRatioMode.KeepAspectRatio,
                                        core.Qt.TransformationMode.SmoothTransformation
                                    )
                                    vert_card.WEATHER_LABEL.setPixmap(scaled_pixmap)

                                vert_card.TEMPERATURE_LABEL.setFixedSize(scale.scale_x(25), scale.scale_y(19))
                                scale.setFontSize(vert_card.TEMPERATURE_LABEL, 16)

                                # diagramm_icon отдельно
                                if i < len(cardd.DIAGRAMM_ICON_LIST):
                                    diagramm_icon = cardd.DIAGRAMM_ICON_LIST[i]

                                    diagramm_icon.setFixedSize(scale.scale_x(16), scale.scale_y(16))

                                    forecast_icon = gui.QPixmap(
                                        f"media/title_bar/scrollbar_weather_icons/"
                                        f"{vert_card.hour_data['weather'][0]['icon']}.png"
                                    )

                                    if not forecast_icon.isNull():
                                        scaled_pixmap = forecast_icon.scaled(
                                            scale.scale_x(16),
                                            scale.scale_y(16),
                                            core.Qt.AspectRatioMode.KeepAspectRatio,
                                            core.Qt.TransformationMode.SmoothTransformation
                                        )
                                        diagramm_icon.setPixmap(scaled_pixmap)
            
            if search_frame:
                search_frame.SEARCH_FRAME_LAYOUT.setContentsMargins(scale.scale_x(8),scale.scale_y(7),scale.scale_x(8),scale.scale_y(7))
                search_frame.setFixedSize(scale.scale_x(261), scale.scale_y(36))
                search_frame.SEARCH_LABEL.setFixedSize(scale.scale_x(25), scale.scale_y(22))
                search_pixmap = gui.QPixmap(f"media/title_bar/additional_elements/searcher.png")
                if not search_pixmap.isNull():
                    scaled_pixmap = search_pixmap.scaled(scale.scale_x(18),scale.scale_y(19), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                    search_frame.SEARCH_LABEL.setPixmap(scaled_pixmap)
                search_frame.CLEAR_BUTTON_FRAME.setFixedSize(scale.scale_x(20), scale.scale_y(20))
                search_frame.clear_button.setFixedSize(scale.scale_x(20), scale.scale_y(20))
                search_frame.clear_button.setIconSize(core.QSize(scale.scale_x(20),scale.scale_y(20)))
                
            if search_field:
                search_field.setFixedSize(scale.scale_x(200), scale.scale_y(22))
                search_field.DROP_DOWN_SCROLL_AREA.setFixedSize(scale.scale_x(261), scale.scale_y(200))
                search_field.DROP_DOWN_FRAME.setGeometry(scale.scale_x(918), scale.scale_y(55), scale.scale_x(261), scale.scale_y(200))
                search_field.DROP_DOWN_LAYOUT.setContentsMargins(scale.scale_x(7),scale.scale_y(5),0,scale.scale_y(5))
                scale.setFontSize(search_field,17)
            
            if modal_window:
                modal_window.MODAL_LAYOUT.setContentsMargins(scale.scale_x(24),scale.scale_y(24),scale.scale_x(24),scale.scale_y(24))
                modal_window.SETTINGS_CONTEINER_LEFT_LAYOUT.setContentsMargins(0,0,scale.scale_x(16),scale.scale_y(438))
                modal_window.setGeometry(scale.scale_x(391), scale.scale_y(66), scale.scale_x(790), scale.scale_y(688))
                modal_window.HEADER_FRAME.setFixedSize(scale.scale_x(742), scale.scale_y(28))
                modal_window.HEADER_FRAME_LAYOUT.setSpacing(scale.scale_x(550))
                modal_window.HEADER_FRAME_LABEL.setFixedSize(scale.scale_x(168), scale.scale_y(28))
                scale.setFontSize(modal_window.HEADER_FRAME_LABEL,24)
                modal_window.CLOSE_BUTTON.setFixedSize(scale.scale_x(24), scale.scale_y(24))
                modal_window.SETTINGS_CONTEINER.setFixedSize(scale.scale_x(742), scale.scale_y(578))
                modal_window.SETTINGS_CONTEINER_LEFT.setFixedSize(scale.scale_x(174), scale.scale_y(578))
                modal_window.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME.setFixedSize(scale.scale_x(158), scale.scale_y(140))
                modal_window.SETTINGS_CONTEINER_RIGHT.setFixedSize(scale.scale_x(544), scale.scale_y(578))
                modal_window.CLOSE_BUTTON.setIconSize(core.QSize(scale.scale_x(24), scale.scale_y(24)))
                
                
            if left_container:
                left_container.leftcontainer_layout.setContentsMargins(0, scale.scale_y(20), 0, 0)
                left_container.header_layout.setContentsMargins(0, scale.scale_y(10), scale.scale_x(20), scale.scale_y(10))
                left_container.setFixedSize(scale.scale_x(370), scale.scale_y(800))
                left_container.leftcontainer_header.setFixedSize(scale.scale_x(370), scale.scale_y(44))
                left_container.CHANGE_THEME_BUTTON.setFixedSize(scale.scale_x(54), scale.scale_y(24))
                left_container.scroll_area.setFixedWidth(scale.scale_x(370))
                left_container.CHANGE_THEME_BUTTON.setIconSize(left_container.CHANGE_THEME_BUTTON.size())
                
                
            if search_city:
                search_city.LAYOUT.setContentsMargins(scale.scale_x(8), scale.scale_y(8), 0, scale.scale_y(8))
                search_city.setFixedSize(scale.scale_x(158), scale.scale_y(35))
                search_city.LABEL.setFixedWidth(scale.scale_x(150))
                scale.setFontSize(search_city.LABEL,16)
                
                
                
            if self:
                self.LIST_OF_SIZE_FRAME_LAYOUT.setSpacing(scale.scale_y(16))
                self.LAYOUT.setContentsMargins(scale.scale_x(8), scale.scale_y(8), 0, scale.scale_y(8))
                self.SETTINGS_LAYOUT.setContentsMargins(0, 0, scale.scale_x(305), scale.scale_y(359))
                self.setFixedSize(scale.scale_x(158), scale.scale_y(35))
                self.LABEL1.setFixedWidth(scale.scale_x(150))
                scale.setFontSize(self.LABEL1,16)
                self.SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(219))
                self.CHOOSE_SIZE_LABEL.setFixedSize(scale.scale_x(239), scale.scale_y(21))
                scale.setFontSize(self.CHOOSE_SIZE_LABEL,18)
                self.LIST_OF_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(112))
                self.FIRST_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
                self.FIRST_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
                scale.setFontSize(self.FIRST_SIZE_BUTTON,14)
                self.SECOND_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
                self.SECOND_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
                scale.setFontSize(self.SECOND_SIZE_BUTTON,14)
                self.THIRD_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
                self.THIRD_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
                scale.setFontSize(self.THIRD_SIZE_BUTTON,14)
                self.FOURTH_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
                self.FOURTH_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
                scale.setFontSize(self.FOURTH_SIZE_BUTTON,14)
                self.SAVE_BUTTON.setFixedSize(scale.scale_x(105), scale.scale_y(38))
                scale.setFontSize(self.SAVE_BUTTON,14)
            
            if app_language:
                app_language.LAYOUT.setContentsMargins(scale.scale_x(8), scale.scale_y(8), 0, scale.scale_y(8))
                app_language.setFixedSize(scale.scale_x(158), scale.scale_y(35))        
                app_language.LABEL2.setFixedWidth(scale.scale_x(150))
                scale.setFontSize(app_language.LABEL2,16)
                
                
            if app_icons:
                app_icons.LAYOUT.setContentsMargins(scale.scale_x(8), scale.scale_y(8), 0, scale.scale_y(8))
                app_icons.setFixedSize(scale.scale_x(158), scale.scale_y(35))
                app_icons.LABEL3.setFixedWidth(scale.scale_x(150))
                scale.setFontSize(app_icons.LABEL3,16)
            
                
        
        
        
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
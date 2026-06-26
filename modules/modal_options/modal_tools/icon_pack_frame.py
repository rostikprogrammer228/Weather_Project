import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from utils import scale
class IconPackFrame(widgets.QFrame) :
    def __init__(self, parent, icon_pack,pack_number):
        
        super().__init__(parent)
        self.ICON_FRAME_LIST = []
        self.ICON_LIST = []
        self.PACK_SELECTED = True
        self.WEATHER_ICONS_PACK = icon_pack
        self.setFixedSize(scale.scale_x(490), scale.scale_y(136)) 
        if pack_number == 1 and not self.window().findChild(widgets.QFrame, "APPICONS").PACK_CHOOSED:
            self.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border-radius: 8px;")
        else:
            self.setStyleSheet("background-color : transparent")
        
        self.ICON_PACK_LAYOUT = widgets.QVBoxLayout()
        self.ICON_PACK_LAYOUT.setSpacing(scale.scale_y(13))
        self.ICON_PACK_LAYOUT.setContentsMargins(scale.scale_x(16), scale.scale_y(16), scale.scale_x(16), scale.scale_y(16))
        self.setLayout(self.ICON_PACK_LAYOUT)
        
        self.language = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER").LANGUAGE
        if self.language == "Українська":
            self.icons_list_label = f"Список зображень №{pack_number}"
            
        elif self.language == "English" :
            self.icons_list_label = f"List of images №{pack_number}"
            
        self.ICONS_LIST_LABEL = widgets.QLabel(parent = self, text = self.icons_list_label)
        self.ICONS_LIST_LABEL.setFixedSize(scale.scale_x(151), scale.scale_y(17))
        self.ICONS_LIST_LABEL.setStyleSheet("color: white;border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        scale.setFontSize(self.ICONS_LIST_LABEL,14)
        self.ICON_PACK_LAYOUT.addWidget(self.ICONS_LIST_LABEL, alignment = core.Qt.AlignmentFlag.AlignTop | core.Qt.AlignmentFlag.AlignLeft)
        self.ICONS_LIST_LABEL.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        
        self.PACK_FRAME = widgets.QFrame(parent = self)
        self.PACK_FRAME.setFixedSize(scale.scale_x(458), scale.scale_y(74))   
        self.PACK_FRAME.setStyleSheet("background-color : transparent")
        self.ICON_PACK_LAYOUT.addWidget(self.PACK_FRAME, alignment= core.Qt.AlignmentFlag.AlignCenter)
        self.PACK_FRAME.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        
        self.PACK_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.PACK_FRAME_LAYOUT.setSpacing(scale.scale_x(22))
        self.PACK_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.PACK_FRAME.setLayout(self.PACK_FRAME_LAYOUT)
        
        i = 1
        while i < 4:
            self.ICON_FRAME = widgets.QFrame(self.PACK_FRAME)
            self.ICON_FRAME.setStyleSheet("background-color: #6d6c67;")
            self.ICON_FRAME.setFixedSize(scale.scale_x(74), scale.scale_y(74))
            self.PACK_FRAME_LAYOUT.addWidget(self.ICON_FRAME)
            self.ICON_FRAME_LIST.append(self.ICON_FRAME)
            
            self.ICON_FRAME_LAYOUT = widgets.QHBoxLayout()
            self.ICON_FRAME_LAYOUT.setSpacing(0)
            self.ICON_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
            if i == 1 and icon_pack == "main" or i == 3:
                self.ICON_FRAME_LAYOUT.setContentsMargins(0, scale.scale_y(2), scale.scale_x(1), 0)

            if i == 1 and icon_pack == "additional":
                self.ICON_FRAME_LAYOUT.setContentsMargins(0, 0, scale.scale_x(1), 0)
            self.ICON_FRAME.setLayout(self.ICON_FRAME_LAYOUT)
            
            self.SETTINGS_WEATHER_ICON = widgets.QLabel(self.ICON_FRAME)
            self.SETTINGS_WEATHER_ICON.setFixedSize(scale.scale_x(61), scale.scale_y(61))
            self.SETTINGS_WEATHER_ICON.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
            self.ICON_LIST.append(self.SETTINGS_WEATHER_ICON )
            
            pixmap = gui.QPixmap(f"media/title_bar/weather_icons/weather_icons_{icon_pack}/0{i}d.png")
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(61, 61, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                self.SETTINGS_WEATHER_ICON.setPixmap(scaled_pixmap)
            self.ICON_FRAME_LAYOUT.addWidget(self.SETTINGS_WEATHER_ICON)
            self.SETTINGS_WEATHER_ICON.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
            self.ICON_FRAME.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
            i +=1 
        i = 1
        while i < 3:
            self.ICON_FRAME = widgets.QFrame(self.PACK_FRAME)
            self.ICON_FRAME.setStyleSheet("background-color: #6d6c67;")
            self.ICON_FRAME.setFixedSize(scale.scale_x(74), scale.scale_y(74))
            self.PACK_FRAME_LAYOUT.addWidget(self.ICON_FRAME)
            self.ICON_FRAME_LIST.append(self.ICON_FRAME)
            self.ICON_FRAME_LAYOUT = widgets.QHBoxLayout()
            self.ICON_FRAME_LAYOUT.setSpacing(0)
            self.ICON_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
            if i == 1 and  icon_pack == "main":
                self.ICON_FRAME_LAYOUT.setContentsMargins(0, 0, 0,scale.scale_y(2) )  
            
            if i == 1 and icon_pack == "additional":
                self.ICON_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0) 
            
            if i == 2 and icon_pack == "additional":
                self.ICON_FRAME_LAYOUT.setContentsMargins(0, 0, scale.scale_x(2), 1)
            self.ICON_FRAME.setLayout(self.ICON_FRAME_LAYOUT)
            
            self.SETTINGS_WEATHER_ICON = widgets.QLabel(self.ICON_FRAME)
            self.SETTINGS_WEATHER_ICON.setFixedSize(scale.scale_x(61), scale.scale_y(61))
            self.SETTINGS_WEATHER_ICON.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
            self.ICON_LIST.append(self.SETTINGS_WEATHER_ICON )
            pixmap = gui.QPixmap(f"media/title_bar/weather_icons/weather_icons_{icon_pack}/0{i}n.png")
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(61, 61, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                self.SETTINGS_WEATHER_ICON.setPixmap(scaled_pixmap)
            
            self.ICON_FRAME_LAYOUT.addWidget(self.SETTINGS_WEATHER_ICON)
            self.SETTINGS_WEATHER_ICON.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
            self.ICON_FRAME.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
            i +=1
    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton :
            pack_list = self.window().findChild(widgets.QFrame, "APPICONS").ICON_PACKS_LIST
            for pack in pack_list:
                if pack.PACK_SELECTED:
                    pack.setStyleSheet("background-color: transparent;")
                    pack.PACK_SELECTED = False

            self.setStyleSheet("background-color: rgba(0, 0, 0, 0.3);")
            self.PACK_SELECTED = True
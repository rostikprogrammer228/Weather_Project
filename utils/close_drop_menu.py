import PyQt6.QtWidgets as widgets



def close_drop_menu(main_window) :
    try :
        search_field = main_window.findChild(widgets.QLineEdit, "SEARCH_FIELD")
        if search_field and hasattr(search_field, 'DROP_DOWN_FRAME') and isinstance(search_field.DROP_DOWN_FRAME, widgets.QFrame):
            search_field.DROP_DOWN_FRAME.hide()
        country_modal = main_window.findChild(widgets.QFrame, "DROP_COUNTRY_MODAL")
        if country_modal and hasattr(country_modal, 'DROP_DOWN_FRAME') and isinstance(country_modal.DROP_DOWN_FRAME, widgets.QFrame):
            country_modal.DROP_DOWN_FRAME.hide()
            country_modal.DROP_DOWN_FRAME.DROP_MENU_SHOW = False
        city_modal = main_window.findChild(widgets.QFrame, "DROP_CITY_MODAL")
        if city_modal and hasattr(city_modal, 'DROP_DOWN_FRAME') and isinstance(city_modal.DROP_DOWN_FRAME, widgets.QFrame):
            city_modal.DROP_DOWN_FRAME.hide()
            city_modal.DROP_DOWN_FRAME.DROP_MENU_SHOW = False
    except :
        pass
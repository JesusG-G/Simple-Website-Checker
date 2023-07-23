from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
class MessageSuccessPopup(Popup):
    result_text = ObjectProperty()
    pass

class MessageErrorPopup(Popup):
    result_text = ObjectProperty()
    pass

class FileErrorPopup(Popup):
    pass

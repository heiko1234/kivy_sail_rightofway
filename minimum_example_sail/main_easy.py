from kivymd.uix.label import MDLabel
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        return MDLabel(text= "Hello Heiko!", halign= "center")

MainApp().run()
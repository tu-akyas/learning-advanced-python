import time
import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime("%Y%m%d-%H%M%S")
        filename = f"files/{current_time}-cam_capture.png"
        self.ids.camera.export_to_png(filename)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = filename
        self.stop()


class ImageScreen(Screen):
    def create_link(self):
        filepath = self.ids.img.source
        filesharer = FileSharer(filepath)
        url = filesharer.share()
        self.ids.link.text = url

    def copy_link(self):
        Clipboard.copy(self.ids.link.text)

    def open_link(self):
        webbrowser.open(self.ids.link.text)

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()

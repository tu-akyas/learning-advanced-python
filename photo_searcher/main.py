from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests


Builder.load_file('frontend.kv')


class DisplayScreen(Screen):
    def get_image_link(self):
        query = self.manager.current_screen.ids.user_query.text

        # Get Wikipedia page and get first image url for the query
        wiki_page = wikipedia.page(query)
        image_link = wiki_page.images[0]
        return image_link

    def download_image(self):
        # Download the image
        req = requests.get(self.get_image_link())
        download_path = 'files/searched_image.jpg'
        with open(download_path, 'wb') as file:
            file.write(req.content)
        return download_path

    def set_image(self):
        # Set the downloaded image path to Kivy image source
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import os

'----------------------------------------------------------------------------------------------------------------------'
' screens definition '
'----------------------------------------------------------------------------------------------------------------------'
kivy_file_path = os.path.abspath('epec.kv')
Builder.load_file(kivy_file_path)

'----------------------------------------------------------------------------------------------------------------------'
' screens initialisation '
'----------------------------------------------------------------------------------------------------------------------'


class InitialScreen(Screen):
    pass


class StatusScreen(Screen):
    pass


class ClientScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(InitialScreen(name = 'initial_screen'))
sm.add_widget(StatusScreen(name = 'status_screen'))
sm.add_widget(ClientScreen(name = 'client_screen'))


class EPECApp(App):
    def build(self):
        return sm


'----------------------------------------------------------------------------------------------------------------------'


if __name__ == '__main__':
    EPECApp().run()

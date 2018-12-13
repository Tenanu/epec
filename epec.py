import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

'----------------------------------------------------------------------------------------------------------------------'
' screens definition '
'----------------------------------------------------------------------------------------------------------------------'
Builder.load_string("""
<InitialScreen>:
    BoxLayout:
        Button:
            text:       'Status'
            on_press:   root.manager.current = 'status_screen'
            
        Button:
            text:       'Klienci'
            on_press:   root.manager.current = 'client_screen'

<StatusScreen>:
    BoxLayout:
        Button:
            text:       'Powrot'
            on_press:   root.manager.current = 'initial_screen'
            
<ClientScreen>:
    BoxLayout:
        Button:
            text:       'Powrot'
            on_press:   root.manager.current = 'initial_screen'
            
""")


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

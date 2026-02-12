from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HelloWorldApp(App):
    def build(self):
        # Create a simple layout with centered text
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        hello_label = Label(
            text='Hello World!',
            font_size='48sp',
            halign='center',
            valign='middle'
        )
        layout.add_widget(hello_label)
        return layout

if __name__ == '__main__':
    HelloWorldApp().run()

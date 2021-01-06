from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.app import StringProperty

class DynamicLabelsApp(App):
    name_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['AA', 'BB', 'CC', 'DD']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            temp_label.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        name = instance.id
        self.name_text = str(name)

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicLabelsApp().run()
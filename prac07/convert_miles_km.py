from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

class MilesToKmApp(App):
    result = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, input):
        mile = self.handle_valid(input)
        kilometer = mile * 1.609
        self.result = str(kilometer)

    def handle_increment(self, input, increment):
        mile = self.handle_valid(input) + increment
        self.root.ids.input_miles.text = str(mile)

    def handle_valid(input):
        try:
            return float(input)
        except:
            return 0.0


MilesToKmApp().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('main.kv')

class DevCalc(Widget):
    pass


class DevCalcApp(App):

    def build(self):
        return DevCalc()

    def dec_process(self):

        decimal = self.root.ids.dec.text
        hexdec = self.root.ids.hex.text
        octal = self.root.ids.oct.text
        binary = self.root.ids.bin.text
        
        try:
            self.root.ids.hex.text = ('{0:x}'.format(int(int(decimal)))).upper()
            self.root.ids.oct.text = ('{0:o}'.format(int(int(decimal))))
            self.root.ids.bin.text = ('{0:b}'.format(int(int(decimal))))
        
        except:
            self.root.ids.hex.text = ""
            self.root.ids.oct.text = ""
            self.root.ids.bin.text = ""

    def bin_process(self):
        decimal = self.root.ids.dec.text
        hexdec = self.root.ids.hex.text
        octal = self.root.ids.oct.text
        binary = self.root.ids.bin.text
        
        try:
            self.root.ids.dec.text = str(int(binary, 2))
            self.root.ids.hex.text = ('{0:x}'.format(int(int(self.root.ids.dec.text)))).upper()
            self.root.ids.oct.text = ('{0:o}'.format(int(int(self.root.ids.dec.text))))

        except:
            
            self.root.ids.hex.text = ""
            self.root.ids.oct.text = ""
            self.root.ids.dec.text = ""

    def hex_process(self):

        decimal = self.root.ids.dec.text
        hexdec = self.root.ids.hex.text
        octal = self.root.ids.oct.text
        binary = self.root.ids.bin.text
        
        try:

            self.root.ids.dec.text = str(int(hexdec, 16))
            self.root.ids.oct.text = ('{0:o}'.format(int(int(self.root.ids.dec.text))))
            self.root.ids.bin.text = ('{0:b}'.format(int(int(self.root.ids.dec.text))))

        except:

            self.root.ids.dec.text = ""
            self.root.ids.oct.text = ""
            self.root.ids.bin.text =""
    
    def oct_process(self):

        decimal = self.root.ids.dec.text
        hexdec = self.root.ids.hex.text
        octal = self.root.ids.oct.text
        binary = self.root.ids.bin.text
        
        try:

            self.root.ids.dec.text = str(int(octal, 8))
            self.root.ids.hex.text = ('{0:x}'.format(int(int(self.root.ids.dec.text)))).upper()
            self.root.ids.bin.text = ('{0:b}'.format(int(int(self.root.ids.dec.text))))
        
        except:

            self.root.ids.hex.text = ""
            self.root.ids.dec.text = ""
            self.root.ids.bin.text =""

if __name__ == "__main__":
    DevCalcApp().run()
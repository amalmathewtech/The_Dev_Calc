from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder

from kivy.core.window import Window
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

page_num = 1

KV = '''

BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "The Dev Calc"
    MDTabs:
        id: tabs
        Tab1:
            text: 'Base converter'
        Tab2:
            text: 'ASCII Table'
        
<Tab1>:
    
    MDTextField:
        id:dec
        pos_hint: {"x":0.10,"y":0.860}
        size_hint: (0.80,0.13)
        hint_text: 'Decimal number'
        on_text:root.dec_process()
    MDTextField:
        id:hex
        pos_hint: {"x":0.10,"y":0.760}
        size_hint: (0.80,0.13)
        hint_text: 'Hexadecimal number'
        on_text:root.hex_process()
    MDTextField:
        id:oct
        pos_hint: {"x":0.10,"y":0.660}
        size_hint: (0.80,0.13)
        hint_text: 'Octal number'
        on_text:root.oct_process()
    MDTextField:
        id:bin
        pos_hint: {"x":0.10,"y":0.460}
        size_hint: (0.80,0.20)
        hint_text: 'Binary number'
        multiline: True
        on_text:root.bin_process()
<Tab2>:

    Image:
        id:img
        source: '1.png'
        #size: self.texture_size
        allow_stretch:True
        keep_ratio:False
    MDIconButton:
        id:left
        icon: "arrow-left-bold"
        pos_hint:{'left': 1}
        user_font_size: "20sp"
        
        on_press:root.update('-')
    MDIconButton:
        id:right
        icon: "arrow-right-bold"
        pos_hint:{'right': 1}
        user_font_size: "20sp"
        on_press:root.update('+')
    
'''

class Tab1(FloatLayout, MDTabsBase):

    def dec_process(self):
        decimal = self.ids.dec.text
        hexdec = self.ids.hex.text
        octal = self.ids.oct.text
        binary = self.ids.bin.text

        try:
            self.ids.hex.text = ('{0:x}'.format(int(int(decimal)))).upper()
            self.ids.oct.text = ('{0:o}'.format(int(int(decimal))))
            self.ids.bin.text = ('{0:b}'.format(int(int(decimal))))

        except:
            self.ids.hex.text = ""
            self.ids.oct.text = ""
            self.ids.bin.text = ""

    def bin_process(self):
        decimal = self.ids.dec.text
        hexdec = self.ids.hex.text
        octal = self.ids.oct.text
        binary = self.ids.bin.text

        try:
            self.ids.dec.text = str(int(binary, 2))
            self.ids.hex.text = ('{0:x}'.format(int(int(self.ids.dec.text)))).upper()
            self.ids.oct.text = ('{0:o}'.format(int(int(self.ids.dec.text))))

        except:

            self.ids.hex.text = ""
            self.ids.oct.text = ""
            self.ids.dec.text = ""

    def hex_process(self):

        decimal = self.ids.dec.text
        hexdec = self.ids.hex.text
        octal = self.ids.oct.text
        binary = self.ids.bin.text

        try:

            self.ids.dec.text = str(int(hexdec, 16))
            self.ids.oct.text = ('{0:o}'.format(int(int(self.ids.dec.text))))
            self.ids.bin.text = ('{0:b}'.format(int(int(self.ids.dec.text))))


        except:

            self.ids.dec.text = ""
            self.ids.oct.text = ""
            self.ids.bin.text = ""

    def oct_process(self):

        decimal = self.ids.dec.text
        hexdec = self.ids.hex.text
        octal = self.ids.oct.text
        binary = self.ids.bin.text

        try:

            self.ids.dec.text = str(int(octal, 8))
            self.ids.hex.text = ('{0:x}'.format(int(int(self.ids.dec.text)))).upper()
            self.ids.bin.text = ('{0:b}'.format(int(int(self.ids.dec.text))))

        except:

            self.ids.hex.text = ""
            self.ids.dec.text = ""
            self.ids.bin.text = ""


class Tab2(FloatLayout, MDTabsBase):

    def update(self, text):
        global page_num
        if text == '-':
            page_num = page_num - 1
            if page_num == 0:
                page_num = 7
        if text == '+':
            page_num = page_num + 1
            if page_num > 7:
                page_num = 1
        self.ids.img.source = str(page_num) + ".png"


class DevCalcApp(MDApp):

    def build(self):
        return Builder.load_string(KV)


DevCalcApp().run()

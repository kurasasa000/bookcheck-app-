from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Fire Tablet 7 (第9世代) の画面サイズ
Window.size = (600, 1024)

class BookCheckApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        title = Label(
            text='書店 欠本チェックアプリ\nFire Tablet 7版',
            font_size='28sp',
            size_hint_y=0.2,
            halign='center'
        )
        title.bind(size=title.setter('text_size'))
        
        self.status = Label(
            text='準備完了\nタップしてテスト',
            font_size='20sp',
            size_hint_y=0.4,
            halign='center'
        )
        self.status.bind(size=self.status.setter('text_size'))
        
        btn = Button(
            text='動作テスト',
            font_size='24sp',
            size_hint_y=0.4,
            background_color=(0.2, 0.6, 1, 1)
        )
        
        btn.bind(on_press=self.on_test)
        
        layout.add_widget(title)
        layout.add_widget(self.status)
        layout.add_widget(btn)
        
        return layout
    
    def on_test(self, instance):
        self.status.text = 'Fire Tablet 7で\n正常に動作しています！'

if __name__ == '__main__':
    BookCheckApp().run()

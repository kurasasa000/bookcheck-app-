from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (600, 1024)

class BookCheckApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(
            text='書店 欠本チェックアプリ',
            font_size='32sp',
            size_hint_y=0.2
        )
        
        self.status = Label(
            text='準備完了 - Fire Tablet 7向け',
            font_size='24sp',
            size_hint_y=0.4
        )
        
        btn = Button(
            text='テスト',
            font_size='28sp',
            size_hint_y=0.4,
            background_color=(0.2, 0.6, 1, 1)
        )
        
        btn.bind(on_press=self.on_test)
        
        layout.add_widget(title)
        layout.add_widget(self.status)
        layout.add_widget(btn)
        
        return layout
    
    def on_test(self, instance):
        self.status.text = 'ボタンが押されました！\n動作確認OK'

if __name__ == '__main__':
    BookCheckApp().run()

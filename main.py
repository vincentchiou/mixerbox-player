import webview
import threading
import os
import webbrowser
import time

MIXERBOX_URL = 'https://www.mbplayer.com/list/10086761'

HTML = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html'), encoding='utf-8').read()

class Api:
    def play(self):
        def _start():
            webbrowser.open(MIXERBOX_URL)
            time.sleep(1)
            webview.windows[0].destroy()
        threading.Thread(target=_start, daemon=True).start()

window = webview.create_window(
    'MixerBox 一鍵播放器',
    html=HTML,
    js_api=Api(),
    width=400,
    height=540,
    resizable=False,
    text_select=False,
)

if __name__ == '__main__':
    webview.start(debug=False)

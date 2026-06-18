import webview
import threading
import os
import time

MIXERBOX_URL = 'https://www.mbplayer.com/list/10086761'

HTML = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html'), encoding='utf-8').read()

AUTO_CLICK_JS = """
(function() {
    function tryClick() {
        var btns = document.querySelectorAll('button');
        for (var i = 0; i < btns.length; i++) {
            if (btns[i].textContent.indexOf('隨機播放') !== -1) {
                btns[i].click();
                return true;
            }
        }
        return false;
    }
    if (!tryClick()) {
        var observer = new MutationObserver(function() {
            if (tryClick()) {
                observer.disconnect();
            }
        });
        observer.observe(document.body, { childList: true, subtree: true });
        setTimeout(function() { observer.disconnect(); }, 15000);
    }
})();
"""

class Api:
    def play(self):
        def _start():
            window = webview.windows[0]
            window.load_url(MIXERBOX_URL)
            time.sleep(4)
            for i in range(3):
                try:
                    window.evaluate_js(AUTO_CLICK_JS)
                except Exception:
                    pass
                time.sleep(2)
            window.minimize()
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

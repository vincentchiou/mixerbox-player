import webview
import threading
import os
import time
from webview.errors import JavascriptException

MIXERBOX_URL = 'https://www.mbplayer.com/list/10086761'

HTML = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, 'Segoe UI', 'Noto Sans TC', sans-serif;
  background: linear-gradient(145deg, #0f0f1a, #1a1a2e, #16213e);
  height: 100vh; display: flex; flex-direction: column;
  align-items: center; justify-content: center; color: #fff;
  overflow: hidden; user-select: none;
}
.logo {
  font-size: 42px; font-weight: 800;
  background: linear-gradient(135deg, #f7971e, #ffd200);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 4px;
}
.sub { font-size: 14px; color: rgba(255,255,255,0.4); margin-bottom: 40px; letter-spacing: 6px; }
.play-btn {
  width: 160px; height: 160px; border-radius: 50%;
  background: linear-gradient(145deg, #f7971e, #ffd200);
  border: none; cursor: pointer; position: relative;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 24px;
  box-shadow: 0 0 40px rgba(247,151,30,0.3);
  transition: all 0.3s ease;
}
.play-btn:hover { transform: scale(1.05); box-shadow: 0 0 60px rgba(247,151,30,0.5); }
.play-btn:active { transform: scale(0.95); }
.play-btn svg { width: 64px; height: 64px; fill: #1a1a2e; margin-left: 8px; }
.label { font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.9); margin-bottom: 2px; }
.desc { font-size: 13px; color: rgba(255,255,255,0.35); }
#status { margin-top: 28px; font-size: 13px; color: rgba(255,255,255,0.25); transition: 0.3s; }
#status.loading { color: #ffd200; }
</style>
</head>
<body>
<div style="text-align:center;padding:40px;">
<div class="logo">MixerBox</div>
<div class="sub">一 鍵 播 放 器</div>
<button class="play-btn" id="playBtn" onclick="onPlay()">
<svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
</button>
<div class="label">華語本週熱門排行</div>
<div class="desc">隨機播放 · 50 首歌曲</div>
<div id="status">點擊按鈕開始播放</div>
</div>
<script>
function onPlay() {
  var s = document.getElementById('status');
  s.textContent = '正在啟動…';
  s.className = 'loading';
  document.getElementById('playBtn').style.pointerEvents = 'none';
  if (window.pywebview && window.pywebview.api) {
    window.pywebview.api.play();
  }
}
</script>
</body>
</html>
"""

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
        var ob = new MutationObserver(function() {
            if (tryClick()) { ob.disconnect(); }
        });
        ob.observe(document.body, { childList: true, subtree: true });
        setTimeout(function() { ob.disconnect(); }, 15000);
    }
})();
"""

class Api:
    def play(self):
        def _start():
            time.sleep(0.3)
            win = webview.windows[0]
            win.load_url(MIXERBOX_URL)
            time.sleep(4)
            for _ in range(3):
                try:
                    win.evaluate_js(AUTO_CLICK_JS)
                except JavascriptException:
                    pass
                time.sleep(2)
            win.minimize()
        threading.Thread(target=_start, daemon=True).start()

window = webview.create_window(
    'MixerBox 一鍵播放器',
    html=HTML,
    js_api=Api(),
    width=400, height=520,
    resizable=False,
    text_select=False,
)

if __name__ == '__main__':
    webview.start(debug=False)

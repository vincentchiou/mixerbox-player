import tkinter as tk
import threading
import time

MIXERBOX_URL = 'https://www.mbplayer.com/list/10086761'

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

def run_webview():
    import webview
    from webview.errors import JavascriptException

    LOADING_HTML = '<html><body style="background:#0f0f1a;display:flex;align-items:center;justify-content:center;height:100vh;"><span style="color:#f7971e;font-family:sans-serif;font-size:20px;">載入 MixerBox...</span></body></html>'

    window = webview.create_window(
        'MixerBox', html=LOADING_HTML,
        width=1200, height=800,
    )

    def navigate():
        time.sleep(1)
        window.load_url(MIXERBOX_URL)
        time.sleep(5)
        for _ in range(4):
            try:
                window.evaluate_js(AUTO_CLICK_JS)
            except JavascriptException:
                pass
            time.sleep(2)
        window.minimize()

    threading.Thread(target=navigate, daemon=True).start()
    webview.start()

# --- tkinter splash (main thread) ---
root = tk.Tk()
root.title('MixerBox 一鍵播放器')
root.geometry('400x520+{}+{}'.format(
    (root.winfo_screenwidth()-400)//2,
    (root.winfo_screenheight()-520)//2
))
root.resizable(False, False)
root.configure(bg='#1a1a2e')

def on_play():
    root.destroy()          # 釋放主執行緒給 pywebview
    run_webview()           # 在主執行緒啟動 pywebview

tk.Label(root, text='MixerBox', font=('Segoe UI', 42, 'bold'),
         fg='#f7971e', bg='#1a1a2e').pack(pady=(50,0))
tk.Label(root, text='一 鍵 播 放 器', font=('Segoe UI', 11),
         fg='#888', bg='#1a1a2e').pack(pady=(4,36))

btn = tk.Button(root, text='▶', font=('Segoe UI', 40),
    fg='#1a1a2e', bg='#f7971e', activeforeground='#1a1a2e',
    activebackground='#ffd200', bd=0, cursor='hand2',
    width=4, height=2, command=on_play)
btn.pack(pady=16)

tk.Label(root, text='華語本週熱門排行', font=('Segoe UI', 14, 'bold'),
         fg='#eee', bg='#1a1a2e').pack(pady=(8,0))
tk.Label(root, text='隨機播放 · 50 首歌曲', font=('Segoe UI', 10),
         fg='#666', bg='#1a1a2e').pack(pady=(4,0))

root.mainloop()

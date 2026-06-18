import tkinter as tk
import webbrowser

MIXERBOX_URL = 'https://www.mbplayer.com/list/10086761'

def play():
    webbrowser.open(MIXERBOX_URL)
    root.iconify()

root = tk.Tk()
root.title('MixerBox 一鍵播放器')
root.geometry('400x540+{}+{}'.format(
    (root.winfo_screenwidth()-400)//2,
    (root.winfo_screenheight()-540)//2
))
root.resizable(False, False)
root.configure(bg='#1a1a2e')

tk.Label(
    root, text='MixerBox', font=('Segoe UI', 40, 'bold'),
    fg='#f7971e', bg='#1a1a2e'
).pack(pady=(60, 0))

tk.Label(
    root, text='一 鍵 播 放 器', font=('Segoe UI', 11),
    fg='#888', bg='#1a1a2e'
).pack(pady=(4, 40))

btn = tk.Button(
    root, text='▶', font=('Segoe UI', 40),
    fg='#1a1a2e', bg='#f7971e',
    activeforeground='#1a1a2e', activebackground='#ffd200',
    bd=0, cursor='hand2',
    width=4, height=2,
    command=play
)
btn.pack(pady=20)

tk.Label(
    root, text='華語本週熱門排行', font=('Segoe UI', 14, 'bold'),
    fg='#eee', bg='#1a1a2e'
).pack(pady=(10, 0))

tk.Label(
    root, text='隨機播放 · 50 首歌曲', font=('Segoe UI', 10),
    fg='#666', bg='#1a1a2e'
).pack(pady=(4, 0))

root.mainloop()

# MixerBox 一鍵播放器

一鍵開啟 MixerBox「華語本週熱門排行」的桌面啟動器。

## 功能

- 點一下金色按鈕，立刻在瀏覽器開啟 MixerBox 華語本週熱門排行
- 可直接點擊「隨機播放」開始聽歌
- 啟動器瞬間開啟、自動關閉，不佔畫面

## 使用方式

1. 雙擊 `run.bat`
2. 點擊金色播放按鈕
3. 瀏覽器自動開啟華語本週熱門排行，啟動器自動關閉

## 技術架構

- **語言**：Python 3（僅使用標準庫，無需安裝任何套件）
- **GUI 框架**：tkinter（Python 內建）
- **音樂來源**：[MixerBox OnePlayer](https://www.mbplayer.com/)

## 檔案結構

```
├── main.py         # 主程式（tkinter GUI）
├── launch.vbs      # 無聲啟動腳本（隱藏 cmd 視窗）
├── run.bat         # 一鍵啟動捷徑
└── index.html      # 備用（pywebview 時期保留）
```

## 開發者

邱老師 - 科技教育推廣

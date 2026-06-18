# MixerBox 一鍵播放器

一鍵播放 MixerBox「華語本週熱門排行」隨機播放的桌面應用程式。

## 功能

- 點擊一個按鈕，自動載入 MixerBox 華語本週熱門排行
- 自動點擊「隨機播放」，無需手動操作
- 播放後自動縮小到工具列，不佔畫面

## 使用方式

1. 雙擊 `run.bat`
2. 點擊金色播放按鈕
3. 自動載入歌單 → 自動隨機播放 → 縮小到工具列

## 技術架構

- **語言**：Python 3（tkinter + pywebview）
- **GUI 框架**：tkinter（瞬間啟動 UI）+ pywebview（WebView2 嵌入瀏覽器）
- **音樂來源**：[MixerBox OnePlayer](https://www.mbplayer.com/)

## 安裝需求

```bash
pip install pywebview
```

## 檔案結構

```
├── main.py         # 主程式（tkinter 啟動 → pywebview 接力）
├── launch.vbs      # 無聲啟動腳本（隱藏 cmd 視窗）
└── run.bat         # 一鍵啟動捷徑
```

## 啟動流程

```
run.bat → launch.vbs → tkinter(瞬間出現) → 點按鈕 → pywebview(自動播放+縮小)
```

## 開發者

邱老師 - 科技教育推廣

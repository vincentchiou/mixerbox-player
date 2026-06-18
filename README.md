# MixerBox 一鍵播放器

一鍵播放 MixerBox「華語本週熱門排行」隨機播放的桌面應用程式。

## 功能

- 點擊一個按鈕，立即播放 MixerBox 華語本週熱門排行
- 自動隨機播放 50 首熱門華語歌曲
- 播放後自動縮小到工具列，不佔畫面

## 使用方式

1. 雙擊 `run.bat`
2. 點擊金色播放按鈕
3. 自動載入歌單 → 自動隨機播放 → 縮小到工具列

## 技術架構

- **語言**：Python 3
- **GUI 框架**：pywebview（Windows WebView2）
- **音樂來源**：[MixerBox OnePlayer](https://www.mbplayer.com/)

## 安裝需求

```bash
pip install pywebview
```

## 檔案結構

```
├── main.py         # 主程式
├── index.html      # 啟動按鈕 UI
├── launch.vbs      # 無聲啟動腳本（隱藏 cmd）
├── run.bat         # 一鍵啟動捷徑
└── package.json    # Electron 保留設定（未使用）
```

## 開發者

邱老師 - 科技教育推廣

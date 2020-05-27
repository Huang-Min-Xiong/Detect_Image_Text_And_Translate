#### 安裝所需套件
`pip install -r requirements.txt`

#### 下載圖像辨識軟體 
Tesseract-OCR
- 下載位置:
`https://github.com/UB-Mannheim/tesseract/wiki`
- 下載檔案:
`tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe`
- 安裝路徑位置:
`C:\Program Files (x86)\Tesseract-OCR`
- 切換到安裝路徑位置:
`cd C:\Program Files (x86)\Tesseract-OCR`
- 確認是否安裝成功:
`tesseract -v`

#### 程式中需注意內容
- 設置tesseract.exe安裝路徑

`pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'`

#### 透過pytesseract套件來實作功能
- 辨識圖像中的文字並取出

#### 透過Translator套件來實作功能
- 將取出的文字翻譯成繁體字

- 最後將翻譯前與翻譯後的文字寫入txt檔中

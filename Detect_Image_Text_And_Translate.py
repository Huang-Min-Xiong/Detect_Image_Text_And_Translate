import easygui
from cv2 import cv2
import pytesseract
from googletrans import Translator

#tesseract.exe安裝路徑
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#選擇img檔案路徑
img_path = easygui.fileopenbox() 

#偵測圖像文字且翻譯文字
def Detect_image_text_and_translate():
    img=cv2.imread(img_path)
    text=pytesseract.image_to_string(img)
    print('翻譯前:\n'+str(text)+'\n')
    translator = Translator()
    Translation_Text=translator.translate(text,dest='zh-TW') #轉成繁體
    print('翻譯後:\n'+str(Translation_Text.text)+'\n')

    with open(r"Detect_Text\Detect_Text.txt","w") as f:
        f.write('翻譯前:\n'+str(text)+'\n\n') #翻譯前寫入文字檔
        f.write('翻譯後:\n'+str(Translation_Text.text)+'\n\n') #翻譯後寫入文字檔
        print('已寫入文字檔!')


#判斷是否已選擇Img路徑
if img_path==None:
    Open_img_path=False 
else:
    Open_img_path=True
    

#當選擇了Img路徑才執行功能    
if Open_img_path==True:
    Detect_image_text_and_translate()

#持續判斷使用者是否要繼續執行
while Open_img_path==False :
    print('尚未選擇Img路徑!')
    Input=input('若要繼續執行請輸入Y,不要則輸入N:\n')

    if Input=='y' or Input=='Y':
        img_path = easygui.fileopenbox() 
    else:
        exit  
        break
    
    


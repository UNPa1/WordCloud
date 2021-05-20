from wordcloud import WordCloud
from konlpy.utils import pprint
from konlpy.tag import Okt
from PIL import Image
import numpy as np
import sys

fwf=open("Word List.txt","a",encoding="UTF-8")
frf=open("Sentence.txt","r",encoding="UTF-8")
fr2f=open("Word List.txt","r",encoding="UTF-8")
mask=np.array(Image.open("image.png"))
Wstr = ""
okt=Okt()
isListReady = 0
while(1) :
    isListReady = int(input("\n1.워드클라우드 만들기\n2.워드 리스트 추가\n3.워드 리스트 지우기\n>>>"))
    if isListReady == 1 : #이미 존재하는 워드 리스트 사용
        Wstr = fr2f.read()
        break
    elif isListReady == 2 :
        text = okt.nouns(frf.read())
        for i in range(len(text)) : #분석한 문장를 워드클라우드에 맞게 변경
            if len(text[i]) != 1 :
                fwf.write(text[i] + " ")
                Wstr = Wstr + text[i] + " "
        sys.exit()
    elif isListReady == 3 : #워드 리스트 초기화
        fw2f=open("Word List.txt","w",encoding="UTF-8")
        fw2f.write("")
        fw2f.close()
    else : #프로그램 종료
        print("잘못된 번호입니다")
        
wordcloud = WordCloud(font_path='C:\\Users\\Adimin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\AppleSDGothicNeoL.ttf',
                      background_color='white',
                      height=1000,
                      width=1000,
                      random_state=32,
                      mask=mask,
                      colormap="twilight_r"
                      ) #워드클라우드 설정x
wordcloud.generate(Wstr)
wordcloud.to_file('asdf.png')
fwf.close()
frf.close()
fr2f.close()
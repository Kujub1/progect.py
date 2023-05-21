import pyautogui
import PyQt5
from PyQt5.QtWidgets import*
from bs4 import BeautifulSoup
import requests
import sys


url = 'http://horoshee.ru/?cat=4'
page = requests.get(url)

filteredNews = []
allNews = []

soup = BeautifulSoup(page.text, "html.parser")

allNews = str(soup.findAll('div', class_='entry'))

allNews=allNews.replace("\n","")
allNews=allNews.replace("</p></div>","")
allNews=allNews.replace("<br/>","")
allNews=allNews.replace("<p>","")
allNews=allNews.replace("]","")
allNews=allNews.replace("]","")
allNews=allNews.replace(",","")

filteredNews = allNews.split('<div class="entry">')


import random
test=random.choice(filteredNews)

txt = ''

for i in range(len(test)):
    if (i/32).is_integer() and i/8!=0:
        txt = txt + '\n'
    txt = txt + ' ' + test[i]
test=txt

app = QApplication([])
okno = QWidget()
okno.resize(900,800)
okno.setWindowTitle("Wish Everyone Peace")
line1 = QVBoxLayout()
okno.setLayout(line1)



text1 = QLabel(test)


print(test)
text33 = QLabel("Нажми на кнопку и получишь результат!!")
text33.setStyleSheet("QLabel{font-size:40px; color:green;}")
line1.addWidget(text33)
text1.setStyleSheet("QLabel{font-size:50px; color:green;}")
but1 = QPushButton("Если нету интернета")
line1.addWidget(but1)
but1.setStyleSheet('''QPushButton{font-size:100px; color:red; 
background:
 qlineargradient(x1:1 y1:0, x2:0 y2:0,stop:0 red, stop:1 blue);}''')
okno.setStyleSheet('''QWidget{
background-image: url("fonn.jpg");}
}''')

but2 = QPushButton("Если есть интернет!")
line1.addWidget(but2)
but2.setStyleSheet('''QPushButton{font-size:100px; color:red; 
background:
 qlineargradient(x1:1 y1:0, x2:0 y2:0,stop:0 red, stop:1 blue);}''')

vvod = QLabel(test)
vvod.setStyleSheet("QLabel{font-size:40px; color:purple;}")
line1.addWidget(vvod)

vvod2 = QLabel("121212")
line1.addWidget(vvod2)


def Wish():
    import random
    test=random.choice(filteredNews)
    txt=''
    for i in range(len(test)):
        if (i/32).is_integer() and i/8!=0:
            txt = txt + '\n'
        txt = txt + ' ' + test[i]
    test=txt
    vvod.setText(test)
 
def Otsebya():
    import random
    goodness = ["Удачи!", "Добра!", "Не грусти)", "У тебя все получиться"]
    test=random.choice(goodness)
  
    vvod.setText(test)
    
    
but1.clicked.connect(Otsebya)

but2.clicked.connect(Wish)










okno.show()
app.exec_()

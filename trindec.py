import pyautogui
import PyQt5
from PyQt5.QtWidgets import*
from bs4 import BeautifulSoup
import requests


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
#print(allNews)
filteredNews = allNews.split('<div class="entry">')


#print(filteredNews)   
#with pyautogui.hold('shift'):
    #pyautogui.press(['left', 'left', 'left'])
#pyautogui.write('Hello, World!', interval = 0.50)
app = QApplication([])
okno = QWidget()

line1 = QVBoxLayout()
okno.setLayout(line1)

import random
test =random.choice(filteredNews)
text1 = QLabel(test)#"Нажми на кнопку и получишь результат!!"
#line1.addWidget(text1)
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
line1.addWidget(vvod)

vvod2 = QLabel("121212")
line1.addWidget(vvod2)










okno.show()
app.exec_()

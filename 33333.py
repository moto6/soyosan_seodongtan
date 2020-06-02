
from PyQt5.QtWidgets import *
#15 day2 Final
from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()



app.setApplicationName("Login Screen")
win.resize(400,250)
bar = win.statusBar()
bar.showMessage("copyright(c) 2020 홍길동 All rights reserved")


#win.resize(300,300)
mb = win.menuBar()
menu = mb.addMenu('MENU')

menuAdd = QAction('LOGIN',win)
menuRemove = QAction('Cancel',win)
bye = QAction('EXIT',win)


menu.addAction(menuAdd)
menu.addAction(menuRemove)
mb.addAction(bye)


main = QWidget()
win.setCentralWidget(main)


addBtn = QPushButton("Login")
removeBtn = QPushButton("Cancel")

btnLayout = QHBoxLayout()
btnLayout.addWidget(addBtn)
btnLayout.addWidget(removeBtn)

form = QFormLayout()
name = QLineEdit()
form.addWidget(QLabel("Pleas, Insert your ID/PW"))
form.addRow("Account/ID",name)

#//pwform = QFormLayout()
pwname = QLineEdit()
#pwform.addWidget(QLabel("pwform"))
form.addRow("Password",pwname)

form.addRow(btnLayout)

main.setLayout(form)






#================
def add():
    print("LOGIN")
    #================
    str = name.text()
    if len(str) == 0:return

    global names
    if names.count(str) == 1:
        bar.showMessage("LOGIN")
    else:
        bar.showMessage("@#@#@#")
        names.append(str)
        print(names)
    #================

def remove():
    print("CANCLED")
    #================
    str = name.text()
    if len(str) == 0:return

    global names
    if names.count(str) == 0:
        bar.showMessage(str+",CANCLED!!!!")
    else: 
        bar.showMessage(str+",CANCLED@@@@")
        names.remove(str)
        print(names)
    #

def byebye():
    print("EXIT")
    quit()


names = ["inho","dongHun","cart","hwan"]
addBtn.clicked.connect(add)
removeBtn.clicked.connect(remove)

menuAdd.triggered.connect(add)
menuRemove.triggered.connect(remove)
bye.triggered.connect(byebye)
#


win.show()
app.exec()
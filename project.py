from PyQt5.QtWidgets import *
from PyQt5.uic import *
from sources import contains_symbol, contains_uppercase, contains_number, contains_lowercase, generate_password


def test():
    password = win.input.text()
    if(len(password) <= 8):
        password = win.erorr.setText("The string must have 8 characters or more.")
        password = win.good.setText("")
    elif not(contains_symbol(password)):
        password = win.erorr.setText("The string must contain at least one symbol.")
        password = win.good.setText("")
    elif not(contains_uppercase(password)):
        password = win.erorr.setText("The string must contain at least one uppercase character.")
        password = win.good.setText("")
    elif not(contains_lowercase(password)):
        password = win.erorr.setText("The string must contain at least one lowercase character.")
        password = win.good.setText("")
    elif not(contains_number(password)):
        password = win.erorr.setText("The string must contain at least one number.")
        password = win.good.setText("")
    else:
        password = win.erorr.setText("")
        password = win.good.setText("Strong password.")


def gener():
    password = generate_password()
    win.gener.setText(password)


app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.b1.clicked.connect(test)
win.b2.clicked.connect(gener)
app.exec_()

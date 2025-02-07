from PyQt5 import QtCore, QtGui, QtWidgets
from interfaceup import Ui_MainWindow
import sys


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
info  = ''

def click_one():
    global info
    info += '1'
    ui.info_text.setText(info)

def click_two():
    global info
    info += '2'
    ui.info_text.setText(info)
    
def click_three():
    global info
    info += '3'
    ui.info_text.setText(info)

def click_four():
    global info 
    info += '4'
    ui.info_text.setText(info)

def click_five():
    global info
    info += '5'
    ui.info_text.setText(info)

def click_six():
    global info
    info +='6'
    ui.info_text.setText(info)

def click_seven():
    global info
    info  +='7'
    ui.info_text.setText(info)

def click_eight():
    global info
    info += '8'
    ui.info_text.setText(info)

def click_nine():
    global info
    info +='9'
    ui.info_text.setText(info)

def click_zero():
    global info
    info += '0'
    ui.info_text.setText(info)

def plus():
    global info
    info += '+'
    ui.info_text.setText(info)

def minus():
    global info
    info += '-'
    ui.info_text.setText(info)

def multiplication():
    global info
    info += '*'
    ui.info_text.setText(info)

def division():
    global info
    info += '/'
    ui.info_text.setText(info)

def remove():
    global info
    info = ''
    ui.info_text.setText(info)

def equals():
    global info
    result = None
    try:
        result = eval(info)
        ui.info_text.setText(str(result))
    except:
        ui.info_text.setText(result)
    

def coma():
    global info
    info += '.'
    ui.info_text.setText(info)

def ckob_op():
    global info
    info += '('
    ui.info_text.setText(info)

def ckod_clos():
    global info
    info += ')'
    ui.info_text.setText(info)

def white():
    MainWindow.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
    ui.info_text.setStyleSheet("QLabel{\n"
"    background-color: white;\n"
"\n"
"}")
    ui.one_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.two_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"

"border: 2px solid black;"
"    border-radius: 8px;\n"
"border-color: black;"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.three_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"

"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.four_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"

"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.five_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.six_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.seven_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.eight_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.nine_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.zero_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.coma_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.multiplication_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.minus_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.plus_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;\n"
"border: 2px solid  black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.remove_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;\n"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.division_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;\n"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.equals_bt.setStyleSheet("QPushButton  {\n"
"    background-color: white;\n"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.white_theme.setStyleSheet("QPushButton  {\n"
"    background-color: white;\n"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.black_theme.setStyleSheet("QPushButton  {\n"
"    background-color: white;\n"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.skob_open.setStyleSheet("QPushButton  {\n"
"    background-color: white;\n"
"border: 2px  solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.skob_close.setStyleSheet("QPushButton  {\n"
"    background-color: white;\n"
"border: 2px solid black;"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"\n"
"\n"
"\n"
"}")
    ui.info_text.setStyleSheet("QLabel{\n"
"    background-color: white;"
"color: black;"
"border: 3px solid black;"
"\n"
"}")

def  black():
    MainWindow.setStyleSheet("QWidget {\n"
"    background-color: black;\n"
"}")
    ui.info_text.setStyleSheet("QLabel{\n"
"    background-color: black;"
"color: white;"
"border: 3px solid white"
"\n"
"}")
    ui.one_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.two_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.three_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.four_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.five_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.six_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.seven_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.eight_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.nine_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.zero_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.coma_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.multiplication_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.minus_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.plus_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.remove_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.division_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.equals_bt.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.white_theme.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.black_theme.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.skob_open.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")
    ui.skob_close.setStyleSheet("QPushButton  {\n"
"    background-color: orange;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"\n"
"\n"
"\n"
"}")

ui.two_bt.clicked.connect(click_two)
ui.one_bt.clicked.connect(click_one)
ui.three_bt.clicked.connect(click_three)
ui.four_bt.clicked.connect(click_four)
ui.five_bt.clicked.connect(click_five)
ui.six_bt.clicked.connect(click_six)
ui.seven_bt.clicked.connect(click_seven)
ui.eight_bt.clicked.connect(click_eight)
ui.nine_bt.clicked.connect(click_nine)
ui.zero_bt.clicked.connect(click_zero)
ui.remove_bt.clicked.connect(remove)
ui.plus_bt.clicked.connect(plus)
ui.minus_bt.clicked.connect(minus)
ui.multiplication_bt.clicked.connect(multiplication)
ui.equals_bt.clicked.connect(equals)
ui.coma_bt.clicked.connect(coma)
ui.division_bt.clicked.connect(division)
ui.skob_open.clicked.connect(ckob_op)
ui.skob_close.clicked.connect(ckod_clos)
ui.white_theme.clicked.connect(white)
ui.black_theme.clicked.connect(black)
sys.exit(app.exec_())
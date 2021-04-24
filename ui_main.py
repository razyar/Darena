import socket
import shutil
import select
import errno
import os
import sys
import PySide2
from PySide2 import *
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from shutil import copyfile

path = os.getcwd()
sys.path.append(path)
os.chdir(os.getcwd())




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        MainWindow.setMaximumSize(QtCore.QSize(750, 521))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("QPushButton {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:hover {\n"
"  \n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.Btn_Toggle.setText("")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_15.setGeometry(QtCore.QRect(320, 0, 61, 31))
        self.pushButton_15.setMinimumSize(QtCore.QSize(61, 31))
        self.pushButton_15.setMaximumSize(QtCore.QSize(61, 31))
        self.pushButton_15.setStyleSheet("\n"
"  border: 0px solid;\n"
"image: url(:/1/icons/header/Screenshot (22).png);\n"
"\n"
"")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 68))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"  border: 0px solid;\n"
"border-radius: 10px;\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/1/icons/menu/image.png);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(5, 5, 5);\n"
"}\n"
"")
        self.btn_page_3.setText("")
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget.addWidget(self.page_1)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 661, 391))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 661, 391))
        self.label_5.setStyleSheet("QLabel {\n"
"  color: rgb(255, 255, 255);\n"
"\n"
"    background-color: rgb(5, 5, 5);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"QLabel:hover {\n"
"    background-color: rgb(17, 17, 17);\n"
"}")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit.setGeometry(QtCore.QRect(0, 400, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"QFontDatabase::addApplicationFont(\":/fonts/bigjohnpro-bold.ttf\");\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(15, 15, 15);\n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(80)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 400, 31, 31))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"    image: url(:/1/icons/main/cil-cursor.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(15, 15, 15);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        self.pushButton.setGeometry(QtCore.QRect(580, 400, 31, 31))
        self.pushButton.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"  border: 0px solid;\n"
"    border-radius: 10px;\n"
"    image: url(:/1/icons/main/cil-paperclip.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(15, 15, 15);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Darena"))
    


    def client(self):
        HEADER_LENGTH = 10

        IP = "your server"
        PORT = 1234
        my_username = "razyar saeedian"


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        client_socket.connect((IP, PORT))
        print('connected')

        client_socket.setblocking(False)

        username = my_username.encode('utf-8')
        print('debug 1 passed')
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        print('debug 2 passed')
        client_socket.send(username_header + username)
        print('debug 3 passed')
        while self.lineEdit.text():
            try:
                
                message = self.lineEdit.text()
                f = open('data.kos', 'a')
                f.write("\n Me: "+ str(message))
                messages = QtCore.QFile("data.kos")
                if not messages.open(QtCore.QIODevice.ReadOnly):
                    QtGui.QMessageBox.information(None, 'info', messages.errorString())
                stream_messages = QtCore.QTextStream(messages)
                self.label_5.setText(stream_messages.readAll())
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                client_socket.send(message_header + message)
                self.lineEdit.setText("")
                client_socket.settimeout(0)
                break;
            except Exception as e:
                print('No new message', e)
            try:

                while True:


                    username_header = client_socket.recv(HEADER_LENGTH)


                    if not len(username_header):
                        print('Connection closed by the server')
                        sys.exit()


                    username_length = int(username_header.decode('utf-8').strip())


                    username = client_socket.recv(username_length).decode('utf-8')

                    message_header = client_socket.recv(HEADER_LENGTH)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = client_socket.recv(message_length).decode('utf-8')


                    print((f'{username} > {message}'))

            except IOError as e:

                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()


                continue

            except Exception as e:

                print('Reading error: '.format(str(e)))
                sys.exit()

    

    def file_selector(self):
        Tk().withdraw() 
        photo = askopenfilename()
        print('location: '+ photo)
        datapath = os.getcwd()
        os.chdir(datapath)
        photofile = open('photo.kos', 'w')
        photofile.write(photo)
        self.label.setStyleSheet("image: url(%s)};" % photo)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
        "image: url(%s);\n"
        "border: 0px solid;" % photo)


    def bio_edit(self):
        datapath = os.getcwd()
        os.chdir(datapath)
        bio = self.lineEdit_4.text()
        biofile = open('bio.kos', 'w')
        biofile.write(bio)
        biofile.close()



import qrc_rc


import os
from os import listdir
import time
import shutil
import sys
from PyQt5 import QtWidgets
from FotoScript import *
from PyQt5.QtWidgets import QMessageBox



def move():
    all_photo = sorted(listdir(file_path))
    count=1
    first_folder = 1
    photo_previos = ''
    for photo in all_photo:
        photo_presnt=photo

        if photo_previos=='':
            os.chdir(path_folders)
            os.mkdir(str(first_folder))
            os.chdir(str(first_folder))
            shutil.copy(str(file_path)+'/'+str(photo_presnt),str(photo_presnt))

        elif os.path.getmtime(str(file_path)+'/'+str(photo_presnt))-os.path.getmtime(str(file_path)+'/'+str(photo_previos))<=10 :
            shutil.copy(str(file_path) + '/' + str(photo_presnt),  str(photo_presnt))

        else:
            count+=1
            os.chdir(path_folders)
            os.mkdir(str(count))
            os.chdir(str(count))
            shutil.copy(str(file_path) + '/' + str(photo_presnt), str(photo_presnt))
        photo_previos = photo_presnt
    myLogText = 'Все успешно завершено'
    showInfoMsg(myLogText)


def showInfoMsg(mstring):
    info_msg.setInformativeText(mstring)
    info_msg.exec_()


def getDirectory():
    global file_path
    file_path = QtWidgets.QFileDialog.getExistingDirectory()
    ui.plainTextEdit_folder.setPlainText(format(file_path))

def getFolder():
    global path_folders
    path_folders = QtWidgets.QFileDialog.getExistingDirectory()
    ui.plainTextEdit_folder_2.setPlainText(format(path_folders))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

info_msg = QMessageBox()
info_msg.setIcon(QMessageBox.Information)
info_msg.setInformativeText('')
info_msg.setWindowTitle("Ход работы")

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.pushButton_folder.clicked.connect(getDirectory)
ui.pushButton_folder_2.clicked.connect(getFolder)
ui.pushButton.clicked.connect(move)

sys.exit(app.exec_())

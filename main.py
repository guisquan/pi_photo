# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 上午9:15
# @Author  : gui
# @File    : main.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from PyQt5.QtWidgets import QMainWindow
from UI.MainInterface import *

if __name__ == "__main__":
    """
    启动界面
    """
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

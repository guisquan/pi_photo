# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainInterface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Tools import *
import time
from multiprocessing import Process


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(301, 211)
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(40, 160, 80, 25))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(200, 160, 80, 25))
        self.stop.setObjectName("stop")
        self.frequency = QtWidgets.QLineEdit(Dialog)
        self.frequency.setGeometry(QtCore.QRect(120, 30, 51, 25))
        self.frequency.setObjectName("frequency")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 55, 21))
        self.label_2.setObjectName("label_2")
        self.times = QtWidgets.QLineEdit(Dialog)
        self.times.setGeometry(QtCore.QRect(120, 80, 51, 25))
        self.times.setText("")
        self.times.setObjectName("times")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 80, 41, 21))
        self.label_4.setObjectName("label_4")

        # 设置槽函数
        self.start.clicked.connect(self.start_action)
        self.stop.clicked.connect(self.stop_action)
        self.current_task = None

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start.setText(_translate("Dialog", "开始"))
        self.stop.setText(_translate("Dialog", "终止"))
        self.frequency.setText(_translate("Dialog", "30"))
        self.label.setText(_translate("Dialog", "频率"))
        self.label_2.setText(_translate("Dialog", "min"))
        self.times.setText(_translate("Dialog", "50"))
        self.label_4.setText(_translate("Dialog", "次数"))

    # 自定义槽函数
    def start_action(self):
        """
        开始拍摄任务
        :return:
        """
        if self.current_task is None or not self.current_task.is_alive():
            self.current_task = Process(target=self.photo_task)
            self.current_task.start()

    def stop_action(self):
        """
        结束拍摄任务
        :return:
        """
        if self.current_task is None:
            return
        if self.current_task.is_alive():
            try:
                self.current_task.kill()
                self.current_task.close()
            except Exception as e:
                print(e)
            finally:
                if self.current_task.is_alive():
                    print("still alive,pid is ", self.current_task.pid)
                print("stop photo task")

    def photo_task(self):
        """
        拍摄任务
        :return:
        """
        frequency = float(self.frequency.text())
        total_times = int(self.times.text())
        for i in range(total_times):
            take_photo_by_fswebcam("./tmp")
            time.sleep(int(frequency * 60))
            # time.sleep(5)

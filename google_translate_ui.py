# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './google_translate.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1006, 235)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icon/icon_form.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 981, 211))
        self.frame.setStyleSheet("background-color:#FFFFFF;\n"
"border: 2px solid white;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox_language_text = QtWidgets.QComboBox(self.frame)
        self.comboBox_language_text.setGeometry(QtCore.QRect(500, 20, 461, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_language_text.setFont(font)
        self.comboBox_language_text.setStyleSheet("background-color:#FFFFFF;\n"
"border-bottom: 2px solid #4284F3;\n"
"\n"
"")
        self.comboBox_language_text.setObjectName("comboBox_language_text")
        self.comboBox_language_text.addItem("")
        self.comboBox_language_text.setItemText(0, "")
        self.comboBox_language_text.addItem("")
        self.comboBox_list_language_translate = QtWidgets.QComboBox(self.frame)
        self.comboBox_list_language_translate.setGeometry(QtCore.QRect(10, 20, 461, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_list_language_translate.setFont(font)
        self.comboBox_list_language_translate.setStyleSheet("background-color:#FFFFFF;\n"
"border-bottom: 2px solid #4284F3;")
        self.comboBox_list_language_translate.setObjectName("comboBox_list_language_translate")
        self.plainTextEdit_text_translated = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_text_translated.setEnabled(False)
        self.plainTextEdit_text_translated.setGeometry(QtCore.QRect(10, 50, 461, 151))
        self.plainTextEdit_text_translated.setStyleSheet("background-color:#F5F5F5")
        self.plainTextEdit_text_translated.setObjectName("plainTextEdit_text_translated")
        self.plainTextEdit_translate_text = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_translate_text.setGeometry(QtCore.QRect(500, 50, 461, 131))
        self.plainTextEdit_translate_text.setStyleSheet("background-color:#FFFFFF;border-top:1px solid #E0E0E0;")
        self.plainTextEdit_translate_text.setPlainText("")
        self.plainTextEdit_translate_text.setObjectName("plainTextEdit_translate_text")
        self.pushButton_clean = QtWidgets.QPushButton(self.frame)
        self.pushButton_clean.setGeometry(QtCore.QRect(475, 80, 20, 23))
        self.pushButton_clean.setStyleSheet("border:none")
        self.pushButton_clean.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icon/icon_clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clean.setIcon(icon1)
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.pushButton_copy = QtWidgets.QPushButton(self.frame)
        self.pushButton_copy.setGeometry(QtCore.QRect(20, 170, 21, 23))
        self.pushButton_copy.setStyleSheet("border:none")
        self.pushButton_copy.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\icon/icon_copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_copy.setIcon(icon2)
        self.pushButton_copy.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_copy.setObjectName("pushButton_copy")

        self.retranslateUi(Dialog)
        self.pushButton_copy.clicked.connect(self.plainTextEdit_text_translated.selectAll)
        self.pushButton_copy.clicked.connect(self.plainTextEdit_text_translated.copy)
        self.pushButton_clean.clicked.connect(self.plainTextEdit_text_translated.clear)
        self.pushButton_clean.clicked.connect(self.plainTextEdit_translate_text.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton_copy, self.pushButton_clean)
        Dialog.setTabOrder(self.pushButton_clean, self.plainTextEdit_translate_text)
        Dialog.setTabOrder(self.plainTextEdit_translate_text, self.comboBox_language_text)
        Dialog.setTabOrder(self.comboBox_language_text, self.comboBox_list_language_translate)
        Dialog.setTabOrder(self.comboBox_list_language_translate, self.plainTextEdit_text_translated)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Google Translate"))
        self.comboBox_language_text.setItemText(1, _translate("Dialog", "Auto"))

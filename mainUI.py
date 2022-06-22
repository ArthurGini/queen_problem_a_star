# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(310, 390, 61, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setObjectName("nextButton")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(20, 60, 461, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMaximumSize(QtCore.QSize(2000, 2000))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(144, 390, 61, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevButton.sizePolicy().hasHeightForWidth())
        self.prevButton.setSizePolicy(sizePolicy)
        self.prevButton.setObjectName("prevButton")

        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(40, 10, 411, 31))
        self.outputLabel.setTextFormat(QtCore.Qt.RichText)
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")

        self.runAStarButton = QtWidgets.QPushButton(self.centralwidget)
        self.runAStarButton.setGeometry(QtCore.QRect(540, 60, 121, 41))
        self.runAStarButton.setStyleSheet("")
        self.runAStarButton.setObjectName("runAStarButton")

        self.nQueenSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.nQueenSpinBox.setGeometry(QtCore.QRect(641, 10, 51, 22))
        self.nQueenSpinBox.setMinimum(4)
        self.nQueenSpinBox.setMaximum(100)
        self.nQueenSpinBox.setObjectName("nQueenSpinBox")
        self.nQueensLabel = QtWidgets.QLabel(self.centralwidget)
        self.nQueensLabel.setGeometry(QtCore.QRect(520, 10, 101, 21))
        self.nQueensLabel.setObjectName("nQueensLabel")
        self.stopastarButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopastarButton.setGeometry(QtCore.QRect(540, 110, 121, 31))
        self.stopastarButton.setObjectName("stopastarButton")
        self.imagecountLabel = QtWidgets.QLabel(self.centralwidget)
        self.imagecountLabel.setGeometry(QtCore.QRect(210, 390, 91, 20))
        self.imagecountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagecountLabel.setObjectName("imagecountLabel")

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(420, 392, 75, 51))
        self.resetButton.setObjectName("resetButton")

        self.autoTrace = QtWidgets.QPushButton(self.centralwidget)
        self.autoTrace.setGeometry(QtCore.QRect(10, 390, 91, 23))
        self.autoTrace.setObjectName("autoTrace")
        self.stopAutotrace = QtWidgets.QPushButton(self.centralwidget)
        self.stopAutotrace.setGeometry(QtCore.QRect(10, 420, 91, 23))
        self.stopAutotrace.setObjectName("stopAutotrace")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.imageLabel.setText(_translate("MainWindow", "<html><head /><body>	<p align=\"justify\"><span style=\" font-size:16pt; font-weight:600; text-decoration:			underline;\">Instrucoes:</span><span style=\" font-size:12pt; font-weight:600;\">:</span></p>	<p align=\"justify\"><span style=\" font-size:12pt; font-weight:300; text-decoration: bold;\"></span>1. Escolha a		quantidade de rainhas n.</p></body></html>"))
        self.prevButton.setText(_translate("MainWindow", "Prev"))
        self.outputLabel.setText(_translate("MainWindow", "Steps/Time"))
        self.runAStarButton.setText(_translate("MainWindow", "Run A*"))
        self.nQueensLabel.setText(_translate("MainWindow", "Choose N Queens"))
        self.stopastarButton.setText(_translate("MainWindow", "Stop"))
        self.imagecountLabel.setText(_translate("MainWindow", "Image Count"))
        self.resetButton.setText(_translate("MainWindow", "RESET"))
        self.autoTrace.setText(_translate("MainWindow", "Auto Trace"))
        self.stopAutotrace.setText(_translate("MainWindow", "Stop AutoTrace"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

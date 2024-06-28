# Form implementation generated from reading ui file 'QuanLyTaiKhoan.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

class Ui_Dialog(object):
    def __init__(self, main_window):
      self.main_window = main_window
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 695)
        Dialog.setStyleSheet("background-color: #D0F9FD;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(310, 10, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.tblDuLieu = QtWidgets.QTableView(parent=Dialog)
        self.tblDuLieu.setGeometry(QtCore.QRect(0, 220, 911, 481))
        self.tblDuLieu.setStyleSheet("background-color:white;\n"
"color:black;")
        self.tblDuLieu.setObjectName("tblDuLieu")
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 80, 911, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.btnQuayVe = QtWidgets.QPushButton(parent=Dialog)
        self.btnQuayVe.setGeometry(QtCore.QRect(850, 0, 61, 51))
        self.btnQuayVe.setStyleSheet("")
        self.btnQuayVe.setText("")
        self.btnQuayVe.setObjectName("btnQuayVe")
        self.Favicon = QtWidgets.QLabel(parent=Dialog)
        self.Favicon.setGeometry(QtCore.QRect(10, 10, 121, 71))
        self.Favicon.setText("")
        self.Favicon.setObjectName("Favicon")
        self.btnThemTaiKhoan = QtWidgets.QPushButton(parent=Dialog)
        self.btnThemTaiKhoan.setGeometry(QtCore.QRect(360, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnThemTaiKhoan.setFont(font)
        self.btnThemTaiKhoan.setObjectName("btnThemTaiKhoan")
        self.txtTimKiem = QtWidgets.QTextEdit(parent=Dialog)
        self.txtTimKiem.setGeometry(QtCore.QRect(150, 130, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.txtTimKiem.setFont(font)
        self.txtTimKiem.setObjectName("txtTimKiem")
        self.btnSuaTaiKhoan = QtWidgets.QPushButton(parent=Dialog)
        self.btnSuaTaiKhoan.setGeometry(QtCore.QRect(540, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnSuaTaiKhoan.setFont(font)
        self.btnSuaTaiKhoan.setObjectName("btnSuaTaiKhoan")
        self.btnXoaTaiKhoan = QtWidgets.QPushButton(parent=Dialog)
        self.btnXoaTaiKhoan.setGeometry(QtCore.QRect(720, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnXoaTaiKhoan.setFont(font)
        self.btnXoaTaiKhoan.setObjectName("btnXoaTaiKhoan")
        self.btnSearch = QtWidgets.QPushButton(parent=Dialog)
        self.btnSearch.setGeometry(QtCore.QRect(20, 120, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
#=============================CSS===============================================
        #CSS label
        self.label.setStyleSheet("""
                    color: #FF4500;
                    font-weight: bold;
                """)
        #CSS Favicon
        pixamp = QPixmap("../Access/Icon/favicon.jpg")
        self.Favicon.setPixmap(pixamp)
        self.Favicon.setScaledContents(True)
        #Icon Button
        self.btnQuayVe.setIcon(QIcon("../Access/Icon/back.png"))
        self.btnQuayVe.setIconSize(QSize(30, 30))
        self.btnSearch.setIcon(QIcon("../Access/Icon/search.png"))
        self.btnSearch.setIconSize(QSize(30, 30))
        self.btnThemTaiKhoan.setIcon(QIcon("../Access/Icon/plus.png"))
        self.btnThemTaiKhoan.setIconSize(QSize(30, 30))
        self.btnSuaTaiKhoan.setIcon(QIcon("../Access/Icon/update.png"))
        self.btnSuaTaiKhoan.setIconSize(QSize(30, 30))
        self.btnXoaTaiKhoan.setIcon(QIcon("../Access/Icon/delete.png"))
        self.btnXoaTaiKhoan.setIconSize(QSize(30, 30))

        #CSS Button
        self.btnSearch.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                              
                                        """)
        self.btnQuayVe.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 20px;
                                              
                                        """)
        self.btnThemTaiKhoan.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                              
                                        """)
        self.btnSuaTaiKhoan.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                              
                                        """)
        self.btnXoaTaiKhoan.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                              
                                        """)
        self.txtTimKiem.setPlaceholderText("Tìm Theo Tên, Quyền")
        self.txtTimKiem.setStyleSheet("""
                                              background-color: white;
                                              color: black;
                                        """)
#===============================SỰ KIỆN=========================================
        self.Dialog = Dialog
        self.btnQuayVe.clicked.connect(self.quayve)
#===============================HÀM=============================================
    def quayve(self):
      from UiAdmin import Ui_MainWindow
      self.main_window = QtWidgets.QMainWindow()  # tạo một instance mới của QMainWindow
      self.ui = Ui_MainWindow(self.main_window)  # truyền self.main_window như là MainWindow
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      self.Dialog.hide()





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Quản Lý Tài Khoản"))
        self.btnThemTaiKhoan.setText(_translate("Dialog", "Thêm Tài Khoản"))
        self.txtTimKiem.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnSuaTaiKhoan.setText(_translate("Dialog", "Sửa Tài Khoản"))
        self.btnXoaTaiKhoan.setText(_translate("Dialog", "Xóa Tài Khoản"))
        self.btnSearch.setText(_translate("Dialog", "Tìm Kiếm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())




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
        self.txtTimKiem = QtWidgets.QTextEdit(parent=Dialog)
        self.txtTimKiem.setGeometry(QtCore.QRect(240, 130, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.txtTimKiem.setFont(font)
        self.txtTimKiem.setObjectName("txtTimKiem")
        self.btnSuaTaiKhoan = QtWidgets.QPushButton(parent=Dialog)
        self.btnSuaTaiKhoan.setGeometry(QtCore.QRect(590, 120, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnSuaTaiKhoan.setFont(font)
        self.btnSuaTaiKhoan.setObjectName("btnSuaTaiKhoan")
        self.btnXoaTaiKhoan = QtWidgets.QPushButton(parent=Dialog)
        self.btnXoaTaiKhoan.setGeometry(QtCore.QRect(740, 120, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnXoaTaiKhoan.setFont(font)
        self.btnXoaTaiKhoan.setObjectName("btnXoaTaiKhoan")
        self.btnSearch = QtWidgets.QPushButton(parent=Dialog)
        self.btnSearch.setGeometry(QtCore.QRect(10, 120, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 140, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtTimKiem_2 = QtWidgets.QTextEdit(parent=Dialog)
        self.txtTimKiem_2.setGeometry(QtCore.QRect(430, 130, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.txtTimKiem_2.setFont(font)
        self.txtTimKiem_2.setObjectName("txtTimKiem_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
#========================= CSS=================================================
        #CSS Favicon
        pixamp = QPixmap("../Access/Icon/favicon.jpg")
        self.Favicon.setPixmap(pixamp)
        self.Favicon.setScaledContents(True)
        #CSS label
        self.label.setStyleSheet("""
                    color: #FF4500;
                    font-weight: bold;
                """)
        #CSS Icon cho Button
        self.btnQuayVe.setIcon(QIcon("../Access/Icon/back.png"))
        self.btnQuayVe.setIconSize(QSize(30,30))

        self.btnSuaTaiKhoan.setIcon(QIcon("../Access/Icon/update.png"))
        self.btnSuaTaiKhoan.setIconSize(QSize(30,30))
        self.btnXoaTaiKhoan.setIcon(QIcon("../Access/Icon/delete.png"))
        self.btnXoaTaiKhoan.setIconSize(QSize(30,30))
        self.btnSearch.setIcon(QIcon("../Access/Icon/search.png"))
        self.btnSearch.setIconSize(QSize(30,30))

        #CSS Button
        self.btnXoaTaiKhoan.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                              
                                        """)

        self.btnQuayVe.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 20px;
                                              
                                        """)
        self.btnSuaTaiKhoan.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                              
                                        """)
        self.btnSearch.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                              
                                        """)
        self.txtTimKiem.setStyleSheet("""
                                              background-color: white;
                                              color: black;
                                      """)
        self.txtTimKiem_2.setStyleSheet("""
                                              background-color: white;
                                              color: black;
                                      """)

        self.txtTimKiem.setPlaceholderText("Ngày/Tháng/Năm")
        self.txtTimKiem_2.setPlaceholderText("Ngày/Tháng/Năm")

#================================SỰ KIỆN======================================
        self.btnQuayVe.clicked.connect(self.quayve)
        self.Dialog = Dialog
#================================HÀM=========================================
    def quayve(self):
      from UiAdmin import Ui_MainWindow
      self.main_window = QtWidgets.QMainWindow()  # tạo một instance mới của QMainWindow
      self.ui = Ui_MainWindow(self.main_window)  # truyền self.main_window như là MainWindow
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      self.Dialog.hide()


#============================================================================
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Quản Lý Đơn Hàng"))
        self.txtTimKiem.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnSuaTaiKhoan.setText(_translate("Dialog", "Sửa Thông Tin"))
        self.btnXoaTaiKhoan.setText(_translate("Dialog", "Xóa Tài Khoản"))
        self.btnSearch.setText(_translate("Dialog", "Tìm Kiếm Đơn Hàng"))
        self.label_2.setText(_translate("Dialog", "Từ"))
        self.label_3.setText(_translate("Dialog", "Đến"))
        self.txtTimKiem_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

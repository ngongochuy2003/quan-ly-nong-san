# Form implementation generated from reading ui file 'LoginAdmin.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap


class Ui_Dialog(object):
    def __init__(self, main_window):
        self.main_window = main_window

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # Ẩn thanh thông báo Dialog
        Dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Dialog.resize(552, 367)
        Dialog.setFixedSize(552, 367)
        Dialog.setStyleSheet("background: #E0FFFF;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(140, 60, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.iconAccount = QtWidgets.QLabel(parent=Dialog)
        self.iconAccount.setGeometry(QtCore.QRect(130, 150, 21, 21))
        self.iconAccount.setObjectName("iconAccount")
        self.txtTaiKhoan = QtWidgets.QPlainTextEdit(parent=Dialog)
        self.txtTaiKhoan.setGeometry(QtCore.QRect(160, 140, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.txtTaiKhoan.setFont(font)
        self.txtTaiKhoan.setObjectName("txtTaiKhoan")
        self.btnDangNhap = QtWidgets.QPushButton(parent=Dialog)
        self.btnDangNhap.setGeometry(QtCore.QRect(200, 280, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDangNhap.setFont(font)
        self.btnDangNhap.setStyleSheet("")
        self.btnDangNhap.setObjectName("btnDangNhap")
        self.iconAccount_2 = QtWidgets.QLabel(parent=Dialog)
        self.iconAccount_2.setGeometry(QtCore.QRect(130, 220, 21, 21))
        self.iconAccount_2.setObjectName("iconAccount_2")
        self.txtMatKhau = QtWidgets.QPlainTextEdit(parent=Dialog)
        self.txtMatKhau.setGeometry(QtCore.QRect(160, 210, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.txtMatKhau.setFont(font)
        self.txtMatKhau.setObjectName("txtMatKhau")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #============================CSS===================================
        #CSS Label
        self.label.setStyleSheet("""
            color: #FF4500;
            font-weight: bold;
        """)
        print("thu lai")
        # CSS hai hình
        pixmapAccount = QPixmap("../Access/Icon/user-solid.svg")
        self.iconAccount.setPixmap(pixmapAccount)
        self.iconAccount.setScaledContents(True)

        pixmapPassword = QPixmap("../Access/Icon/password-solid.svg")
        self.iconAccount_2.setPixmap(pixmapPassword)
        self.iconAccount_2.setScaledContents(True)

        #CSS Vùng Nhập Liệu
        self.txtTaiKhoan.setStyleSheet("""
                background: white;
                border: 3px solid black;
                border-radius: 10px;  
            """)
        self.txtTaiKhoan.setPlaceholderText("Tài Khoản") #Tạo chữ giả

        self.txtMatKhau.setStyleSheet("""
                background: white;
                border: 3px solid black;
                border-radius: 10px;  
            """)
        self.txtMatKhau.setPlaceholderText("Mật Khẩu") #Tạo chữ giả

        #CSS Button
        self.btnDangNhap.setStyleSheet("""
                background-color: #000080;
                color: #FFFFFF;
                font-weight: bold;
                border-radius: 10px;
            """)

    #=========================SỰ KIỆN===================================
        self.Dialog = Dialog


    #===================================================================


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Đăng Nhập ADMIN"))
        self.iconAccount.setText(_translate("Dialog", "d"))
        self.btnDangNhap.setText(_translate("Dialog", "Đăng Nhập"))
        self.iconAccount_2.setText(_translate("Dialog", "d"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

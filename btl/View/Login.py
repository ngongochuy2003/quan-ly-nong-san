# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from LoginAdmin import Ui_Dialog as Ui_Dialog_Admin
from LoginUser import Ui_Dialog as Ui_Dialog_User


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        def __init__(self, MainWindow):
            pass
        Dialog.setObjectName("Dialog")

        Dialog.resize(834, 608)
        Dialog.setFixedSize(834, 608)
        Dialog.setStyleSheet("background: #E0FFFF;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnAdmin = QtWidgets.QPushButton(parent=Dialog)
        self.btnAdmin.setGeometry(QtCore.QRect(70, 330, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnAdmin.setFont(font)
        self.btnAdmin.setObjectName("btnAdmin")
        self.btnUser = QtWidgets.QPushButton(parent=Dialog)
        self.btnUser.setGeometry(QtCore.QRect(70, 440, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnUser.setFont(font)
        self.btnUser.setObjectName("btnUser")
        self.lbImage = QtWidgets.QLabel(parent=Dialog)
        self.lbImage.setGeometry(QtCore.QRect(330, 0, 501, 611))
        self.lbImage.setText("")
        self.lbImage.setObjectName("lbImage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    #========================= CSS=========================

        # Thêm hình ảnh vào giao diện
        pixamp = QPixmap("../Access/Images/CoHaiLua.png")
        self.lbImage.setPixmap(pixamp)
        self.lbImage.setScaledContents(True)

        #Thêm CSS cho label
        self.label.setStyleSheet("""
            color: #FF4500;
            font-weight: bold;
        """)

        self.label_2.setStyleSheet("""
            color: #FF4500;
            font-weight: bold;
        """)

        self.label_3.setStyleSheet("""
            color: #000080; 
            font-weight: bold;
        """)
        #Thêm CSS cho button
        self.btnAdmin.setStyleSheet("""
            background-color: #000080;
            color: #FFFFFF;
            font-weight: bold;
            border-radius: 10px;
        """)

        self.btnUser.setStyleSheet("""
            background-color: #000080;
            color: #FFFFFF;
            font-weight: bold;
            border-radius: 10px;
        """)

    #========================= Sự Kiện =========================
        self.Dialog = Dialog
        self.btnAdmin.clicked.connect(self.openLoginAdmin)
        self.btnUser.clicked.connect(self.openLoginUser)

    #========================= Hàm =========================
    def openLoginAdmin(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_Admin(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()

    def openLoginUser(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_User()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()







    #==================================================
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Cửa Hàng Nông Sản "))
        self.label_2.setText(_translate("Dialog", "Cô Hai Lúa"))
        self.label_3.setText(_translate("Dialog", "Chọn phương thức đăng nhập"))
        self.btnAdmin.setText(_translate("Dialog", "Sign in with ADMIN"))
        self.btnUser.setText(_translate("Dialog", "Sign in with USER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

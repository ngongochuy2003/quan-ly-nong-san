
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHeaderView

from Controller.DơnHangController import DonhangController


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
        self.btnQuayVe.setIconSize(QSize(30 ,30))
        self.btnSuaTaiKhoan.setIcon(QIcon("../Access/Icon/update.png"))
        self.btnSuaTaiKhoan.setIconSize(QSize(30 ,30))
        self.btnXoaTaiKhoan.setIcon(QIcon("../Access/Icon/delete.png"))
        self.btnXoaTaiKhoan.setIconSize(QSize(30 ,30))
        self.btnSearch.setIcon(QIcon("../Access/Icon/search.png"))
        self.btnSearch.setIconSize(QSize(30 ,30))

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
        self.tblDuLieu.doubleClicked.connect(self.hienthi)
        self.btnSearch.clicked.connect(self.search)
        self.btnSuaTaiKhoan.clicked.connect(self.suadonhang)
        self.btnXoaTaiKhoan.clicked.connect(self.xoadonhang)
        self.load_data()
        self.Dialog = Dialog
#================================HÀM=========================================
    def quayve(self):
      from View.UiAdmin import Ui_MainWindow
      self.main_window = QtWidgets.QMainWindow()  # tạo một instance mới của QMainWindow
      self.ui = Ui_MainWindow(self.main_window)  # truyền self.main_window như là MainWindow
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      self.Dialog.hide()

    def load_data(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID_Đơn Hàng', 'IDUser', 'Tên khách', 'SĐT', 'Tổng tiền'])
        controller = DonhangController()
        data = controller.getAllDonHang()
        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)
        self.tblDuLieu.setModel(model)
        self.tblDuLieu.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def hienthi(self):
        try:
            row = self.tblDuLieu.currentIndex().row()
            item = self.tblDuLieu.model().index(row, 0)

            if item is not None:
                idDonHang = self.tblDuLieu.model().data(item)
                controller = DonhangController()
                data = controller.loadctdh(idDonHang)
                if data:
                    model = QStandardItemModel()
                    model.setRowCount(len(data))
                    model.setColumnCount(7)
                    model.setHorizontalHeaderLabels(
                        ["ID", "ID Đơn Hàng", "ID Sản Phẩm", "Số Lượng", "Đơn Giá", "Thành Tiền", "Ngày bán"])
                    for i, nv in enumerate(data):
                        for j, data in enumerate(nv):
                            model.setItem(i, j, QStandardItem(str(data)))
                    self.tblDuLieu.setModel(model)

                else:
                    QtWidgets.QMessageBox.warning(self, "Thông báo", "Không có dữ liệu")
            else:
                print("No item selected.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search(self):
        if self.txtTimKiem.toPlainText().strip() != "" and self.txtTimKiem_2.toPlainText().strip() != "":
            try:
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(
                    ["ID", "ID Đơn Hàng", "ID Sản Phẩm", "Số Lượng", "Đơn Giá", "Thành Tiền", "Ngày bán"])
                controller = DonhangController()
                data = controller.searchChitiethoadon(self.txtTimKiem.toPlainText().strip(),
                                                       self.txtTimKiem_2.toPlainText().strip())
                if data:
                    for row in data:
                        items = [QStandardItem(str(field)) for field in row]
                        model.appendRow(items)
                    self.tblDuLieu.setModel(model)
                    self.tblDuLieu.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                else:
                    QtWidgets.QMessageBox.information(self.Dialog, "Thông báo", "Không tìm thấy dữ liệu.")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self.Dialog, "Lỗi", f"Đã xảy ra lỗi: {e}")
        else:
            QtWidgets.QMessageBox.warning(self.Dialog, "Thông báo", "Vui lòng nhập đầy đủ thông tin tìm kiếm.")
            self.load_data()

    def suadonhang(self):
        from Suadonhangmanager import Ui_Dialog as Ui_Suadonhangmanager
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Suadonhangmanager()
        self.ui.setupUi(self.window)
        self.window.show()

    def xoadonhang(self):
        row = self.tblDuLieu.currentIndex().row()
        if row != -1:  # Ensure a row is selected
            item = self.tblDuLieu.model().index(row, 0)
            idDonHang = self.tblDuLieu.model().data(item)  # Assuming the first column holds the ID
            checkctdh = DonhangController()
            check = checkctdh.checkdata(idDonHang) # Pass the ID, not the QModelIndex
            if check:
                controller = DonhangController()
                controller.deleteDonHang(idDonHang)
                QtWidgets.QMessageBox.information(self.Dialog, "Thông báo", "Xoá đơn hàng thành công")
                self.load_data()
            else:
                QtWidgets.QMessageBox.warning(self.Dialog, "Thông báo", "Bạn cần xoá chi tiết đơn hàng này trước")
        else:
            QtWidgets.QMessageBox.warning(self.Dialog, "Thông báo", "Vui lòng chọn đơn hàng cần xoá")


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
        self.btnSuaTaiKhoan.setText(_translate("Dialog", "Sửa Đơn Hàng"))
        self.btnXoaTaiKhoan.setText(_translate("Dialog", "Xoá Đơn Hàng"))
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

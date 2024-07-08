
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMessageBox, QHeaderView
from View.Ui_QuanLyTaiKhoan import Ui_Dialog
from Controller.TaiKhoanController import TaiKhoanController

class QuanLyTaiKhoan(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setupEvents()
        self.load_data()


    def setupEvents(self):
        self.ui.btnQuayVe.clicked.connect(self.quayve)
        self.ui.btnSuaTaiKhoan.clicked.connect(self.openSuaTaiKhoan)
        self.ui.btnThemTaiKhoan.clicked.connect(self.openThemTaiKhoan)
        self.ui.tblDuLieu.clicked.connect(self.row_clicked)
        self.ui.btnXoaTaiKhoan.clicked.connect(self.deleteTaiKhoan)
        self.ui.btnSearch.clicked.connect(self.searchTaiKhoan)

    def load_data(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID_USER', 'UserName', 'PassWord', 'Role'])
        controller = TaiKhoanController()
        data = controller.getAllTaiKhoan()
        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)
        self.ui.tblDuLieu.setModel(model)
        self.ui.tblDuLieu.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def quayve(self):
        from View.UiAdmin import Ui_MainWindow
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        self.hide()

    def openSuaTaiKhoan(self):
        from View.SuaTaiKhoan import Ui_Dialog as Ui_Dialog_SuaTaiKhoan
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_SuaTaiKhoan()
        self.ui.setupUi(self.window)
        self.window.show()
        self.hide()

    def openThemTaiKhoan(self):
        from View.ThemTaiKhoan import Ui_Dialog as Ui_Dialog_ThemTaiKhoan
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_ThemTaiKhoan()
        self.ui.setupUi(self.window)
        self.window.show()
        self.hide()

    def row_double_clicked(self, index):
        username = self.ui.tblDuLieu.model().index(index.row(), 1).data()
        controller = TaiKhoanController()
        thongtin = controller.getThongTinByUserName(username)
        if not thongtin:
            QMessageBox.information(self, "Thông báo", "Không có thông tin nhân viên trên Database")
        else:
            from View.ChiTietThongTinNhanVien import Ui_Dialog as Ui_Dialog_ChiTietThongTinNhanVien
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog_ChiTietThongTinNhanVien()
            self.ui.setupUi(self.window)
            self.window.show()
            self.hide()

    def row_clicked(self, index):
        global selected_row_data
        selected_row_data = []
        for i in range(self.ui.tblDuLieu.model().columnCount()):
            selected_row_data.append(self.ui.tblDuLieu.model().index(index.row(), i).data())

    def deleteTaiKhoan(self):
        index = self.ui.tblDuLieu.currentIndex()
        if index.row() >= 0:  # Ensure there is a row selected
            selected_row_data = []
            for i in range(self.ui.tblDuLieu.model().columnCount()):
                selected_row_data.append(self.ui.tblDuLieu.model().index(index.row(), i).data())
            confirm = QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xóa tài khoản này không?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                id = selected_row_data[0]
                controller = TaiKhoanController()
                controller.deleteTaikhoan(id)
                QMessageBox.information(self, "Thông báo", "Xóa tài khoản thành công")
                self.load_data()

    def searchTaiKhoan(self):
        keyword = self.ui.txtTimKiem.toPlainText()
        controller = TaiKhoanController()
        data = controller.searchByUsername(keyword) if keyword.isalpha() else controller.searchByRole(keyword)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID_USER', 'UserName', 'PassWord', 'Role'])
        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)
        self.ui.tblDuLieu.setModel(model)
        self.ui.tblDuLieu.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = QuanLyTaiKhoan()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

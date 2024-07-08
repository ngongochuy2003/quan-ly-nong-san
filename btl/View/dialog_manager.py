from PyQt6 import QtWidgets


def openLoginAdmin(main_window):
    from View.LoginAdmin import Ui_Dialog as Ui_Dialog_Admin
    window = QtWidgets.QDialog()
    ui = Ui_Dialog_Admin(window)
    ui.setupUi(window)
    window.show()
    main_window.hide()

def openLoginUser(main_window):
    from View.LoginUser import Ui_Dialog as Ui_Dialog_User
    window = QtWidgets.QDialog()
    ui = Ui_Dialog_User(window)
    ui.setupUi(window)
    window.show()
    main_window.hide()

def openLogin(main_window):
    from Login import Ui_Dialog as Ui_Dialog_Login
    window = QtWidgets.QDialog()
    ui = Ui_Dialog_Login(window)
    ui.setupUi(window)
    window.show()
    main_window.hide()

def openNhaCungCap(self):
    from QuanLyNhaCungCap import Ui_Dialog as Ui_Dialog_NhaCungCap
    self.window = QtWidgets.QDialog()
    self.ui = Ui_Dialog_NhaCungCap(self.window)
    self.ui.setupUi(self.window)
    self.window.show()
    self.MainWindow.hide()

def openThongKe(self):
    from ThongKeDoanhThu import Ui_Dialog as Ui_Dialog_ThongKe
    self.window = QtWidgets.QDialog()
    self.ui = Ui_Dialog_ThongKe(self.window)
    self.ui.setupUi(self.window)
    self.window.show()
    self.MainWindow.hide()

def openSanPham(self):
    from QuanLySanPham import Ui_Dialog as Ui_Dialog_SanPham
    self.window = QtWidgets.QDialog()  # tạo một instance mới của QDialog chỉ khi nó chưa tồn tại
    self.ui = Ui_Dialog_SanPham(self.window)
    self.ui.setupUi(self.window)
    self.window.show()
    self.MainWindow.hide()

def openDonHang(self):
    from QuanLyDonHang import Ui_Dialog as Ui_Dialog_DonHang
    self.window = QtWidgets.QDialog()
    self.ui = Ui_Dialog_DonHang(self.window)
    self.ui.setupUi(self.window)
    self.window.show()
    self.MainWindow.hide()

def openTaiKhoan(self):
    from QuanLyTaiKhoan import Ui_Dialog as Ui_Dialog_TaiKhoan
    self.window = QtWidgets.QDialog()
    self.ui = Ui_Dialog_TaiKhoan(self.window)
    self.ui.setupUi(self.window)
    self.window.show()
    self.MainWindow.hide()

def quayve(self):
    from View.UiAdmin import Ui_MainWindow
    self.main_window = QtWidgets.QMainWindow()  # tạo một instance mới của QMainWindow
    self.ui = Ui_MainWindow(self.main_window)  # truyền self.main_window như là MainWindow
    self.ui.setupUi(self.main_window)
    self.main_window.show()
    self.Dialog.hide()
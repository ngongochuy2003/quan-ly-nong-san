def load_data(self):
    #Tạo model
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(['ID_USER', 'UserName', 'PassWord', 'Role'])
    #Tạo controller
    controller = TaiKhoanController()
    #Lấy dữ liệu
    data  = controller.getAllTaiKhoan()
    #Duyệt dữ liệu
    for row in data:
        items = [QStandardItem(str(field)) for field in row]
        model.appendRow(items)
    #Hiển thị dữ liệu
    self.tblDuLieu.setModel(model)
    # Điều chỉnh kích thước cột và hàng phù hợp với nội dung
    # self.tblDuLieu.resizeColumnsToContents()
    # self.tblDuLieu.resizeRowsToContents()

    # Điều chỉnh tất cả các cột để có độ rộng bằng nhau và chiếm đủ chiều rộng của bảng
    (self.tblDuLieu.horizontalHeader().setSectionResizeMode
     (QHeaderView.ResizeMode.Stretch))


def quayve(self):
    from View.UiAdmin import Ui_MainWindow
    self.main_window = QtWidgets.QMainWindow()  # tạo một instance mới của QMainWindow
    self.ui = Ui_MainWindow(self.main_window)  # truyền self.main_window như là MainWindow
    self.ui.setupUi(self.main_window)
    self.main_window.show()
    self.Dialog.hide()

def openSuaTaiKhoan(self):
    from View.SuaTaiKhoan import Ui_Dialog as Ui_Dialog_SuaTaiKhoan
    self.window = QtWidgets.QDialog()
    self.ui = Ui_Dialog_SuaTaiKhoan(self.window)
    self.ui.setupUi(self.window)
    self.window.show()
    self.Dialog.hide()
    # Truyền dữ liệu từ selected_row_data vào các trường nhập liệu
    global selected_row_data
    self.ui.txtTaiKhoan.setText(selected_row_data[0])
    self.ui.txtTaiKhoan_2.setText(selected_row_data[1])
    self.ui.txtMatKhau.setText(selected_row_data[2])
    self.ui.txtRole.setText(selected_row_data[3])

def openThemTaiKhoan(self):
    from ThemTaiKhoan import Ui_Dialog as Ui_Dialog_ThemTaiKhoan
    self.window = QtWidgets.QDialog()
    self.ui = Ui_Dialog_ThemTaiKhoan(self.window)
    self.ui.setupUi(self.window)
    self.window.show()
    self.Dialog.hide()

def row_double_clicked(self, index):
    username = self.tblDuLieu.model().index(index.row(), 1).data()
    controller = TaiKhoanController()
    thongtin = controller.getThongTinByUserName(username)
    print(thongtin)
    if not thongtin:
        QMessageBox.information(self.Dialog, "Thông báo",
                                "Không có thông tin nhân viên trên Database")
    else:
        thongtin = controller.getAllThongTin()
        print(thongtin)
        from View.ChiTietThongTinNhanVien import (Ui_Dialog as
                                                  Ui_Dialog_ChiTietThongTinNhanVien)
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_ChiTietThongTinNhanVien(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.Dialog.hide()
        # Load dữ liệu từ thongtin vào các trường txtID, txtHoVaTen, txtTuoi, txtEmail, txtDiaChi, txtSoDienThoai
        for info in thongtin:
            if info[1] == username:  # Sử dụng chỉ số thay vì tên trường
                self.ui.txtID.setText(str(info[0]))  # iduser
                self.ui.txtHoVaTen.setText(info[1])  # hoten
                self.ui.txtTuoi.setText(str(info[2]))  # tuoi
                self.ui.txtEmail.setText(info[3])  # email
                self.ui.txtDiaChi.setText(info[4])  # diachi
                self.ui.txtSoDienThoai.setText(info[5])  # sdt
                break




def row_clicked(self, index):
    global selected_row_data
    selected_row_data = []
    for i in range(self.tblDuLieu.model().columnCount()):
        selected_row_data.append(self.tblDuLieu.model().index(index.row(), i).data())

def deleteTaiKhoan(self):
    selected_row_data = []
    index = self.tblDuLieu.currentIndex()
    for i in range(self.tblDuLieu.model().columnCount()):
        selected_row_data.append(self.tblDuLieu.model().index(index.row(), i).data())
    confirm = QMessageBox.question(self.Dialog, "Xác nhận", "Bạn có chắc chắn muốn xóa tài khoản này không?",
                                   QMessageBox.StandardButton.Yes |
                                   QMessageBox.StandardButton.No )
    if confirm == QMessageBox.StandardButton.Yes:
        id = selected_row_data[0]
        controller = TaiKhoanController()
        controller.deleteTaikhoan(id)
        QMessageBox.information(self.Dialog, "Thông báo", "Xóa tài khoản thành công")
        self.load_data()


def searchTaiKhoan(self):
    keyword = self.txtTimKiem.toPlainText()
    controller = TaiKhoanController()
    data = []
    if keyword.isalpha():
        data = controller.searchByUsername(keyword)
    else:
        data = controller.searchByRole(keyword)
    if data:
        QMessageBox.information(self.Dialog, "Thông báo", "Tìm thấy dữ liệu")
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID_USER', 'UserName', 'PassWord', 'Role'])
        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)
        self.tblDuLieu.setModel(model)
        (self.tblDuLieu.horizontalHeader().setSectionResizeMode
         (QHeaderView.ResizeMode.Stretch))
    else:
        QMessageBox.information(self.Dialog, "Thông báo", "Không tìm thấy dữ liệu")
        self.load_data()
    #==============================================================================
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
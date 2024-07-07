from Controller.TaiKhoanController import TaiKhoanController
from Dao.TaiKhoanDao import TaiKhoanDao
from Controller.DơnHangController import DonhangController
from Dao.DonHangDao import DonhangDao
# def test_updateTaiKhoan(id, username, password, role):
#     controller = TaiKhoanController()
#     controller.updateTaiKhoan(id, username, password, role)
#     updated_account = controller.getTaiKhoanById(id)  # assuming this method exists
#     return updated_account[1] == username and updated_account[2] == password and updated_account[3] == role
#
# def test_commit_after_update(id, username, password, role):
#     controller = TaiKhoanController()
#     controller.updateTaiKhoan(id, username, password, role)
#     dao = TaiKhoanDao()
#     cursor = dao.db.get_connection().cursor()
#     cursor.execute("SELECT UserName, PassWord, Role FROM taikhoan WHERE ID_USER = %s", (id,))
#     updated_account = cursor.fetchone()
#     return updated_account[0] == username and updated_account[1] == password and updated_account[2] == role
#
# def test_adđonhang(iduser):
#     controller = DonhangController()
#     controller.addDonHang(iduser)
#     added_order = controller.getDonHangById(iduser)  # assuming this method exists
#     return added_order[1] == iduser
#
# test_adđonhang(2)
# print(test_updateTaiKhoan(5, 'daohuy', 'daohuy2003', '3'))  # replace with your test values
# # print(test_commit_after_update(1, 'new_username', 'new_password', 'new_role'))  # replace with your test values
def update (id,iddonhang, idsanpham, soluong, dongia):
    controller = DonhangController()
    controller.updateChiTietDonHang(iddonhang, idsanpham, soluong, dongia,id)
update(1,1,1,2,20000)
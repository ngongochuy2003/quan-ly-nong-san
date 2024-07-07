from Dao.TaiKhoanDao import TaiKhoanDao

class TaiKhoanController:
  def __init__(self):
    self.dao = TaiKhoanDao()

  def getAllTaiKhoan(self):
    return self.dao.getAllTaiKhoan()

  def updateTaiKhoan(self, id, username, password, role):
    return self.dao.updateTaiKhoan(id, username, password, role)

  def addTaiKhoan(self, username, password, role):
    return self.dao.addTaiKhoan(username, password, role)

  def deleteTaikhoan(self, id):
    return self.dao.deleteTaikhoan(id)

  def searchByUsername(self, username):
    return self.dao.searchByUsername(username)

  def searchByRole(self, role):
    return self.dao.searchByRole(role)

  def getThongTinByUserName(self, username):
    result = self.dao.getThongTinByUserName(username)
    print(result)  # In ra kết quả
    return result

  def getAllThongTin(self):
    return self.dao.getAllThongTin()

  def updateThongTin(self, iduser, hoten, tuoi, email, diachi, sdt):
    return self.dao.updateThongTin(iduser, hoten, tuoi, email, diachi, sdt)

  def addThongTinChiTietNhanVien(self, iduser, hoten, tuoi, email, diachi, sdt):
    return self.dao.addThongTinChiTietNhanVien(iduser, hoten, tuoi, email, diachi, sdt)
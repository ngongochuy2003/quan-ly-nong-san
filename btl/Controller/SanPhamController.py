import Dao.SanPhamDao as SanPhamDao

class SanPhamController:
  def __init__(self):
    self.sanpham_dao = SanPhamDao.SanPhamDao()

  def getAllSanPham(self):
    return self.sanpham_dao.getAllSanPham()

  def addSanPham(self, idsanpham, soluong, tensanpham, dongia, idnhacungcap):
    self.sanpham_dao.addSanPham(idsanpham, soluong, tensanpham, dongia, idnhacungcap)

  def updateSanPham(self, idsanpham, soluong, tensanpham, dongia, idnhacungcap):
    self.sanpham_dao.updateSanPham(idsanpham, soluong, tensanpham, dongia, idnhacungcap)

  def deleteSanPham(self, idsanpham):
    self.sanpham_dao.deleteSanPham(idsanpham)

  def searchById(self, idsanpham):
    return self.sanpham_dao.searchById(idsanpham)

  def getAllChiTietSanPham(self):
    return self.sanpham_dao.getAllChiTietSanPham()

  def updateChiTietSanPham(self, idsanpham, ngaynhapkho, hansudung, loai):
    self.sanpham_dao.updateChiTietSanPham(idsanpham, ngaynhapkho, hansudung, loai)
  def insertChiTietSanPham(self, idsanpham, ngaynhapkho, hansudung, loai):
    self.sanpham_dao.insertChiTietSanPham(idsanpham, ngaynhapkho, hansudung, loai)
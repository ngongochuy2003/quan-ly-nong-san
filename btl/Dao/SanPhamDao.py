from Context.DBConnect import Database

class SanPhamDao:
    def __init__(self):
      self.db = Database()
      self.cursor = self.db.get_connection().cursor()

    def getAllSanPham(self):
      self.cursor.execute("SELECT * FROM sanpham")
      return self.cursor.fetchall()

    def addSanPham(self, idsanpham, soluong, tensanpham, dongia, idnhacungcap):
      query = ("INSERT INTO sanpham(idsanpham, soluong, tensanpham, dongia,"
               " idnhacungcap) VALUES(%s, %s, %s, %s, %s)")
      values = (idsanpham, soluong, tensanpham, dongia, idnhacungcap)
      self.cursor.execute(query, values)
      self.db.get_connection().commit()

    def updateSanPham(self, idsanpham, soluong, tensanpham, dongia, idnhacungcap):
      query = ("UPDATE sanpham SET soluong = %s, tensanpham = %s, dongia = %s, "
               "idnhacungcap = %s WHERE idsanpham = %s")
      values = (soluong, tensanpham, dongia, idnhacungcap, idsanpham)
      self.cursor.execute(query, values)
      self.db.get_connection().commit()

    def deleteSanPham(self, idsanpham):
      query = "DELETE FROM sanpham WHERE idsanpham = %s"
      values = (idsanpham,)
      self.cursor.execute(query, values)
      self.db.get_connection().commit()

    def searchById(self, idsanpham):
      query = ("SELECT * FROM chitietsanpham WHERE idsanpham = %s")
      self.cursor.execute(query, (idsanpham,))
      return self.cursor.fetchall()

    def getAllChiTietSanPham(self):
      self.cursor.execute("SELECT * FROM chitietsanpham")
      return self.cursor.fetchall()

    def updateChiTietSanPham(self, idsanpham, ngaynhapkho, hansudung, loai):
      query = ("UPDATE chitietsanpham SET ngaynhapkho = %s, hansudung = %s, loai = %s WHERE idsanpham = %s")
      values = (ngaynhapkho, hansudung, loai, idsanpham)
      self.cursor.execute(query, values)
      self.db.get_connection().commit()
    def insertChiTietSanPham(self, idsanpham, ngaynhapkho, hansudung, loai):
      query = ("INSERT INTO chitietsanpham(idsanpham, ngaynhapkho, hansudung, loai) VALUES(%s, %s, %s, %s)")
      values = (idsanpham, ngaynhapkho, hansudung, loai)
      self.cursor.execute(query, values)
      self.db.get_connection().commit()
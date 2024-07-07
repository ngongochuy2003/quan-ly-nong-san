from datetime import datetime

from Context.DBConnect import Database
class DonhangDao:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.get_connection().cursor()

    def getAllDonHang(self):
        self.cursor.execute("SELECT * FROM donhang")
        return self.cursor.fetchall()

    def addDonHang(self, iduser,tenkhach, sdt, tongtien=0):
        query = ("INSERT INTO donhang(iduser,tenkhach, sdt, tongtien) VALUES(%s,%s,%s, %s)")
        values = (iduser,tenkhach,sdt, tongtien)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()

    def updateDonHang(self, iddonhang,tenkhach,sdt, iduser ):
        query = ("UPDATE donhang SET iduser = %s, tenkhach = %s, sdt=%s WHERE iddonhang = %s")
        values = (iduser,tenkhach,sdt, iddonhang)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()

    def deleteDonHang(self, iddonhang):
        query = ("DELETE FROM donhang WHERE iddonhang = %s")
        self.cursor.execute(query, (iddonhang,))
        self.db.get_connection().commit()

    def searchByIdUser(self, iduser):
        query = ("SELECT * FROM donhang WHERE iduser = %s")
        self.cursor.execute(query, (iduser,))
        return self.cursor.fetchall()

    def updateTongtiendonhang(self, iddonhang):
        query = ("UPDATE donhang SET tongtien = (SELECT SUM(tongtien) FROM chitietdonhang WHERE iddonhang = %s) WHERE iddonhang = %s")
        self.cursor.execute(query, (iddonhang, iddonhang))
        self.db.get_connection().commit()

    def getAllChitietdonhang(self):
        self.cursor.execute("SELECT * FROM chitietdonhang")
        return self.cursor.fetchall()
    def updateChiTietDonHang(self,iddonhang, idsanpham, soluong, dongia,id):
        tongtien = soluong * dongia
        query = ("UPDATE chitietdonhang SET iddonhang = %s,idsanpham = %s, soluong = %s, dongia = %s, tongtien = %s WHERE id = %s")
        values = (iddonhang,idsanpham,soluong, dongia, tongtien, id)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()

    def addChiTietDonHang(self, iddonhang, idsanpham, soluong, dongia):
        tongtien = int(soluong) * int(dongia)
        ngayban = datetime.now()
        query = ("INSERT INTO chitietdonhang(iddonhang, idsanpham, soluong, dongia, tongtien, ngayban) VALUES(%s, %s, %s, %s, %s, %s)")
        values = (iddonhang, idsanpham, soluong, dongia, tongtien, ngayban)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()
        self.updateSoluongsanpham(idsanpham, soluong)

    def updateSoluongsanpham(self, idsanpham, soluong):
        query = ("UPDATE sanpham SET soluong = soluong - %s WHERE idsanpham = %s")
        values = (soluong, idsanpham)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()
    def deleteChitietDonhang(self, id,idsanpham, soluong):
        query = ("DELETE FROM chitietdonhang WHERE id = %s")
        self.cursor.execute(query, (id,))
        self.db.get_connection().commit()
        self.revertSoluongsanpham(idsanpham, soluong)
    def revertSoluongsanpham(self, idsanpham, soluong):
        query = ("UPDATE sanpham SET soluong = soluong + %s WHERE idsanpham = %s")
        values = (soluong, idsanpham)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()
    def loadctdh(self, iddonhang):
        query = ("SELECT * FROM chitietdonhang WHERE iddonhang = %s")
        self.cursor.execute(query, (iddonhang,))
        return self.cursor.fetchall()
    def searchChitiethoadon(self,ngaydau,ngaycuoi):
        query = ("SELECT * FROM chitietdonhang WHERE ngayban BETWEEN %s AND %s")
        self.cursor.execute(query, (ngaydau, ngaycuoi))
        return self.cursor.fetchall()

    def checkdata(self,iddonhang):
        query = ("SELECT count(*) FROM chitietdonhang where iddonhang = %s")
        self.cursor.execute(query, (iddonhang,))
        count = self.cursor.fetchone()[0]
        if count == 0:
            return True
        else:
            return False
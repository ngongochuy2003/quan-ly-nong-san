import Dao.DonHangDao as DonHangDao
class DonhangController:
    def __init__(self):
        self.donhang_dao = DonHangDao.DonhangDao()
    def getAllDonHang(self):
        return self.donhang_dao.getAllDonHang()
    def addDonHang(self,iduser, tenkhach, sdt):
        return self.donhang_dao.addDonHang( iduser,tenkhach, sdt)
    def updateDonHang(self, iduser,tenkhach,sdt, iddonhang):
        return self.donhang_dao.updateDonHang(iduser,tenkhach,sdt, iddonhang)
    def deleteDonHang(self, iddonhang):
        return self.donhang_dao.deleteDonHang(iddonhang)
    def searchByIdUser(self, iduser):
        return self.donhang_dao.searchByIdUser(iduser)

    def updateTongtiendonhang(self, iddonhang):
        return self.donhang_dao.updateTongtiendonhang(iddonhang)
    def getAllChitietdonhang(self):
        return self.donhang_dao.getAllChitietdonhang()
    def updateChiTietDonHang(self,iddonhang,idsanpham,soluong, dongia, id):
        return self.donhang_dao.updateChiTietDonHang(iddonhang,idsanpham,soluong, dongia, id)
    def addChiTietDonHang(self, iddonhang, idsanpham, soluong, dongia):
        return self.donhang_dao.addChiTietDonHang(iddonhang, idsanpham, soluong, dongia)
    def deleteChitietDonhang(self, id, idsanpham, soluong):
        return self.donhang_dao.deleteChitietDonhang(id, idsanpham, soluong)
    def loadctdh(self, iddonhang):
        return self.donhang_dao.loadctdh(iddonhang)

    def searchChitiethoadon(self, ngaydau, ngaycuoi):
        return self.donhang_dao.searchChitiethoadon(ngaydau,ngaycuoi)

    def checkdata(self, iddonhang):
        return self.donhang_dao.checkdata(iddonhang)
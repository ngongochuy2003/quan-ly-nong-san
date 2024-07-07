from Dao.NhaCungCapDao import NhaCungCapDao

class NhaCungCapController:

    def __init__(self):
        self.dao = NhaCungCapDao()

    def getAllNhaCungCap(self):
        return self.dao.getAllNhaCungCap()

    def addNhaCungCap(self, idnhacungcap, tennhacungcap, diachi, sodienthoai, email):
        self.dao.addNhaCungCap(idnhacungcap, tennhacungcap, diachi, sodienthoai, email)

    def updateNhaCungCap(self, idnhacungcap, tennhacungcap, diachi, sodienthoai, email):
        self.dao.updateNhaCungCap(idnhacungcap, tennhacungcap, diachi, sodienthoai, email)

    def deleteNhaCungCap(self, idnhacungcap):
        self.dao.deleteNhaCungCap(idnhacungcap)
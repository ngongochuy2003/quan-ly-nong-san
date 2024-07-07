from Context.DBConnect import Database

class TaiKhoanDao:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.get_connection().cursor()


    def getAllTaiKhoan(self):
        self.cursor.execute("SELECT * FROM taikhoan WHERE role != 1")
        return self.cursor.fetchall()

    def updateTaiKhoan(self, id, username, password, role):
        query = ("UPDATE taikhoan SET username = %s, pass = %s,"
                 " role = %s WHERE iduser = %s")
        values = (username, password, role, id)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()

    def addTaiKhoan(self, username, password, role):
        query = ("INSERT INTO taikhoan(username, pass, role) VALUES(%s, %s, %s)")
        values = (username, password, role)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()

    def deleteTaikhoan(self, id):
        query = ("DELETE FROM taikhoan WHERE iduser = %s")
        self.cursor.execute(query, (id,))
        self.db.get_connection().commit()

    def searchByUsername(self, username):
        query = ("SELECT * FROM taikhoan WHERE username = %s")
        self.cursor.execute(query, (username,))
        return self.cursor.fetchall()

    def searchByRole(self, role):
        query = ("SELECT * FROM taikhoan WHERE role = %s")
        self.cursor.execute(query, (role,))
        return self.cursor.fetchall()

    def getThongTinByUserName(self, username):
        query = ("SELECT * FROM thongtin WHERE hoten = %s")
        self.cursor.execute(query, (username,))
        return self.cursor.fetchall()

    def getAllThongTin(self):
        self.cursor.execute("SELECT * FROM thongtin")
        return self.cursor.fetchall()

    def updateThongTin(self, iduser, hoten, tuoi, email, diachi, sdt):
        query = ("UPDATE thongtin SET hoten = %s, tuoi = %s, email = %s, diachi = %s, sdt = %s WHERE iduser = %s")
        values = (hoten, tuoi, email, diachi, sdt, iduser)
        self.cursor.execute(query, values)
        self.db.get_connection().commit()

    def addThongTinChiTietNhanVien(self,iduser, hoten, tuoi, email, diachi, sdt):
        try:
            query = ("INSERT INTO thongtin(iduser, hoten, tuoi, email, diachi, sdt) "
                     "VALUES(%s, %s, %s, %s, %s, %s)")
            values = (iduser, hoten, tuoi, email, diachi, sdt)
            self.cursor.execute(query, values)
            self.db.get_connection().commit()
        except Exception as e:
            print("Error occurred:", e)
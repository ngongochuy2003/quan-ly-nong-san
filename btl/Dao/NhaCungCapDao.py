from Context.DBConnect import Database

class NhaCungCapDao:
   def __init__(self):
      self.db = Database()
      self.cursor = self.db.get_connection().cursor()


   def getAllNhaCungCap(self):
     self.cursor.execute("SELECT * FROM nhacungcap")
     return self.cursor.fetchall()

   def addNhaCungCap(self,idnhacungcap, tennhacungcap, diachi, sodienthoai, email):
     query = ("INSERT INTO nhacungcap(idnhacungcap, tennhacungcap, diachi, sodienthoai, email) VALUES(%s, %s, %s, %s, %s)")
     values = (idnhacungcap, tennhacungcap, diachi, sodienthoai, email)
     self.cursor.execute(query, values)
     self.db.get_connection().commit()

   def updateNhaCungCap(self, idnhacungcap, tennhacungcap, diachi, sodienthoai, email):
      query = ("UPDATE nhacungcap SET tennhacungcap = %s, diachi = %s, sodienthoai = %s, email = %s WHERE idnhacungcap = %s")
      values = (tennhacungcap, diachi, sodienthoai, email, idnhacungcap)
      self.cursor.execute(query, values)
      self.db.get_connection().commit()

   def deleteNhaCungCap(self,idnhacungcap):
      query = ("DELETE FROM nhacungcap WHERE idnhacungcap = %s")
      self.cursor.execute(query, (idnhacungcap,))
      self.db.get_connection().commit()
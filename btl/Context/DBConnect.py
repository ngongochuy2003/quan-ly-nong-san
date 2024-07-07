import mysql.connector

class Database:
    def __init__(self):

        self.mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user = "root",
            password = "123456",
            db = "db_quanlynongsan"
            )
    def get_connection(self):
        if self.mydb.is_connected():
            print("Kết nối thành công")
            return self.mydb
        else:
            print("Kết nối đã bị đóng")
            return None

    def close_connection(self):
        if self.mydb.is_connected():
            self.mydb.close()
            print("Ngắt kết nối thành công")
        else:
            print("Kết nối đã bị đóng trước đó")
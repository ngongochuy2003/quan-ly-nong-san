import pandas as pd

from Context.DBConnect import Database

db = Database()
connection = db.get_connection()

sql = "SELECT * FROM maytinh"
data = pd.read_sql(sql, connection)

print(data)
db.close_connection()
import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.db", check_same_thread=False)

    def updCnt(self, value):
        cursor = self.connection.cursor()
        request = "UPDATE info SET cnt=?"
        cursor.execute(request, (value,))
        self.connection.commit()

    def getCnt(self):
        cursor = self.connection.cursor()
        request = "SELECT cnt FROM info"
        result = cursor.execute(request).fetchone()
        return result[0]

    def updAlbum(self, value):
        cursor = self.connection.cursor()
        request = "UPDATE info SET album=?"
        cursor.execute(request, (value,))
        self.connection.commit()

    def getAlbum(self):
        cursor = self.connection.cursor()
        request = "SELECT album FROM info"
        result = cursor.execute(request).fetchone()
        return result[0]

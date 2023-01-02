import sqlite3

class student_repo:
    def __init__(self):
        self.conn = sqlite3.connect("test.db", isolation_level=None)
        self.c = self.conn.cursor()

    def login(self,id,pw):
        SQL = f"SELECT upw FROM users WHERE uid = '{id}'"
        self.c.execute(SQL)
        try:
            if (self.c.fetchone()[0]==pw):
                print('로그인 성공')
            else:
                print('패스워드가 틀렸습니다')
        except TypeError:
            print('아이디가 없습니다')

    def submit(self,id,pw):
        SQL = f"INSERT INTO users(uid,upw) VALUES('{id}','{pw}')"
        self.c.execute(SQL)
        self.conn.commit()

    def getAllUser(self):
        SQL = f"SELECT * from users"
        self.c.execute(SQL)
        return self.c.fetchall()
import pymysql

class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user=id, password=pw, db=db_name, charset='utf-8')
        self.curs = self.conn.cursor()

    def insert_total(self, total):
        sql = 'insert into demo(b, c) values(%s)'
        self.curs.excute(sql, (total, ))
        self.conn.commit()


new MysqlController()
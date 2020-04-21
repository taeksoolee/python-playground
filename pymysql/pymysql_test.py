import pymysql

conn = pymysql.connect(host='localhost', port="3307" user='root', password='toor', db='demo')

'''
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from book"

curs.execute(sql)

rows = curs.fetchall()

for row in rows:
    print(row)
    print(row['id'], row['name'])
'''

curs =conn.cursor()

sql = "insert into book(name) values(%s)"
curs.execute(sql, ('test'))

print(curs.fetchall())

conn.close()
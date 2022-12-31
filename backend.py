import sqlite3


def connect():
    conn = sqlite3.connect("Users.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS user (ID INTEGER,Nickname text,Code text,Live_answering boolean,Entering_code INTEGER,Is_Admin boolean,subset_of INTEGER)")
    conn.commit()
    conn.close()


def insert(id,nickname, code, live_answ, entering_code,is_admin,subset_of):
    conn = sqlite3.connect("Users.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO user VALUES (?,?,?,?,?,?,?)', (id,nickname, code, live_answ,entering_code, is_admin, subset_of))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Users.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM user')
    rows = cur.fetchall()
    conn.close()
    return rows

def search(id="",nickname="", code="", live_answ="", entering_code="",is_admin="",subset_of=""):
    conn = sqlite3.connect("Users.db")
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM user WHERE ID=? OR Nickname=? OR Code=? OR Live_answering=? OR Entering_code=? OR Is_Admin=? OR subset_of=?',
        (id, nickname, code, live_answ,entering_code,is_admin,subset_of))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("Users.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM user WHERE id=?', (id,))
    conn.commit()
    conn.close()


def update(id,nickname, code, live_answ, entering_code, is_admin, subset_of):
    conn = sqlite3.connect("Users.db")
    cur = conn.cursor()
    cur.execute(
        'UPDATE user SET Nickname=?,Code=?,Live_answering=?,Entering_code=?,Is_Admin=?,subset_of=? WHERE id=?',
        (nickname,code,live_answ,entering_code, is_admin, subset_of, id))
    conn.commit()
    conn.close()


connect()
# insert(2025031482, 'code 10', '10', 1, 123456, 1, 2)
# update(394075806, 'code 1', '1', 1, 193496, 1, 1)
# delete(2025031482)

# print(view())
# print(view())
# delete(1263524768)
# insert(1498008651,'code 007','007',False)
# insert(1149573041, 'code 7', '7', 0,781177)
# a = view()
# print(a[0][0])#number_id
# print(a[0][1])#nickname
# print(a[0][2])#code
# print(a[0][3])#Live_answering
# print(a[0][4])#Entering_code
# print(search(nickname='code 1'))
for i in view():
    print(i)
# a = search(id='',nickname='', code='1', live_answ='', entering_code='')
# print(a)
# for i in view():
    # print(i)
# insert(1263524768, 'code 1', '1', 0, 818504, 1, 1)

#یادت باشه چیزی بنویسی که اگه یه نفر چیزی وارد کرد که از قبل وجود داشت بهش ارور بده

'''
(1263524768, 'code 1', '1', 0, 818504, 1, 1)
(1250041126, 'code 2', '2', 0, 456428, 0, 1)
(1499841944, 'code 3', '3', 0, 971494, 0, 1)
(1414632095, 'code 4', '4', 0, 471302, 0, 1)
(1287889248, 'code 5', '5', 0, 651851, 0, 1)
(1498008651, 'code 6', '6', 0, 151660, 0, 1)
(1149573041, 'code 7', '7', 0, 781177, 0, 1)
'''
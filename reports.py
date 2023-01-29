import psycopg2

connection = psycopg2.connect(
    host='34.83.186.91',
    database='koboform',
    user='kobo',
    password='[<]y.<f!zfNh'

)
cur = connection.cursor()
cur.execute('select * from core_site where project_id = 394')
x = cur.fetchall()
print(x)
print(len(x))

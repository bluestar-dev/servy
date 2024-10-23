import psycopg2

def get_technician_info():
    connection = psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM technicians')
    techs = cursor.fetchall()
    cursor.close()
    connection.close()
    return [{'id': tech[0], 'name': tech[1], 'phone': tech[2], 'skill': tech[3]} for tech in techs]

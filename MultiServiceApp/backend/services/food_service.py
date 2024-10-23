import psycopg2

def list_food_items():
    connection = psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM food_items')
    items = cursor.fetchall()
    cursor.close()
    connection.close()
    return [{'id': item[0], 'name': item[1], 'price': item[2], 'image_url': item[3]} for item in items]

def add_food_item(data):
    connection = psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute('INSERT INTO food_items (name, price, image_url) VALUES (%s, %s, %s)',
                   (data['name'], data['price'], data['image_url']))
    connection.commit()
    cursor.close()
    connection.close()
    return {'message': 'Food item added successfully'}, 201

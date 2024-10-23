import psycopg2

def get_bike_orders():
    connection = psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM bike_orders')
    orders = cursor.fetchall()
    cursor.close()
    connection.close()
    return [{'id': order[0], 'order_details': order[1]} for order in orders]

def create_bike_order(data):
    connection = psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute('INSERT INTO bike_orders (order_details) VALUES (%s)', 
                   (data['order_details'],))
    connection.commit()
    cursor.close()
    connection.close()
    return {'message': 'Bike order created successfully'}, 201

def get_bike_riders():
    connection = psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM bike_riders')
    riders = cursor.fetchall()
    cursor.close()
    connection.close()
    return [{'id': rider[0], 'name': rider[1], 'phone': rider[2]} for rider in riders]

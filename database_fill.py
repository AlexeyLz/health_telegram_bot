from bot_settings import connection


def create_database():
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sedentary_work_table
                        (serial_id SERIAL,
                         id INT,
                         description TEXT,
                         image_path TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
                        (
                         user_id INTEGER,
                         serial_id SERIAL,
                         sedentary_work_exercise_number INTEGER)""")
    connection.commit()
    cursor.close()


def insert_data():
    cursor = connection.cursor()
    postgres_insert_blob_query = """INSERT INTO sedentary_work_table
                                      (id, description, image_path) VALUES (%s, %s, %s)"""
    for i in range(1, 9):
        path = 'resources/' + str(i) + '.jpg'
        description = open('resources/' + str(i) + '.txt').read()
        # Преобразование данных в формат кортежа
        data_tuple = (i, description, path)
        cursor.execute(postgres_insert_blob_query, data_tuple)
        connection.commit()
    cursor.close()

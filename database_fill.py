from bot_settings import connection


def change_database():
    cursor = connection.cursor()
    cursor.execute("""ALTER TABLE users ALTER COLUMN user_id TYPE BIGINT;""")

    connection.commit()
    cursor.close()

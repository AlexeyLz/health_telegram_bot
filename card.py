from bot_settings import sqlite_connection
class Card:
    def __init__(self, number_exercise):
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT * FROM sedentary_work_table WHERE rowid=?", (number_exercise,))
        card_data = cursor.fetchone()
        self.description = card_data[0]
        self.image_path = card_data[1]

    def get_description(self):
        return self.description

    def get_image(self):
        return open(self.image_path, 'rb')
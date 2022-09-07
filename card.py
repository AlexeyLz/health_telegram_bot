from bot_settings import connection
class Card:
    def __init__(self, number_exercise):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sedentary_work_table WHERE id=%s", (number_exercise,))
        card_data = cursor.fetchone()
        self.serial_id = card_data[0]
        self.id = card_data[1]
        self.description = card_data[2]
        self.image_path = card_data[3]

    def get_description(self):
        return self.description

    def get_image(self):
        return open(self.image_path, 'rb')
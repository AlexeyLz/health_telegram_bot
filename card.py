from bot_settings import connection


class Card:
    def __init__(self, number_exercise, table):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM " + table + " WHERE id=%s", (number_exercise,))
        card_data = cursor.fetchone()
        self.serial_id = card_data[0]
        self.id = card_data[1]
        self.description = card_data[2]
        self.image_path = card_data[3]
        self.video_url = 'https://media.publit.io/file/h_1080/' + card_data[3] + '.mp4'

    def get_description(self):
        return self.description

    def get_image(self):
        return open(self.image_path, 'rb')

    def get_video(self):
        return self.video_url

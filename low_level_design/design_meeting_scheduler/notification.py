

class Notification:

    def __init__(self, notification_id: int, content: str, creation_date):
        self.__notification_id = notification_id
        self.__content = content
        self.__creation_date = creation_date

    def send_notification(self, user):
        pass

    def cancel_notification(self, user):
        pass
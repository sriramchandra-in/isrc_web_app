from models.message import Message, DateObj


class KcvMessage:
    def __init__(self, date:DateObj, message: Message):
        self.date = date
        self.message = message

    @classmethod
    def create(cls, item):
        date: DateObj = DateObj.create(item)
        message: Message = Message.create(item)
        return KcvMessage(date, message)
from models.message import Message, BabujiAudio, KcnAudio


class KcvMessage:
    def __init__(self, date, message):
        self.date = date
        self.message = message

    @classmethod
    def create(cls, item):
        date_elems = item.iter("date")
        dates = []
        for date_elem in date_elems:
            dates.append(date_elem.text)
        date = dates[0]
        message = Message.create(item)
        return KcvMessage(date, message)
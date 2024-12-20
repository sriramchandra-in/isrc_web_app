from models.message import Message, BabujiAudio, KcnAudio


class BabujiMessage:
    def __init__(self, date, message, babuji_audio, kcn_audio):
        self.date = date
        self.message = message
        self.babuji_audio = babuji_audio
        self.kcn_audio = kcn_audio

    @classmethod
    def create(cls, item):
        date_elems = item.iter("date")
        dates = []
        for date_elem in date_elems:
            dates.append(date_elem.text)
        date = dates[0]
        message = Message.create(item)
        babuji_audio = BabujiAudio.create(item)
        kcn_audio = KcnAudio.create(item)
        return BabujiMessage(date, message, babuji_audio, kcn_audio)
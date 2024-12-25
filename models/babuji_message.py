from models.message import Message, BabujiAudio, KcnAudio, DateObj, EraDate

class BabujiMessage:
    def __init__(self, date: DateObj,
                 era_date: EraDate,
                 message: Message,
                 babuji_audio: BabujiAudio,
                 kcn_audio: KcnAudio):
        self.date = date
        self.era_date = era_date
        self.message = message
        self.babuji_audio = babuji_audio
        self.kcn_audio = kcn_audio

    @classmethod
    def create(cls, item):
        date: DateObj = DateObj.create(item)
        era_date = EraDate.create(item)
        message: Message = Message.create(item)
        babuji_audio: BabujiAudio = BabujiAudio.create(item)
        kcn_audio: KcnAudio = KcnAudio.create(item)
        return BabujiMessage(date, era_date, message, babuji_audio, kcn_audio)
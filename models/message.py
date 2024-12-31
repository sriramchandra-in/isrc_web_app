class Message:
    def __init__(self, text: str, attributes:dict, reference: str):
        self.sentence = text
        self.href = attributes['href']
        self.reference = reference

    @classmethod
    def create(cls, item):
        message_elems = item.iter("message")
        messages = []
        for message_elem in message_elems:
            messages.append( (message_elem.text, message_elem.attrib))
        message = messages[0]
        (text, attributes) = message
        reference_elems = item.iter("reference")
        references = []
        for reference_elem in reference_elems:
            references.append(reference_elem.text)
        reference = references[0]
        return cls(text, attributes, reference)


class BabujiAudio:
    def __init__(self, exists:bool, text: str,  attributes: dict):
        self.exists = exists
        self.title = text
        self.audio = attributes.get('audio', "")
        self.txt = attributes.get('txt', "")

    @classmethod
    def create(cls, item):
        babuji_elems = item.iter("babuji")
        babuji_audios = []
        for babuji_elem in babuji_elems:
            babuji_audios.append( cls(True, babuji_elem.text, babuji_elem.attrib))
        if len(babuji_audios) == 0 :
            return cls(False,  "", {})
        return babuji_audios[0]

class KcnAudio:
    def __init__(self, exists: bool, text: str, attributes: dict):
        self.exists = exists
        self.title = text
        self.audio = attributes.get('audio', "")
        self.txt = attributes.get('txt', "")
        self.partial_txt = attributes.get('partial_txt', "")
        self.start = attributes.get('start', "")
        self.end = attributes.get('end', "")
        self.partial_audio_exists = self.start != ""
        self.partial_text_exists = self.partial_txt != ""

    @classmethod
    def create(cls, item):
        kcn_elems = item.iter("kcn")
        kcn_audios = []
        for kcn_elem in kcn_elems:
            kcn_audios.append( cls(True, kcn_elem.text, kcn_elem.attrib))
        if len(kcn_audios) == 0 :
            return cls(False,"", {})
        return kcn_audios[0]

class DateObj:
    def __init__(self, text: str, attributes: dict):
        self.text = text
        self.has_attributes = len(attributes) > 0
        self.title = attributes.get('title', "")
        self.reference = attributes.get('ref', "")

    @classmethod
    def create(cls, item):
        date_elems = item.iter("date")
        dates = []
        for date_elem in date_elems:
            dates.append( cls(date_elem.text, date_elem.attrib))
        return dates[0]


class EraDate:
    def __init__(self, text: str):
        self.text = text

    @classmethod
    def create(cls, item):
        era_dt_elems = item.iter("era_dt")
        era_dts = []
        for era_dt_elem in era_dt_elems:
            era_dts.append( cls(era_dt_elem.text))
        return era_dts[0]
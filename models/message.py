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
            return BabujiAudio(False,  "", {})
        return babuji_audios[0]

class KcnAudio:
    def __init__(self, exists: bool, text: str, attributes: dict):
        self.exists = exists
        self.title = text
        self.audio = attributes.get('audio', "")
        self.txt = attributes.get('txt', "")

    @classmethod
    def create(cls, item):
        kcn_elems = item.iter("kcn")
        kcn_audios = []
        for kcn_elem in kcn_elems:
            kcn_audios.append( cls(True, kcn_elem.text, kcn_elem.attrib))
        if len(kcn_audios) == 0 :
            return KcnAudio(False,"", {})
        return kcn_audios[0]

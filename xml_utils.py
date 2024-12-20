import xml.etree.ElementTree as ET

from models.babuji_message import BabujiMessage
from models.kcv_message import KcvMessage


def create_babuji_message_map(fileName: str):
    babuji_message_dict = {}
    messages = ET.parse(fileName).getroot()
    for item in messages:
       message =  BabujiMessage.create(item)
       babuji_message_dict[message.date] = message
    return babuji_message_dict

def create_kcv_message_map(fileName: str):
    kcv_message_dict = {}
    messages = ET.parse(fileName).getroot()
    for item in messages:
        message = KcvMessage.create(item)
        kcv_message_dict[message.date] = message
    return kcv_message_dict

import xml.etree.ElementTree as ET

from models.babuji_message import BabujiMessage
from models.kcv_message import KcvMessage


def create_babuji_message_map(file_name: str):
    babuji_message_dict = {}
    messages = ET.parse(file_name).getroot()
    for item in messages:
       message =  BabujiMessage.create(item)
       babuji_message_dict[message.date.text] = message
    return babuji_message_dict

def create_kcv_message_map(file_name: str):
    kcv_message_dict = {}
    messages = ET.parse(file_name).getroot()
    for item in messages:
        message = KcvMessage.create(item)
        kcv_message_dict[message.date.text] = message
    return kcv_message_dict

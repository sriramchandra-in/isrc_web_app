from dotenv import load_dotenv, dotenv_values

from models.message import Message
import xml.etree.ElementTree as ET

from xml_utils import create_babuji_message_map, create_kcv_message_map

load_dotenv()

def convert_text_to_html(txt: str):
    src = f'{txt}.txt'
    dest = f'{txt}.html'
    contents = open(src, 'r')
    with open(dest, 'w') as f:
        for line in contents.readlines():
            f.write(f'<pre>{line}</pre>')

def main():
    # config = dotenv_values(".env")
    # config_dir = config.get("CONFIG_DIR")
    # babuji_xml = config.get("BABUJI_XML")
    # kcv_xml = config.get("KCV_XML")
    # babuji_abs_xml = config_dir + "/" + babuji_xml
    # print(babuji_abs_xml)
    # kcv_abs_xml = config_dir + "/" + kcv_xml
    # print(kcv_abs_xml)
    #babuji_message_map = create_babuji_message_map(babuji_abs_xml)
    #kcv_message_map = create_kcv_message_map(kcv_abs_xml)
    convert_text_to_html("config/txt/constant_remembrance")

if __name__ == '__main__':
  main()

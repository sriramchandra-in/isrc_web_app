import sys

import uvicorn
from fastapi import FastAPI
from xml_utils import create_babuji_message_map,create_kcv_message_map
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

from dotenv import dotenv_values

config = dotenv_values(".env")
config_dir = config.get("CONFIG_DIR")
babuji_xml = config.get("BABUJI_XML")
kcv_xml = config.get("KCV_XML")
babuji_abs_xml = config_dir+ "/" + babuji_xml
print(babuji_abs_xml)
kcv_abs_xml = config_dir + "/" + kcv_xml
print(kcv_abs_xml)
babuji_message_map = create_babuji_message_map(babuji_abs_xml)
kcv_message_map = create_kcv_message_map(kcv_abs_xml)


@app.get("/data/{date}")
async def message(date: str):
    return {babuji_message_map[date], kcv_message_map[date] }

@app.get("/{date}", response_class=HTMLResponse)
async def html(request: Request, date: str):
    context = {
        "id": date,
        "master": babuji_message_map[date],
        "kcv": kcv_message_map[date]
    }
    return templates.TemplateResponse(
        request=request, name="index.html", context=context
    )

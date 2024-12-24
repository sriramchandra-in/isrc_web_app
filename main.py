import logging
import sys
from datetime import datetime

import uvicorn
from fastapi import FastAPI
from starlette.responses import Response, FileResponse

from xml_utils import create_babuji_message_map,create_kcv_message_map
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')



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


@app.middleware("http")
async def log_traffic(request: Request, call_next):
    start_time = datetime.now()
    response = await call_next(request)
    process_time = (datetime.now() - start_time).total_seconds()
    client_host = request.client.host
    log_params = {
        "request_method": request.method,
        "request_url": str(request.url),
        "request_size": request.headers.get("content-length"),
        "request_headers": dict(request.headers),
        "request_body": await request.body(),
        "response_status": response.status_code,
        "response_size": response.headers.get("content-length"),
        "response_headers": dict(response.headers),
        "process_time": process_time,
        "client_host": client_host
    }
    logging.info(str(log_params))
    return response
#
# @app.api_route("/{rest_of_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
# async def catch_all(request: Request, rest_of_path: str):
#     return Response(status_code=200)

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

@app.get("/html/babuji/{file}", response_class=HTMLResponse)
async def render_babuji_html(file:str):
    return FileResponse(f'static/html/babuji/{file}.html')

@app.get("/audio/babuji/{file}", response_class=HTMLResponse)
async def render_babuji_audio(file:str):
    return FileResponse(f'static/audio/babuji/{file}.mp3', media_type='audio/mpeg')
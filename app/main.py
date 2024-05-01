from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from hospital_fsm import HospitalFSM

app = FastAPI()
templates = Jinja2Templates(directory="templates")

hospital_fsm = HospitalFSM()

@app.get("/")
async def root():
    return templates.TemplateResponse("index.html", {"request": Request})

@app.post("/button_click")
async def button_click(button_id: str):
    hospital_fsm.send(button_id)
    return {"state": hospital_fsm.state.value, "buttons": hospital_fsm.buttons}
from fastapi import APIRouter
from hospital_fsm import HospitalFSM

router = APIRouter()
hospital_fsm = HospitalFSM()

@router.post("/button_click")
async def button_click(button_id: str):
    hospital_fsm.send(button_id)
    return {"state": hospital_fsm.state.value, "buttons": hospital_fsm.buttons}
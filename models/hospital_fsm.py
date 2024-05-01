import xstate

class HospitalFSM(xstate.Machine):
    states = {
        "start": {
            "on": {
                "GENERAL_INFO": "general_info",
                "SERVICES": "services",
                "APPOINTMENTS": "appointments"
            }
        },
        "general_info": {
            "on": {
                "VISITING_HOURS": "visiting_hours",
                "PARKING_INFO": "parking_info",
                "RETURN_TO_START": "start"
            }
        },
        "services": {
            "on": {
                "MEDICAL_DEPARTMENTS": "medical_departments",
                "PATIENT_SUPPORT": "patient_support",
                "RETURN_TO_START": "start"
            }
        },
        "appointments": {
            "on": {
                "SCHEDULE_APPOINTMENT": "schedule_appointment",
                "CHANGE_APPOINTMENT": "change_appointment",
                "RETURN_TO_START": "start"
            }
        },
        "medical_departments": {
            "on": {
                "CARDIOLOGY_INFO": "cardiology_info",
                "NEUROLOGY_INFO": "neurology_info",
                "RETURN_TO_SERVICES": "services"
            }
        },
        "cardiology_info": {
            "on": {
                "RETURN_TO_MEDICAL_DEPARTMENTS": "medical_departments"
            }
        },
        "neurology_info": {
            "on": {
                "RETURN_TO_MEDICAL_DEPARTMENTS": "medical_departments"
            }
        }
    }

    def __init__(self):
        super().__init__(states=self.states, initial="start")

    @property
    def buttons(self):
        buttons = []
        for transition in self.state.transitions:
            buttons.append(transition.event)
        return buttons
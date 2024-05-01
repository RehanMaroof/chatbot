import unittest
from hospital_fsm import HospitalFSM

class TestHospitalFSM(unittest.TestCase):
    def setUp(self):
        self.hospital_fsm = HospitalFSM()

    def test_start_state(self):
        self.assertEqual(self.hospital_fsm.state.value, "start")

    def test_general_info_state(self):
        self.hospital_fsm.send("GENERAL_INFO")
        self.assertEqual(self.hospital_fsm.state.value, "general_info")

    def test_services_state(self):
        self.hospital_fsm.send("SERVICES")
        self.assertEqual(self.hospital_fsm.state.value, "services")

    def test_appointments_state(self):
        self.hospital_fsm.send("APPOINTMENTS")
        self.assertEqual(self.hospital_fsm.state.value, "appointments")

    def test_medical_departments_state(self):
        self.hospital_fsm.send("SERVICES")
        self.hospital_fsm.send("MEDICAL_DEPARTMENTS")
        self.assertEqual(self.hospital_fsm.state.value, "medical_departments")

    def test_cardiology_info_state(self):
        self.hospital_fsm.send("SERVICES")
        self.hospital_fsm.send("MEDICAL_DEPARTMENTS")
        self.hospital_fsm.send("CARDIOLOGY_INFO")
        self.assertEqual(self.hospital_fsm.state.value, "cardiology_info")

    def test_neurology_info_state(self):
        self.hospital_fsm.send("SERVICES")
        self.hospital_fsm.send("MEDICAL_DEPARTMENTS")
        self.hospital_fsm.send("NEUROLOGY_INFO")
        self.assertEqual(self.hospital_fsm.state.value, "neurology_info")

if __name__ == "__main__":
    unittest.main()
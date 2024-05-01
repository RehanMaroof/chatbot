import unittest
import requests

class TestHospitalRoutes(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000"

    def test_start_state(self):
        response = requests.get(f"{self.base_url}")
        self.assertEqual(response.json()["state"], "start")

    def test_general_info_state(self):
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "GENERAL_INFO"})
        self.assertEqual(response.json()["state"], "general_info")

    def test_services_state(self):
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "SERVICES"})
        self.assertEqual(response.json()["state"], "services")

    def test_appointments_state(self):
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "APPOINTMENTS"})
        self.assertEqual(response.json()["state"], "appointments")

    def test_medical_departments_state(self):
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "SERVICES"})
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "MEDICAL_DEPARTMENTS"})
        self.assertEqual(response.json()["state"], "medical_departments")

    def test_cardiology_info_state(self):
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "SERVICES"})
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "MEDICAL_DEPARTMENTS"})
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "CARDIOLOGY_INFO"})
        self.assertEqual(response.json()["state"], "cardiology_info")

    def test_neurology_info_state(self):
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "SERVICES"})
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "MEDICAL_DEPARTMENTS"})
        response = requests.post(f"{self.base_url}/button_click", json={"button_id": "NEUROLOGY_INFO"})
        self.assertEqual(response.json()["state"], "neurology_info")

if __name__ == "__main__":
    unittest.main()
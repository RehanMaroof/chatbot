**Title**: Multi-Level FAQ Chatbot for a Hospital Using X-State and Python

**Introduction**
The Multi-Level FAQ Chatbot for a Hospital is a Python application that utilizes the FastAPI framework and X-State library to create an interactive chatbot for hospitals. The chatbot provides users with information on various topics, including general information, services, and appointments. The chatbot features multi-level button interactions, allowing users to navigate through different topics and subtopics efficiently.
A state Diagram is available in the Public folder of this repositry.
**Installation**
Install Python: Download and install Python from https://www.python.org/downloads/
Clone the repository: git clone https://github.com/RehanMaroof/chatbot.git
Install the requirements: pip install -r requirements.txt
Running the Chatbot
Run the FastAPI server: uvicorn app.main:app --reload
Open your web browser and navigate to http://localhost:8000
Testing
The chatbot is tested using simple tests to verify that state transitions are handled correctly based on user button interactions. The tests are implemented using Python's unittest library and are available in the tests directory. To run the tests, executethe following command: python -m unittest tests

**Documentation**
For more information on the chatbot's design, implementation, and evaluation criteria, refer to the Documentation Report.

**License**
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
FastAPI: https://fastapi.tiangolo.com/
X-State: https://xstate.js.org/

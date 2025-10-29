💡 Project Overview
The Simple AI Tutor is a minimalist web application designed to help students, particularly those in Year 5 and above, by providing helpful, non-direct hints for their questions. It uses the Python Flask framework for the backend and leverages the Google Gemini API to act as a patient, encouraging, Socratic tutor.

Key Features
Tutor Persona: The AI is instructed to act as a friendly tutor, offering hints rather than direct answers.

Simple Interface: A single web page for inputting questions and receiving guidance.

Python Backend: Built with Flask for lightweight web handling.

🚀 Setup and Installation
Follow these steps to get the application running on your local machine.

1. Prerequisites
You need Python 3.9+ installed on your system.

2. Get Your API Key
Go to Google AI Studio and create a new Gemini API Key.

Crucially: You must set this key as an environment variable in your terminal. This is a security best practice.

macOS/Linux:

Bash

export GEMINI_API_KEY="YOUR_API_KEY_HERE"
Windows (Command Prompt):

Bash

set GEMINI_API_KEY="YOUR_API_KEY_HERE"
Windows (PowerShell):

PowerShell

$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
3. Project Structure
Create the following files and folders:

/simple-ai-tutor
├── app.py          # The main Python application logic
└── /templates
    └── index.html  # The web page interface
4. Install Dependencies
In your terminal, navigate to the simple-ai-tutor directory and install the necessary Python libraries:

Bash

pip install flask google-genai
💻 How to Run
Ensure your GEMINI_API_KEY is set (see step 2 in Setup).

Run the Python application from the main directory:

Bash

python app.py
Open your web browser and navigate to the local address provided by Flask, usually:

http://127.0.0.1:5000/

🛠️ Code Breakdown
app.py Highlights
The core functionality is controlled by a specific set of instructions sent to the Gemini model:

Python

# The system instruction ensures the AI behaves like a good tutor.
TUTOR_INSTRUCTION = (
    "You are a friendly, patient, and encouraging tutor for a Year 5 student (age 10-11). "
    "Your only job is to provide **one simple, helpful hint** and a **suggested next step** to solve the problem. "
    "You must NEVER give the direct answer. Use simple language."
)

@app.route('/', methods=['GET', 'POST'])
def index():
    # ... logic to call client.models.generate_content with the TUTOR_INSTRUCTION ...
templates/index.html Highlights
This file uses Flask's templating engine (Jinja) to display the dynamic results:

The <form method="POST"> sends the student's question back to app.py.

The {% if hint %} block only appears after the Python backend has processed the question and returned a result.

import os
from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)
client = None

# Initialize the Gemini client 
try:
    # The client automatically reads the GEMINI_API_KEY environment variable
    client = genai.Client()
except Exception as e:
    print(f"Error initializing Gemini client: {e}")

def get_ai_hint(student_question):
    """Sends the question to the AI with a specific Year 5 tutor persona."""
    if not client:
        return "AI service error. Check your API key setup."

    # This is the "system instruction" that defines the tutor's behavior
    TUTOR_INSTRUCTION = (
        "You are a friendly, encouraging, and highly patient tutor for a Year 5 student (age 10-11). "
        "Your only job is to provide **one simple, helpful hint** and a **suggested next step** to solve the problem. "
        "You must NEVER give the direct answer. Use simple language."
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[student_question],
            config={"system_instruction": TUTOR_INSTRUCTION}
        )
        return response.text
    except Exception as e:
        return f"An error occurred with the AI request: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    hint = None
    question = ""

    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            hint = get_ai_hint(question)

    # The result (or the empty form) is passed to the HTML template
    return render_template('index.html', hint=hint, question=question)

if __name__ == '__main__':
    # Set debug=True for easy development restarts
    app.run(debug=True)

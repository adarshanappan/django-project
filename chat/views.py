# import openai
# import json
# from django.http import JsonResponse
from django.shortcuts import render
import re

# # Create your views here.
def index(request):
    return render(request, 'index.html')
# # chat/views.py


from django.shortcuts import render
from django.http import JsonResponse
import json
import google.generativeai as genai

# Initialize Google Generative AI API
genai.configure(api_key="AIzaSyBJBi1PEGCEt5einIk77CZYnzvbdGky7zo") 
model = genai.GenerativeModel("gemini-1.5-flash")

# Define possible greeting words
greeting_keywords = ["hi", "hello", "hey", "morning", "good day"]

# Helper function to check for greetings
def is_greeting(user_input):
    user_input = user_input.strip().lower()
    for keyword in greeting_keywords:
        if user_input.startswith(keyword):
            return True
    return False

# Welcome message handler
def welcome_message(request):
    # Get the user input
    body = json.loads(request.body) if request.body else {}
    user_input = body.get("message", "")

    # Check if the input is a greeting
    if is_greeting(user_input):
        return JsonResponse({
            "message": "Hello! How can I assist you today?",
            "options": [
                "1. Solve an equation",
                "2. Generate math problems",
                "3. Get help with a topic",
            ]
        })

    # If not a greeting, check if it is an equation to solve
    return solve_equation(request)

# Solve equation handler
def solve_equation(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            equation = body.get('data', '')

            if not equation:
                return JsonResponse({"error": "No equation provided."}, status=400)

            # Use the Generative AI model to process the equation
            response = model.generate_content(f"Solve the equation: {equation}")
            answer = extract_answer_from_response(response.text)

            # Clean answer to remove unwanted characters
            clean_answer = clean_up_answer(answer)

            return JsonResponse({"answer": clean_answer})

        except Exception as e:
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

# Helper function to extract answer from response
def extract_answer_from_response(response_text):
    try:
        return response_text.split("=")[-1].strip()
    except:
        return "Could not extract answer."

# Clean up answer by removing unwanted characters
def clean_up_answer(answer):
    # Replace unwanted characters or symbols
    answer = answer.replace("$", "").replace("}", "").strip()  # Add more unwanted chars if needed
    return answer

# Generate math problems handler
def generate_math_problems(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            topic = body.get('topic', '')
            difficulty = body.get('difficulty', 'easy')

            if not topic:
                return JsonResponse({"error": "No topic provided."}, status=400)

            # Create prompt for generating math problems
            prompt = f"Create {difficulty} level Mathematics problems for {topic}. Include numerical calculations."

            # Use AI to generate problems
            response = model.generate_content(prompt)
            problems = extract_problems_from_response(response.text)

            return JsonResponse({"problems": problems})

        except Exception as e:
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

# Helper function to extract problems from AI response
def extract_problems_from_response(response_text):
    problems = []
    questions = response_text.split("Question")[1:]

    for q in questions:
        problem = q.split("\n")[0].strip()  # Extract the first line as the problem
        problems.append(problem)

    return problems
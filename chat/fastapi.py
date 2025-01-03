# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import google.generativeai as genai

# # Initialize FastAPI app
# app = FastAPI()

# # Configure Google Generative AI API
# genai.configure(api_key="AIzaSyBJBi1PEGCEt5einIk77CZYnzvbdGky7zo")

# # Welcome message and options
# @app.get("/welcome/")
# async def welcome_message():
#     greeting = "Hi! "
#     options = [
#         "1. Solve an equation",
#         "2. Generate math problems",
#         "3. Get help with a topic",
#     ]
#     return {
#         "message": greeting + "How can I assist you today?",
#         "options": options
#     }

# # Problem generation model
# class ProblemRequest(BaseModel):
#     topic: str
#     difficulty: str = "easy"

# # Solve equation endpoint
# @app.post("/solve-equation/")
# async def solve_equation(equation: str):
#     try:
#         if not equation:
#             raise HTTPException(status_code=400, detail="No equation provided.")
        
#         # Generate solution using AI
#         response = genai.generate_text(f"Solve the equation: {equation}")
#         answer = extract_answer_from_response(response.content)

#         return {"answer": answer}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

# # Generate math problems endpoint
# @app.post("/generate-math-problems/")
# async def generate_math_problems(request: ProblemRequest):
#     try:
#         prompt = f"Create {request.difficulty} level Mathematics problems for {request.topic}. Include numerical calculations."
        
#         # Generate problems using AI
#         response = genai.generate_text(prompt)
#         problems = extract_problems_from_response(response.content)

#         return {"problems": problems}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# # Helper functions to process the AI response
# def extract_answer_from_response(response_text: str):
#     try:
#         return response_text.split("=")[-1].strip()
#     except:
#         return "Could not extract answer."

# def extract_problems_from_response(response_text: str):
#     problems = []
#     questions = response_text.split("Question")[1:]
    
#     for q in questions:
#         problem = q.split("\n")[0].strip()  # Extract first line as problem
#         problems.append(problem)

#     return problems


import google.generativeai as genai

def analyze_educational_content():
    """
    Analyzes user-provided educational content and provides detailed insights.
    """
    # Configure Gemini
    genai.configure(api_key="AIzaSyBJBi1PEGCEt5einIk77CZYnzvbdGky7zo")
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    while True:
        print("\n=== Educational Content Analyzer ===")
        print("Select analysis type:")
        print("1. Question/Answer Analysis")
        print("2. Study Material Analysis")
        print("3. Exam Paper Analysis")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '4':
            print("Goodbye!")
            break
            
        try:
            print("\nEnter your content (type 'END' on a new line when finished):")
            content_lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                content_lines.append(line)
            
            content = "\n".join(content_lines)
            
            # Different analysis prompts based on type
            prompts = {
                '1': f"""
                Analyze this question/answer content:
                {content}
                
                Provide:
                1. Difficulty level assessment
                2. Concepts covered
                3. Common misconceptions this addresses
                4. Suggested improvements
                5. Additional practice questions
                6. Teaching tips
                """,
                
                '2': f"""
                Analyze this study material:
                {content}
                
                Provide:
                1. Content organization evaluation
                2. Key concepts covered
                3. Missing important topics
                4. Clarity assessment
                5. Suggested enhancements
                6. Additional resources needed
                7. Learning outcome alignment
                """,
                
                '3': f"""
                Analyze this exam paper:
                {content}
                
                Provide:
                1. Question distribution analysis
                2. Difficulty level breakdown
                3. Coverage of learning objectives
                4. Time allocation assessment
                5. Marking scheme evaluation
                6. Balance of question types
                7. Suggestions for improvement
                """
            }
            
            # Generate analysis
            response = model.generate_content(prompts.get(choice, "Invalid choice"))
            
            # Display results
            print("\n=== Analysis Results ===")
            print("-" * 50)
            print(response.text)
            print("-" * 50)
            
            # Option to save analysis
            save = input("\nSave this analysis to file? (yes/no): ")
            if save.lower() in ['yes', 'y']:
                filename = f"content_analysis_{choice}.txt"
                with open(filename, 'w') as f:
                    f.write("Original Content:\n")
                    f.write(content)
                    f.write("\n\nAnalysis:\n")
                    f.write(response.text)
                print(f"Analysis saved to {filename}")
            
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Please try again")
        
        # Ask to continue
        cont = input("\nAnalyze more content? (yes/no): ")
        if cont.lower() not in ['yes', 'y']:
            print("Goodbye!")
            break

if __name__ == "__main__":
    analyze_educational_content()
    
    
    
    
    
    
    # test
#     Enter your choice (1-3): 1

# Enter your content (type 'END' on a new line when finished):
# Q: Solve the quadratic equation x² + 5x + 6 = 0
# A: Step 1: Identify a=1, b=5, c=6
#    Step 2: Use factoring: (x+2)(x+3) = 0
#    Step 3: Therefore x = -2 or x = -3
# END

# 
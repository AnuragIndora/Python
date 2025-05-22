import os 

Root_Folder = "."

# List of all 100 project names
projects = [
    # Beginner Projects
    "Mad Libs Generator", "Number Guessing Game", "Rock-Paper-Scissors", "Dice Roll Simulator", "Calculator (CLI)",
    "Countdown Timer", "Password Generator", "BMI Calculator", "Unit Converter", "Tip Calculator",
    "Word & Character Counter", "Simple Interest Calculator", "Area & Perimeter Calculator", "Leap Year Checker",
    "Even/Odd Number Checker", "Multiplication Table Generator", "Palindrome Checker", "Prime Number Checker",
    "To-Do List (CLI)", "Digital Clock", "Currency Converter", "Random Joke Generator", "Typing Speed Test",
    "Quiz App (MCQ)", "Email Slicer", "Fibonacci Sequence Generator", "Calendar App", "Alarm Clock",
    "Love Calculator", "Weather Info Fetcher",

    # Intermediate Projects
    "Contact Book App", "Flashcard App (Tkinter)", "Image Resizer", "Expense Tracker", "QR Code Generator",
    "Notepad App (Tkinter)", "PDF Merger", "File Organizer Script", "Instagram Profile Scraper", "Hangman Game",
    "Pomodoro Timer", "URL Shortener", "Blog Site using Flask", "Portfolio Website", "Markdown to HTML Converter",
    "Digital Diary App", "Screenshot Taker", "Web Scraper for Product Prices", "Random Password Locker",
    "Web Crawler", "File Encryption & Decryption", "Sudoku Generator/Solver", "Chatbot", "Snake Game",
    "Tic Tac Toe", "Binary Search Visualizer", "Stack Implementation", "Queue Simulator", "Linked List Demo",
    "Priority Queue Task Manager", "Binary Tree Traversal", "LRU Cache", "Recursion Practice",
    "CSV File Analyzer", "JSON Data Viewer",

    # Advanced Projects
    "Sorting Visualizer", "Maze Solver", "Graph Traversal Visualizer", "Pathfinding Algorithms",
    "Word Ladder Solver", "Knapsack Problem GUI", "Sudoku Solver", "N-Queens Solver", "LRU Cache (Advanced)",
    "Trie Auto-Complete",

    "Flask REST API", "URL Shortener Service", "GitHub Profile Viewer", "Chat App with SocketIO",
    "API Client Library", "Twitter Bot", "Email Automation", "PDF Report Generator", "ML Prediction API",

    "File Backup Tool", "Batch Image Renamer", "Auto Email Sender", "Resume Builder", "Invoice Generator",
    "YouTube Downloader", "Custom Web Browser", "Desktop Assistant", "Excel Report Automation",
    "Selenium Web Bot",

    "EDA Dashboard", "Data Visualizer", "Linear Regression Model", "Digit Recognition",
    "Recommendation System", "Spam Classifier"
]


def create_project_structure(base_dir, project_list):
    os.makedirs(base_dir, exist_ok=True)
    for project in project_list:
        # Clean Project name for folder (remove special character)
        folder_name = project.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("-", "_")
        project_dir = os.path.join(base_dir, folder_name)
        os.makedirs(project_dir, exist_ok=True)
        
        # Create main.py file 
        with open(os.path.join(project_dir, "main.py"), "w") as f:
            f.write(f"# {project}\n\nif __name__ == '__main__':\n  pass\n")

        # Create README.md file 
        with open(os.path.join(project_dir, "README.md"), "w") as f:
            f.write(f"# {project}\n\n> Description: _Write about the project here._\n")

    print(f"Created {len(project_list)} project folders in '{base_dir}'.")


create_project_structure(Root_Folder, project_list=projects)







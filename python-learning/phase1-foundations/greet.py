import datetime
import random

# --- Step 1: Ask for the user's name ---
name = input("Hello! What is your name? ")

# --- Step 2: Get the current hour to determine time of day ---
now=datetime.datetime.now()
current_hour = now.hour
current_minute = now.minute

if current_hour < 12:
    greeting = "Good Morning"
elif current_hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

# --- Step 3: Print the greeting ---
print(f"\n{greeting}, {name}! Welcome!")
print(f"The current time is {current_hour:02d}:{current_minute:02d}.")  # prints the current time in HH:MM format

# --- Step 4: Pick a random motivational quote ---
quotes = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("You are never too old to set another goal or to dream a new dream.", "C.S. Lewis"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("I can do any damn thing that I want to do.","Stanley Joshua"),
]

quote, author = random.choice(quotes)

# --- Step 5: Print the motivational quote ---
print(f"\nHere's a quote to inspire your day:")
print(f'  "{quote}"')
print(f"  - {author}")

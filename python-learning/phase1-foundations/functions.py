# Program for learning and testing functions in Python
import math, random, datetime #importing multiple modules in one line
# Improve the program to find the current time and change the greeting according to the time of the day.
# Use the datetime module to get the current time and use if-else statements to determine the
# appropriate greeting based on the hour of the day. But it must also use functions to make the 
# code more organized and reusable. The program should also include a list of motivational quotes and 
# randomly select one to display to the user after the greeting.
def get_greeting():
    now = datetime.datetime.now()
    current_hour = now.hour
    if current_hour < 12:
        return "Good Morning"
    elif current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def get_random_quote():
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
    return random.choice(quotes)

def greet(name):
    greeting = get_greeting()
    print(f"The current time is {datetime.datetime.now().strftime('%H:%M')}.") #prints the current time in HH:MM format
    print(f"Hello {name}, {greeting}!")
    print(f"\nHere's a quote to inspire your day:")
    quote, author = get_random_quote()
    print(f'  "{quote}"')
    print(f"  - {author}")  

def main():
    name = input("What is your name? ")
    greet(name)
main()

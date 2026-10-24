
# RULE-BASED AI PYTHON CHATBOT

import datetime
import time
import random

# Get user's name
name = input("Please enter your name: ").strip()

if not name:
    name = "Friend"

# Greeting according to current time
presenthour = datetime.datetime.now().hour

if 5 <= presenthour < 12:
    print("Good morning", name)
elif 12 <= presenthour < 17:
    print("Good afternoon", name)
elif 17 <= presenthour < 21:
    print("Good evening", name)
else:
    print("Good night", name)

print("\nHello! Welcome to Rule-Based Chatbot.")
print("You can ask me basic questions and also question of python that is basic.")
print("Type 'help' for commands or 'bye' to exit.\n")

# Dictionary of responses
responses = {
    "hello": "Hi! Welcome. How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What can I do for you?",
    "how are you": "I am fine, thank you!",
    "who are you": "I am a smart rule-based AI chatbot.",
    "what is your name": "You can call me PyBot!",
    "motivate me": "Keep going! Every bug you fix makes you a better developer!",
    "happy": "Great to hear that! Keep smiling.",
    "sad": "Don't worry. Take a break and keep moving forward.",
    "what is a function": "A function is a reusable block of code.",
    "what is python": "Python is a popular programming language.",
    "what is a variable": "A variable stores a value in a program.",
    "what is a loop": "A loop repeats a block of code.",
    "what is a list": "A list stores multiple items in Python.",
    "what is a dictionary": "A dictionary stores data as key-value pairs.",
    "what is a keyword": "Keywords are reserved words in Python.",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "You're welcome!"
}

greeting_replies = [
    "Hello! How can I help you?",
    "Hi there! What would you like to know?",
    "Hey! Nice to chat with you."
]

# Store conversation history
chat_history = []


# Function to get chatbot response
def getresponsebot(userquestion):
    userquestion = userquestion.lower().strip()

    if not userquestion:
        return "Please enter a question."

    if userquestion in responses:
        if userquestion in ["hello", "hi", "hey"]:
            return random.choice(greeting_replies)
        return responses[userquestion]

    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]

    if userquestion in ["date", "today's date", "what is the date"]:
        return datetime.datetime.now().strftime(
            "Today's date is %d %B %Y."
        )

    if userquestion in ["time", "what time is it", "current time"]:
        return datetime.datetime.now().strftime(
            "The current time is %I:%M %p."
        )

    return (
        "Sorry, I don't know the answer yet. "
        "Try asking another question or type 'help'."
    )


# Main chatbot loop
while True:
    try:
        userinput = input(f"{name}: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nBot: Goodbye! Have a nice day.")
        break

    question = userinput.lower()

    if not question:
        print("Bot: Please type something!")
        continue

    if question in ["bye", "exit", "quit", "goodbye"]:
        print(f"Bot: Goodbye {name}! Have a nice day.")
        break

    if question == "help":
        print("""
Bot: Here are some things you can ask:
- Hello / Hi
- How are you?
- Who are you?
- What is Python?
- What is a function?
- What is a variable?
- Tell me a joke
- Motivate me
- Date / Time
- History
- Bye
""")
        continue

    if question == "history":
        if not chat_history:
            print("Bot: No conversation history yet.")
        else:
            print("\n--- Chat History ---")
            for old_question, old_reply in chat_history:
                print("You:", old_question)
                print("Bot:", old_reply)
            print("--------------------")
        continue

    reply = getresponsebot(userinput)

    time.sleep(0.5)
    print("Bot:", reply)

    chat_history.append((userinput, reply))

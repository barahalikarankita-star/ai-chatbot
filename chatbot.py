import random

print("Chatbot: Hello! I am your AI assistant. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day ")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot:", random.choice(["Hello!", "Hi there!", "Hey!"]))

    elif "how are you" in user_input:
        print(" Chatbot: I'm just code, but I'm doing great! ")

    elif "your name" in user_input:
        print("Chatbot: I am Ankita's AI Chatbot ")

    elif "help" in user_input:
        print("Chatbot: I can greet you, answer simple questions, and chat with you!")

    elif "ai" in user_input:
        print("Chatbot: AI stands for Artificial Intelligence ")

    elif "study" in user_input:
        print("Chatbot: Stay consistent and practice daily ")

    else:
        print("Chatbot:", random.choice([
            "Interesting!",
            "Tell me more...",
            "I didn't understand that ",
            "Can you rephrase?"
        ]))
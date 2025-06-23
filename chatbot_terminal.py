# Simple Chatbot using Dictionary

def chatbot():
    print("🤖 Chatbot: Assalamualaikum! I'm your friendly chatbot. Type 'exit' to quit.\n")

    # Dictionary of known inputs and their responses
    responses = {
        "assalamualaikum": "Wa Alaikum Assalam! 😊",
        "how are you": "I'm just code, but Alhamdulillah I'm doing great! 😄",
        "what is your name": "I'm a basic Python chatbot created by you! 🤖",
        "what can you do": "I can chat with you and respond to a few commands!",
        "who made you": "I was created by a Python learner as part of Task 3 assignment!"
    }

    while True:
        user_input = input("👤 You: ").strip().lower()

        if user_input == "exit":
            print("🤖 Chatbot: Allah Hafiz! 👋")
            break
        elif user_input in responses:
            print("🤖 Chatbot:", responses[user_input])
        else:
            print("🤖 Chatbot: Sorry, I don't understand that yet. Try something else!")

# Run the chatbot
chatbot()

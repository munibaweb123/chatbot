import chainlit as cl

# 🧠 Define fixed responses using a dictionary
responses = {
    "hi": "Hello! How can I assist you today?",
    "assalamualaikum": "Wa Alaikum Assalam! 😊",
    "how are you": "Alhamdulillah! I'm doing great. What about you?",
    "what is your name": "I'm Panaversity Chatbot, your study companion!",
    "what can you do": "I can respond to a few commands and help you stay on track!"
}

# 🔄 Default response for unknown input
default_response = "Sorry, I don't understand that yet. Try something else!"

@cl.on_chat_start
async def start():
    await cl.Message(content="Welcome to the Panaversity Custom Chatbot! 🤖\nAsk me something like 'hi', 'how are you', or 'what can you do'.").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.strip().lower()
    
    # 🔍 Check if the user input matches one of the known commands
    response = responses.get(user_input, default_response)

    # 💬 Send the matched or default response
    await cl.Message(content=response).send()

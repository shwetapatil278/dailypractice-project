
def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I am fine. Thank you!"

    elif "name" in user_input:
        return "My name is SimpleBot."

    elif "help" in user_input:
        return "I can answer simple questions."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand."


print("Simple Chatbot")
print("Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = chatbot(user)
    print("Bot:", response)

    if "bye" in user.lower():
        break

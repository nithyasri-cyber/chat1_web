# Simple Chatbot

def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "I'm doing well! How about you?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

# Chat loop
print("Welcome to Chat1! (type 'bye' to exit)")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if "bye" in user_input.lower():
        break
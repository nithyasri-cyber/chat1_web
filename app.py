from flask import Flask, render_template, request

app = Flask(__name__)

# Simple chatbot function
def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "I'm doing well! How about you?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Get response
@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)
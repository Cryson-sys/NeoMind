from flask import Flask, render_template, request
import random

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a great day!",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg').lower()
    return responses.get(user_text, "Sorry, I didn't understand that.")

if __name__ == "__main__":
    app.run(debug=True)

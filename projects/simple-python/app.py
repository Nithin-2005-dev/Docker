from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of random quotes
quotes = [
    "Believe you can and you're halfway there.",
    "You are never too old to set another goal or to dream a new dream.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
    "Do not wait to strike till the iron is hot, but make it hot by striking.",
    "The best way to predict the future is to create it."
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Random Quote API! Visit /random-quote to get a quote."})

@app.route('/random-quote')
def random_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote})



import random
import json
from flask import Flask, request, jsonify, render_template
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Load FAQ data from JSON file
with open('./data/faq_data.json', 'r') as f:
    faq_data = json.load(f)

greetings = faq_data['greetings']
farewells = faq_data['farewells']
faq = faq_data['faq']

# Set of stopwords for filtering out common words
stop_words = set(stopwords.words('english'))

# Function to check if the message is a greeting or farewell
def check_greeting_or_farewell(user_message, type='greeting'):
    user_message_tokens = word_tokenize(user_message.lower())
    check_list = greetings if type == 'greeting' else farewells
    for token in user_message_tokens:
        if token in check_list:
            return True
    return False

# Function to process user query using basic NLP techniques
def get_answer(user_query):
    user_query = user_query.lower()
    
    # Tokenize user query
    tokens = word_tokenize(user_query)
    
    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Check for keywords in filtered tokens
    for item in faq:
        question_tokens = word_tokenize(item['question'].lower())
        if all(keyword in filtered_tokens for keyword in question_tokens):
            return item['answer']
    
    return "I'm sorry, I don't have the information you're looking for. Please contact our support team for further assistance."

# Route to handle chatbot requests
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['user_message']
    if check_greeting_or_farewell(user_message, type='greeting'):
        bot_response = random.choice(greetings) + ", how can I assist you today?"
    elif check_greeting_or_farewell(user_message, type='farewell'):
        bot_response = "Goodbye! Have a great day."
    else:
        bot_response = get_answer(user_message)
    return jsonify({'bot_response': bot_response})

# Main route to render the chatbot UI
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

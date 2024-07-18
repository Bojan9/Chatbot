# Chatbot

The aim of this project was to develop a basic AI chatbot prototype that could be integrated into a SaaS model. The chatbot is designed to handle common user queries related to a specific domain using natural language processing (NLP) techniques. This report outlines the approach taken, technologies used, challenges faced, and setup instructions for testing the prototype.

## 1. Setup Instructions

### 1.1. Requirements

- Python 3.12 or higher
- Flask 2.0
- NLTK library (`pip install nltk`)

### 1.2. Steps to Run the Project

Backend Setup:

- Clone the repository containing the project file or extract the zip file provided.
- Install required Python dependencies using `pip install -r requirements.txt`.
- Set up NLTK by running Python and executing `nltk.download('punkt')` and `nltk.download('stopwords')` (provided in code) to download necessary resources.

Running the Flask App:

- Navigate to the project directory in the terminal.
- Run python app.py to start the Flask development server.

Accessing the Chatbot:

- Open a web browser and go to http://localhost:5000 to access the chatbot interface.
- Interact with the chatbot by typing queries into the input box and clicking "Send".

## 2. Technologies Used

- Python 3.12: Backend logic and NLP processing.
- Flask 2.0: Web framework for routing and handling HTTP requests.
- NLTK (Natural Language Toolkit): Python library for NLP tasks.
- JSON: Data format for storing FAQs and responses.
- HTML/CSS/JavaScript: Frontend interface for user interaction and displaying chatbot responses.

## 3. Approach

### 3.1. Functional Requirements

- Greetings and Farewells: The chatbot should handle basic greetings and farewells using predefined responses. (around 30 greetings options)
- FAQ Handling: It should answer frequently asked questions (FAQs) related to the domain using keyword matching and NLP techniques. (30 questions and answers)
- Fallback Response: Provide a fallback response for queries it cannot answer based on the FAQ database.

### 3.2. Technical Implementation

- Python: Utilized Python as the primary programming language for backend development.
- Flask: Chose Flask as the web framework for its simplicity and ease of integration with Python.
- NLTK (Natural Language Toolkit): Implemented basic NLP functionalities such as tokenization and stopwords removal using NLTK library.
- JSON: Stored FAQs and responses in a JSON format for easy retrieval and parsing.

### 3.3. Chatbot Workflow

- User Interaction: Users input queries through a web interface.
- Processing: The chatbot receives user queries, processes them using NLP techniques, and retrieves appropriate responses from the FAQ database.
- Response: Sends the response back to the user interface for display.

## 4. Challenges Faced

- NLP Accuracy: Ensuring accurate matching of user queries to relevant FAQs posed a challenge, especially with variations in user input.
- Deployment: Configuring the Flask application for deployment on different platforms and ensuring smooth integration with frontend components.
- User Experience: Designing a user-friendly interface that mimics natural conversation flow while maintaining simplicity.

## 5. Demo

![demo](https://github.com/user-attachments/assets/15157447-bb67-4468-869f-e6a06e84832f)


## 6. Conclusion

The chatbot prototype successfully demonstrates the integration of basic AI concepts into a SaaS model, providing a responsive interface for handling user queries. By leveraging Python, Flask, and NLTK, the project achieves efficient NLP-based query handling and delivers predefined responses based on stored FAQs. Future enhancements could focus on improving NLP accuracy, expanding the FAQ database, and enhancing the user interface for a more intuitive user experience.

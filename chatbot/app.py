from flask import Flask, render_template, request, jsonify
import csv
import os
import nltk
from datetime import datetime

app = Flask(__name__)

# Download necessary NLTK data
nltk.download('punkt')

# Conversation state
user_data = {}

# List of cities and museums with short forms
cities_museums = {
    'Delhi': {'National Museum': ['national', 'nm'], 'Rail Museum': ['rail', 'rm']},
    'Mumbai': {'Chhatrapati Shivaji Maharaj Vastu Sangrahalaya': ['csmvs', 'chhatrapati'], 'Dr. Bhau Daji Lad Museum': ['bdl', 'bhau', 'dbdl', 'dbdlm']},
    'Kolkata': {'Indian Museum': ['indian', 'im'], 'Victoria Memorial': ['victoria', 'vm']},
    'Chennai': {'Government Museum': ['government', 'gm'], 'Fort Museum': ['fort', 'fm']},
    'Bengaluru': {'Visvesvaraya Industrial and Technological Museum': ['vitm', 'visvesvaraya'], 'National Gallery of Modern Art': ['ngma', 'national gallery']}
}

def extract_city(message):
    words = nltk.word_tokenize(message.lower())  # Ensure case insensitivity
    for word in words:
        if word.title() in cities_museums:
            return word.title()
    return None

def extract_museum(message, city):
    words = nltk.word_tokenize(message.lower())  # Ensure case insensitivity
    museums = cities_museums.get(city, {})
    for word in words:
        for museum, aliases in museums.items():
            if word in aliases or word == museum.lower():
                return museum
    return None

def display_booking_details(user_info):
    return (
        "Booking Details:-\n"
        f"Name: {user_info['name'].title()}\n"
        f"Age: {user_info['age']}\n"
        f"Email: {user_info['email']}\n"
        f"Contact No: {user_info['phone']}\n"
        f"City: {user_info['city']}\n"
        f"Museum: {user_info['museum']}\n"
        f"Date of Visit: {user_info['visit_date']}\n"
    )

def chatbot_response(message, user_id):
    message = message.lower()  # Ensure case insensitivity
    response = ""

    if user_id not in user_data:
        user_data[user_id] = {"stage": "city", "name": "", "email": "", "phone": "", "age": "", "city": "", "museum": "", "visit_date": ""}

    state = user_data[user_id]["stage"]

    if state == "city":
        city = extract_city(message)
        if city:
            user_data[user_id]["city"] = city
            museums = ', '.join(cities_museums[city].keys())
            response = f"Great! Here are the museums in {city}: {museums}. Which museum would you like to visit?"
            user_data[user_id]["stage"] = "museum"
        else:
            response = "Please specify a valid city from our list."

    elif state == "museum":
        museum = extract_museum(message, user_data[user_id]["city"])
        if museum:
            user_data[user_id]["museum"] = museum
            response = f"Could you please provide your full name for the booking to {museum}?"
            user_data[user_id]["stage"] = "name"
        else:
            response = "Please specify a valid museum from the list."

    elif state == "name":
        user_data[user_id]["name"] = message
        response = f"Thank you, {message.title()}! Now, could you please provide your email address?"
        user_data[user_id]["stage"] = "email"

    elif state == "email":
        user_data[user_id]["email"] = message
        response = "Got it! Could you also share your phone number with us?"
        user_data[user_id]["stage"] = "phone"

    elif state == "phone":
        user_data[user_id]["phone"] = message
        response = "Thanks! Could you please provide your age?"
        user_data[user_id]["stage"] = "age"

    elif state == "age":
        user_data[user_id]["age"] = message
        response = "Great! When would you like to visit? Please provide the date in YYYY-MM-DD format."
        user_data[user_id]["stage"] = "visit_date"

    elif state == "visit_date":
        try:
            visit_date = datetime.strptime(message, '%Y-%m-%d').date()
            user_data[user_id]["visit_date"] = visit_date
            response = display_booking_details(user_data[user_id])
            save_to_csv(user_id, user_data[user_id])
            user_data[user_id] = {"stage": "city", "name": "", "email": "", "phone": "", "age": "", "city": "", "museum": "", "visit_date": ""}
        except ValueError:
            response = "The date format is incorrect. Please provide the date in YYYY-MM-DD format."

    elif "bye" in message or "goodbye" in message:
        response = "Goodbye! If you have more questions or need assistance in the future, feel free to reach out. Have a great day!"
        user_data[user_id] = {"stage": "city", "name": "", "email": "", "phone": "", "age": "", "city": "", "museum": "", "visit_date": ""}

    else:
        response = "I’m here to help! Could you please provide more details or clarify your request?"

    return response

def save_to_csv(user_id, user_info):
    file_path = os.path.join(os.getcwd(), 'bookings.csv')
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['UserID', 'Name', 'Email', 'Phone', 'Age', 'City', 'Museum', 'VisitDate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'UserID': user_id,
            'Name': user_info['name'],
            'Email': user_info['email'],
            'Phone': user_info['phone'],
            'Age': user_info['age'],
            'City': user_info['city'],
            'Museum': user_info['museum'],
            'VisitDate': user_info['visit_date']
        })

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["message"]
    user_id = request.cookies.get('user_id', 'guest')
    response = chatbot_response(user_message, user_id)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
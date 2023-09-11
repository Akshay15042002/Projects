import openai
import requests

# Set up your OpenAI API key. Replace 'YOUR_API_KEY' with your actual API key.
openai.api_key = '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'

# Define the base URL and API key for the flight details API.
FLIGHTS_API_BASE_URL = 'https://aerodatabox.p.rapidapi.com'  # Remove the specific endpoint
FLIGHTS_API_KEY = '0d8b690f2dmsh544c43393dd7470p152c3cjsn4754f7c78518'

# Define a function to get travel recommendations from GPT-3.
def get_travel_recommendation(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50  # Adjust based on your needs.
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Define a function to fetch flight details from the API.
def get_flight_details(origin, destination, date):
    try:
        # Replace this with an actual HTTP request to the flight details API.
        headers = {
            'Authorization': f'Bearer {FLIGHTS_API_KEY}',
            'X-RapidAPI-Host': 'aerodatabox.p.rapidapi.com'
        }
        params = {
            'origin': origin,
            'destination': destination,
            'date': date
        }
        response = requests.get(f'{FLIGHTS_API_BASE_URL}/flights/search', params=params, headers=headers)
        flight_details_data = response.json()
        return flight_details_data
    except Exception as e:
        return str(e)

# Main function with chat loop.
def main():
    print("Welcome to the Travel Assistant Chatbot!")
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Construct a prompt to send to OpenAI GPT-3.
        prompt = f"You: {user_input}\nChatbot:"
        if "find flight details" in user_input.lower():
            # Extract relevant information for flight details.
            origin = input("Enter the origin airport: ")
            destination = input("Enter the destination airport: ")
            date = input("Enter the date of travel: ")

            # Get flight details.
            flight_details_data = get_flight_details(origin, destination, date)

            if 'flights' in flight_details_data:
                print("Chatbot: Here are some flight details:")
                for flight in flight_details_data['flights']:
                    print(f"- {flight['flight_number']}: {flight['departure_time']} to {flight['arrival_time']}")
            else:
                print("Chatbot: Sorry, I couldn't find any flight details.")

        else:
            # Get a travel recommendation from GPT-3 based on user input.
            recommendation = get_travel_recommendation(prompt)
            print(f"Chatbot: {recommendation}")

from flask import Flask
app=Flask(__name__)
@app.route("/")
def main():
    return main

if __name__ == "__main__":
    app.run(debug=True)

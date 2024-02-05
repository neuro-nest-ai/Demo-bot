from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import google.generativeai as palm

# Init the Flask App
app = Flask(__name__)

# Initialize the Google API key
# export GOOGLE_API_KEY=YOUR API KEY
#GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# Define a function to generate answers using GPT-3
def generate_answer(question):
    #print("Received question:", question)
    #return str("Please tell the Date for YY/MM/DD of report generation")
          # Add this line for debugging

    #if "report_generation" in question:
        
    
    #else:
        # Replace 'palm' with the actual code to interact with your language model
    #response = palm.chat(messages=question, temperature=0.3, context="you are assistance bot give 3 lines")
    #content = response.messages[0]['content']  # Use index 0 instead of 1
    #return content


# Define a route to handle incoming requests
@app.route('/', methods=['POST'])
def chatgpt():
    incoming_que = request.values.get('Body', '').lower()
    print("Question: ", incoming_que)

    # Generate the answer using GPT-3
    answer = generate_answer(incoming_que)

    print("BOT Answer: ", answer)
    
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    msg.body(answer)

    return str(bot_resp)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8000)
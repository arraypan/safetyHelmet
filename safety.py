from flask import Flask, jsonify, request
from twilio.rest import TwilioRestClient


account_sid = "key"
auth_token = "key"


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Your kid is down!'




@app.route('/alexa',methods=['GET', 'POST'])
def alexaEndpoint():
    text()
    response = {
        "version": "1.0",
        "response": {
            "shouldEndSession": True,
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>Kids are down</speak>"
            }
        }
    }

    return jsonify(response)

def text():
    client = TwilioRestClient(account=account_sid, token=auth_token)
    message = client.messages.create(to="12489300075", from_="15867899227",
                                     body="Your kid is down")


if __name__ == '__main__':
    app.run()

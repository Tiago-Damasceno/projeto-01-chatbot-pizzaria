from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

print('bemvindo ao Sabor de Italia!')
app = Flask(__name__)



@app.route('/bot', methods=['POST'])
def bot():
    orignal_msg = request.values.get('body', '')
    


    print(request.values)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('bemvindo ao Sabor de Italia!')

    return str(resp)



@app.route('/')
def index():
   
     return "bemvindo ao Sabor de Italia!"


if __name__ == '__main__':
    app.run()

#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    res = makeWebhookResult(req)
    return res


def makeWebhookResult(req):
    result = req.get("result")
    parameters = result.get("parameters")    
    indicator = parameters.get("Sensors")

    speech = "Your indoor " + indicator + " is "

    if indicator == "temperature":
	speech += "23 Celsius degree, it's very comfortable now."
    elif indicator == "humidity":
	speech += "68 percent, you can turn on the dehumidifier."
    elif indicator == "co2":
	speech += "higher than 1000, please open the window and turn on the air purifier."
    elif indicator == "pm2.5":
	speech += "less than 100, don't worry."
    elif indicator == "pm10":
	speech += "less than 100, don't worry."
    elif indicator == "tvoc":
	speech += "less than 300, don't worry."
    else:
	speech += "good, don't worry."
		
    # print(json.dumps(item, indent=4))

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "airmonitor-webhook-sample-for-apiai"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')

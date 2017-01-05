# airmonitor-webhook-for-apiai
It's just a test python code to verify some ideas.

More info about Api.ai webhooks could be found here:
[Api.ai Webhook](https://docs.api.ai/docs/webhook)

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a indoor air quality information fulfillment service that uses Air Monitor.
The services takes the `Indicators` parameter from the action, performs indicator and requests indoor air quality information from Air Monitor. 

The service packs the result in the Api.ai webhook-compatible response JSON and returns it to Api.ai.

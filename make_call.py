import os
from twilio.rest import Client

account_sid = 'AC4581a7ea7f9a4108eab6fbc5c2e2d901'
auth_token = 'ef1fdbefa1dd7f12ce5b31c58762cdc5'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+18253431902',
                        from_='+15808758755'
                    )

print(call.sid)

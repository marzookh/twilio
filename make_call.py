import os
from twilio.rest import Client

account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_API_KEY'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='',
                        from_=''
                    )

print(call.sid)

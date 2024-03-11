from twilio.rest import Client
from gasdelivery.settings.base import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
)


def send_sms(to, body):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    twilio_phone_number = TWILIO_PHONE_NUMBER

    client = Client(account_sid, auth_token)

    message = client.messages.create(body=body, from_=twilio_phone_number, to=to)

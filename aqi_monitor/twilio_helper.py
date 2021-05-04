"""
 Helper Library for sending messages using twilio
 Ref: https://www.twilio.com/docs/python/install
"""
from os import environ
from twilio.rest import Client


def send_message(body: str) -> None:
    """
    Send message to the registered number with given body
    """

    account_sid = environ.get("TWILIO_ACCOUNT_SID")
    auth_token = environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"-{body}",
        from_=environ.get("FROM_MOBILE_NUMBER"),
        to=environ.get("TO_MOBILE_NUMBER"),
    )

    print(message.sid)

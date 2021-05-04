"""
Helper class to send emails using smtp library
"""
import smtplib


def send_email(body: str) -> None:
    """
    Constructs and sends an email to the recipient with the given body
    :param body: string
    """
    host = "localhost"
    server = smtplib.SMTP(host, 587)  # port 465 or 587
    server.starttls()
    from_address = "karthiksrinivaasanad@gmail.com"
    to_address = from_address
    message = f"Subject: AQI Monitor\n\n{body}"
    server.sendmail(from_address, to_address, message)

    server.close()
    print("Email Send")


if __name__ == "__main__":
    send_email(body="Hello from Karthik")

import re
from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'


# Your regex pattern for extracting amount, phone numbers, and trust
message_pattern = re.compile(r'yes (?P<amount>\d+) number (?P<phone_number>[\d\s\(\)-]+) trust (?P<trust>\w+)')

class SenderConfig:
    def __init__(self):
        pass

    def extract_data(self, message):
        message=message.split()
        UPI_traction_id=message[1]
        trust=message[2]
        return UPI_traction_id,trust

    def send_twilio_sms(self, to, body):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            to=to,
            from_=TWILIO_PHONE_NUMBER,
            body=body)
        return message


class ReplyConfig:
    def __init__(self):
        pass

    def main(self, received_message):
        sender = SenderConfig()
        UPI_traction_id,trust= sender.extract_data(received_message)
        return UPI_traction_id,trust

# Example usage
reply = ReplyConfig()
received_message = "yes erhh233783043843 trust"
print(f"Received Message: {received_message}")
data = reply.main(received_message)




import re

def is_valid_phone(number):
    pattern = r'^\d{10}$'
    return re.match(pattern, number)

def phone_required(func):
    def wrapper(number):
        if is_valid_phone(number):
            func(number)
        else:
            print("Invalid phone number!")
    return wrapper

@phone_required
def send_sms(number):
    print("SMS sent to", number)

send_sms("9876543210")
send_sms("12345")

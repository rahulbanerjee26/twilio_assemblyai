'''
    Function to work with
    the Twilio API
'''

import os
from dotenv import load_dotenv
from twilio.rest import Client

def make_phone_call(client_,from_phone_number_,to_phone_number_):
    '''
    Parameter:
        client: A twillio client instance
    Return:
        call.sid: The sid of the outgoing call
    '''
    phone_call = '''<Response>
    <Say>What's your name?</Say>
    <Record timeout="5"/>
    <Say>What's your age?</Say>
    <Record timeout="5"/>
    </Response>'''

    call = client_.calls.create(
                            record = True,
                            twiml=phone_call,
                            from_=from_phone_number_,
                            to = to_phone_number_
                        )

    return call.sid

if __name__ == '__main__':
    load_dotenv()
    account_sid = os.environ.get('account_sid')
    auth_token = os.environ.get('auth_token')
    from_phone_number = os.environ.get('from_phone_number')
    to_phone_number = os.environ.get('to_phone_number')

    client = Client(account_sid, auth_token)
    call_sid = make_phone_call(client, from_phone_number, to_phone_number)

    print(f'Call sid is {call_sid}')

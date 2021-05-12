'''
    Function to work with
    the Twilio API
'''

import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from twilio.rest import Client

def make_phone_call(client_,from_phone_number_,to_phone_number_):
    '''
    Parameter:
        client_: A twillio client instance
    Return:
        call.sid: The sid of the outgoing call
    '''
    phone_call = '''<Response>
    <Say>What are you working on?</Say>
    <Pause length="5"/>
    </Response>'''

    call = client_.calls.create(
                            record = True,
                            twiml=phone_call,
                            from_=from_phone_number_,
                            to = to_phone_number_
                        )

    return call.sid

def get_recording_sid(account_sid_,auth_token_,call_sid_):
    '''
    Parameter:
        account_sid: Twilio Account SID,
        auth_token: Twilio API Key/Auth Token
        call_sid_: Call Sid
    Return:
        recording.sid: The sid of the recording
    '''
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid_}"\
        + f'/Calls/{call_sid_}/Recordings.json'
    result = requests.get(url , auth = HTTPBasicAuth(account_sid_, auth_token_))
    recordings  = result.json()
    recording_sid = recordings['recordings'][0]['sid']
    return recording_sid

if __name__ == '__main__':
    load_dotenv()
    account_sid = os.environ.get('account_sid')
    auth_token = os.environ.get('auth_token')
    from_phone_number = os.environ.get('from_phone_number')
    to_phone_number = os.environ.get('to_phone_number')

    client = Client(account_sid, auth_token)
    call_sid = make_phone_call(client, from_phone_number, to_phone_number)

    print(f'Call sid is {call_sid}')

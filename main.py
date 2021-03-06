'''
    Script to send recording url to
    AssemblyAI and poll for status
'''

import os
from dotenv import load_dotenv
from transcribe import get_transcribe_id, get_text
from call import get_recording_sid

# Reading Data from .env file
load_dotenv()
account_sid = os.environ.get('account_sid')
call_sid = os.environ.get('call_sid')
auth_token = os.environ.get('auth_token')
assemblyai_token = os.environ.get('assemblyai_token')
recording_sid = get_recording_sid(account_sid, auth_token, call_sid)
print(f"Recording Sid: {recording_sid}")
recording_endpoint = 'https://api.twilio.com/2010-04-01/Accounts/'\
+ f'{account_sid}/Recordings/{recording_sid}.mp3'

transcribe_id = get_transcribe_id(assemblyai_token,recording_endpoint)
print(f"Transcription ID is {transcribe_id}")

result = {}
print("AssemblyAI is processing the file")
while result.get("status") != 'completed':
    result = get_text(assemblyai_token,transcribe_id)

print("Transcription Complete - The result is below")
print(result['text'])

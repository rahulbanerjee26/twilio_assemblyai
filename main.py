import requests
import os
from dotenv import load_dotenv
from transcribe import get_transcribe_id, get_text

# Reading Data from .env file
load_dotenv()
account_sid = os.environ.get('account_sid')
recording_sid = os.environ.get('recording_sid')
assemblyai_token = os.environ.get('assemblyai_token')
recording_endpoint = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}.mp3'

transcribe_id = get_transcribe_id(assemblyai_token,recording_endpoint)
print(f"Transcription ID is {transcribe_id}")
result = {}

print("AssemblyAI is processing the file")
while result.get("status") != 'completed':
            result = get_text(assemblyai_token,transcribe_id)

print("Transcription Complete - The result is below")
print(result['text'])

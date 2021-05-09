import os
from dotenv import load_dotenv
import requests

def get_transcribe_id(token,url):
  '''
    Parameter:
      token: The API key
      url  : Url to uploaded file
    Return Value:
      id   : The transcribe id of the file
  '''
  endpoint = "https://api.assemblyai.com/v2/transcript"
  json = {
    "audio_url": url
  }
  headers = {
    "authorization": token,
    "content-type": "application/json"
  }
  response = requests.post(endpoint, json=json, headers=headers)
  id = response.json()['id']
  print("Made request and file is currently queued")
  return id

def get_text(token,transcribe_id):
  '''
    Parameter: 
      token: The API key
      transcribe_id: The ID of the file which is being 
    Return Value:
      result : The response object
  '''  
  endpoint = f"https://api.assemblyai.com/v2/transcript/{transcribe_id}"
  headers = {
    "authorization": token
  }
  result = requests.get(endpoint, headers=headers).json()
  return result
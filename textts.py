
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
url= 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/b5ca51fb-56d7-4e2b-827d-3ea50ad17dc3'
apikey= 'J-PsrlP1DwzglNm-kwiEsNuAjHXmGdpKe-roAbUjjjra'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open ('churchill.txt','r') as f:
 text = f.readlines()
 text = [line.replace('\n', '') for line in text]
 text = ''.join(str(line) for line in text)
with open('./churchill.mp3', 'wb') as audio_file:
 res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
 audio_file.write(res.content)
import requests
import json
from appconfig import *
import uuid
from googletrans import Translator

class TranslateTool:
    def azure(text):
        # Add your subscription key and endpoint
        # print(text)
        subscription_key = AZURE_SUBKEY
        endpoint = AZURE_ENDPOINT

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = AZURE_LOCATION

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'from': 'ja',
            'to': TRANSLATE_TO
        }
        constructed_url = endpoint + path

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': text
        }]

        request = requests.post(
            constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        print(json.dumps(response, sort_keys=True,
            ensure_ascii=False, indent=4, separators=(',', ': ')))
        return response[0]['translations'][0]['text']

    def ibm(text):
        url = "https://www.ibm.com/demos/live/watson-language-translator/api/translate/text"
        payload = json.dumps({
            "text": text,
            "source": "ja",
            "target": TRANSLATE_TO
            }) 
        headers = {
            'Content-Type': 'application/json'}
        response = requests.request("POST", url,headers=headers, data=payload)
        data = response.json()
        print(data)

        return data['payload']['translations'][0]['translation']
    
    def googleModule(text):
        translater = Translator(service_urls=['translate.google.com'])
        translated = translater.translate(text=text, src="ja", dest="en").text
        return translated
    
    def googleDict(text):
        text = ''.join([line.strip() for line in text]) 
        # print(text)
        url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=ja&tl="+TRANSLATE_TO+"&q=" + text
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        request_result = requests.get(url, headers=headers).json()

        merged_text = []
        for b in request_result['sentences']:
            try:
                merged_text.append(b['trans'])
            except:
                pass
        print (merged_text)
        return '\n'.join([a for a in merged_text]) 

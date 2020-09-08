import os, requests, uuid, json
from flask_babel import _
from app import app


def translate(text, dest_language):
    print('text:', text)
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _("The translation service is not configured.")

    body = [{
        'text' : text
    }]

    print(body)

    headers = {
        'Ocp-Apim-Subscription-Key': '072bd9018a2145de9964dfcea26988dd',
        'Ocp-Apim-Subscription-Region': 'westeurope',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    r = requests.post('https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'
                    '&to={}'.format(dest_language),headers=headers, json=body)
    

    if r.status_code !=200:
        return _('Error: the translation service failed.')
    #return str(json.loads(r.content.decode('utf-8-sig')))
    return r.json()[0].get('translations')[0].get('text')
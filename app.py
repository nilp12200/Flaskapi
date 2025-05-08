from flask import Flask, request, Response
import json
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    if not data or 'text' not in data or 'target' not in data:
        return Response(json.dumps({'error': 'Missing text or target'}, ensure_ascii=False), mimetype='application/json')

    try:
        result = translator.translate(data['text'], src='auto', dest=data['target'])
        response_data = {
            'translated_text': result.text,
            'source_language': result.src,
            'target_language': result.dest
        }
        return Response(json.dumps(response_data, ensure_ascii=False), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}, ensure_ascii=False), mimetype='application/json')

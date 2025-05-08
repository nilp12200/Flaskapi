from flask import Flask, request, Response
import json
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()

    # Validate input
    if not data or 'q' not in data or 'target' not in data:
        return Response(json.dumps({'error': 'Missing "q" or "target" in request'}, ensure_ascii=False), mimetype='application/json'), 400

    text = data['q']
    src_lang = data.get('source', 'auto')
    dest_lang = data['target']

    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        response_data = {
            'translatedText': translated.text,
            'sourceLanguage': translated.src,
            'targetLanguage': translated.dest
        }
        return Response(json.dumps(response_data, ensure_ascii=False), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({'error': str(e)}, ensure_ascii=False), mimetype='application/json'), 500

@app.route('/languages', methods=['GET'])
def get_languages():
    return Response(json.dumps(LANGUAGES, ensure_ascii=False), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)

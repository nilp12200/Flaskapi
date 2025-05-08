from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()

    if not data or 'text' not in data or 'target' not in data:
        return jsonify({'error': 'Missing "text" or "target" field'}), 400

    text = data['text']
    target = data['target']

    try:
        result = translator.translate(text, src='auto', dest=target)
        return jsonify({
            'translated_text': result.text,
            'source_language': result.src,
            'target_language': result.dest
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify(LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)


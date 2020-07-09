from flask import Flask, Response, request, json, jsonify, make_response
from flask_api import status
from urllib.parse import unquote
import pyttsx3
from pathlib import Path
from werkzeug.utils import secure_filename

# Constants
AUDIO_DIR = 'read'

# Initialized Objects
app = Flask(__name__)
ai = pyttsx3.init()
voices = ai.getProperty('voices')
girl_voice = voices.pop()
ai.setProperty('voice', girl_voice.id)
rate = ai.getProperty('rate')
ai.setProperty('rate', rate - 1)

@app.route('/read/<encoded_phrase>', methods = ['GET'])
def read(encoded_phrase):
    phrase = unquote(encoded_phrase)
    snake_cased = phrase.replace(' ', '_')
    snake_cased = snake_cased.lower()
    file_name = AUDIO_DIR + '/' + snake_cased + '.mp3'
    file_path = Path(file_name)

    if not file_path.is_file():
        try:
            ai.save_to_file(phrase, file_name)
            ai.runAndWait()
        except:
            error = jsonify({'error_msg': 'Action Failed'})
            error.headers.add('Access-Control-Allow-Origin', '*')

            return error

    data = {'mp3_file': file_name}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/listen', methods = ['POST'])
def listen():
    try:
        my_txt = request.form['my_txt']
        my_file = request.files['my_file']
    except:
        error = jsonify({'error_msg': 'Action Failed'})
        error.headers.add('Access-Control-Allow-Origin', '*')

        return error

    my_file.save('listen/' + secure_filename(my_file.filename))

    return secure_filename(my_file.filename)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 6969)
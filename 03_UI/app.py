from typing import Annotated
import autogen
import sys, os, json
import subprocess
from datetime import datetime
from typing import Annotated
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, send_file
import time
import threading
import logging
#logging.getLogger('werkzeug').setLevel(logging.WARNING)

app = Flask(__name__)
SOUND_FOLDER = os.path.join(app.root_path, '../03_UI')


@app.route('/', methods=["GET"])
def initiate_chat():
    return render_template('index.html')  # Assuming your HTML file is named index.html

# Path to the sounds directory

# Function to load JSON data from a file
def load_json_data(path):
    with open(path, 'r') as file:
        return json.load(file)
    
@app.route('/messages', methods=['GET'])
def messages():
    try:
        # Path to the JSON file
        json_file_path = os.path.join(app.root_path, '../02_Pipeline/talk_voices_refined.json')
        # Load data from JSON file
        response_data = load_json_data(json_file_path)
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/03_UI/<path:filename>', methods=['GET'])
def voice(filename):
    # Construct the full file path
    file_path = os.path.join(SOUND_FOLDER, filename)
    # Ensure the file exists and is a WAV file
    if os.path.exists(file_path) and file_path.endswith('.wav'):
        return send_file(file_path, mimetype='audio/wav')
    else:
        return jsonify({"error": "File not found or incorrect file type"}), 404
    

@app.route('/logo/<filename>', methods=['GET'])
def logo(filename):
    # Construct the full file path
    file_path = os.path.join(os.path.join(app.root_path, 'Logo'), filename)
    # Ensure the file exists and is either a JPEG or PNG file
    if os.path.exists(file_path) and (file_path.endswith('.jpg') or file_path.endswith('.png')):
        # Determine the correct MIME type based on the file extension
        if file_path.endswith('.jpg'):
            mimetype = 'image/jpeg'
        elif file_path.endswith('.png'):
            mimetype = 'image/png'
        return send_file(file_path, mimetype=mimetype)
    else:
        return jsonify({"error": "File not found or incorrect file type"}), 404



# @app.route('/send-message', methods=["POST"])
# def send_message():
#     user_input = request.form["msg"]
#     return "Message sent successfully."


@app.route('/start-chat', methods=["POST"])
def start_chat():
    return "Chat started successfully."

if __name__ == '__main__':
    app.run(debug=True)


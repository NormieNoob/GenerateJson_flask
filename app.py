from flask import Flask, jsonify, request
from jsonGenerator import generate_json
import json
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chat', methods=['GET'])
def getChat():
    data = {'message': 'This is a sample API response'}
    return jsonify(data)

@app.route('/chat', methods=['POST'])
def postChat():

    # Get speaker name and content from request
    data = request.get_json()
    speaker = data['speaker']
    content = data['content']

    # Generate JSON data using OpenAI and function
    data = generate_json(speaker, content)

    filename = 'podcast.json'
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            podcast_json = json.load(f)
    else:
        podcast_json = []

    # Read the existing JSON data from the file
    with open(filename, 'r') as f:
        podcast_json = json.load(f)

    # Updating the Podcast json
    podcast_json.append(data)
    with open(filename, 'w') as f:
        json.dump(podcast_json, f)

    # Return the JSON data
    return jsonify(data)

if __name__ == '__main__':
    app.run()

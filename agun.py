from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Define the path to the file where keys will be stored
storage_file = 'keys.pkl'

# Load existing keys from the storage file if it exists
if os.path.exists(storage_file):
    with open(storage_file, 'rb') as f:
        valid_keys = pickle.load(f)
else:
    valid_keys = {}

# Endpoint for key check
@app.route('/key_check', methods=['GET'])
def check_key():
    key = request.args.get('key')
    if key in valid_keys:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Invalid key"})

# Endpoint for uploading a key
@app.route('/key_upload', methods=['POST'])
def upload_key():
    key = request.args.get('key')
    if key:
        valid_keys[key] = None  # You can associate data with the key if needed
        save_keys_to_storage()
        return jsonify({"status": "success", "message": "Key uploaded successfully"})
    else:
        return jsonify({"status": "error", "message": "No key provided"})

# Endpoint for removing a key
@app.route('/key_remove', methods=['POST'])
def remove_key():
    key = request.args.get('key')
    if key in valid_keys:
        del valid_keys[key]
        save_keys_to_storage()
        return jsonify({"status": "success", "message": "Key removed successfully"})
    else:
        return jsonify({"status": "error", "message": "Key not found"})

# Function to save the current keys to the storage file
def save_keys_to_storage():
    with open(storage_file, 'wb') as f:
        pickle.dump(valid_keys, f)

if __name__ == '__main__':
    app.run(debug=True)

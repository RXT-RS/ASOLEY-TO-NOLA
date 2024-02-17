from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to store valid keys and their associated data (if needed)
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
        return jsonify({"status": "success", "message": "Key uploaded successfully"})
    else:
        return jsonify({"status": "error", "message": "No key provided"})

# Endpoint for removing a key
@app.route('/key_remove', methods=['POST'])
def remove_key():
    key = request.args.get('key')
    if key in valid_keys:
        del valid_keys[key]
        return jsonify({"status": "success", "message": "Key removed successfully"})
    else:
        return jsonify({"status": "error", "message": "Key not found"})

if __name__ == '__main__':
    app.run(debug=True)

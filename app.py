from flask import Flask, request, jsonify

app = Flask(__name__)

keys = set()

@app.route('/approve', methods=['GET'])
def approve_key():
    key = request.args.get('key')
    if key:
        keys.add(key)
        return jsonify({'Status': 'Key approved successfully'})
    else:
        return jsonify({'Status': 'Key not provided'})

@app.route('/approve_key_put', methods=['GET'])
def approve_key_put():
    key = request.args.get('key')
    if key:
        keys.add(key)
        return jsonify({'Status': 'Key added successfully'})
    else:
        return jsonify({'Status': 'Key not provided'})

@app.route('/approve_key_rmv', methods=['GET'])
def approve_key_rmv():
    key = request.args.get('key')
    if key in keys:
        keys.remove(key)
        return jsonify({'Status': 'Key removed successfully'})
    else:
        return jsonify({'Status': 'Key not found'})

@app.route('/check_key', methods=['GET'])
def check_key():
    key = request.args.get('key')
    if key in keys:
        return jsonify({'Status': 'Key exists'})
    else:
        return jsonify({'Status': 'Key not found'})

if __name__ == '__main__':
    app.run(debug=True)

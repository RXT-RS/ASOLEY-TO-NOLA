from flask import Flask, request
import json

app = Flask(__name__)

all_key_file = "all_keys.json"
try:
    all_keys = open(all_key_file, "r").read()
    key_data = json.loads(all_keys)
except:
    key_data = {}

@app.route("/keys")
def showKeys():
    keys = ""
    for k, v in key_data.items():
        if v == True:
            keys += k + "<br>"
    return f"<p>{keys}</p>"

@app.route('/add_key')
def add_key():
    key = request.args.get('key')
    password = request.args.get('password')
    if password == "adminPassword123":
        if key is not None:
            key_data[key] = True
            open(all_key_file, "w").write(json.dumps(key_data))
            return json.dumps({'status': 'success', 'message': 'Key added successfully!'}), 200
        else:
            return json.dumps({'status': 'fail', 'message': 'Invalid request'}), 404
    else:
        return json.dumps({'status': 'fail', 'message': 'Action Not allowed for non admin users'}), 404

@app.route('/remove_key')
def remove_key():
    key = request.args.get('key')
    password = request.args.get('password')
    if password == "adminPassword123":
        if key is not None and key in key_data:
            del key_data[key]
            open(all_key_file, "w").write(json.dumps(key_data))
            return json.dumps({'status': 'success', 'message': 'Key removed successfully!'}), 200
        else:
            return json.dumps({'status': 'fail', 'message': 'Key not found'}), 404
    else:
        return json.dumps({'status': 'fail', 'message': 'Action Not allowed for non admin users'}), 404

@app.route('/check_key')
def check_key():
    key = request.args.get('key')
    if key is not None and key in key_data:
        return json.dumps({'status': 'success', 'message': 'Key found'}), 200
    else:
        return json.dumps({'status': 'fail', 'message': 'Key not found'}), 404

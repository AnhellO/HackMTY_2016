from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import make_response
from flask.ext.httpauth import HTTPBasicAuth
import json

app = Flask(__name__)


trucks = {}
# ============== Authentication =================
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'hack_mty':
        return 'pumas'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

# ============== Data input ================

@app.route('/truck', methods=['POST'])
@auth.login_required
def new_pos():
    global trucks
    if not request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'timestamp': request.json['timestamp'],
        'pos': request.json['pos']
    }
    if task['id'] not in trucks:
        trucks[task['id']] = task
    else:
        trucks[task['id']] = task

    return jsonify({'task': task}), 201

# ============ Data output =================

@app.route("/data")
def data():
    result = {'trucks': [trucks[x] for x in trucks.keys()]}
    #turn the results into valid JSON
    return jsonify(result)

@app.route('/')
def get_students():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

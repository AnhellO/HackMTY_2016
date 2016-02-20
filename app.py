from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/data")
def data():
    result = { "truks": [
        {"id": "camioncito 1",
        "timestamp": "2016-02-20T07:30:00.000-05:00",
        "pos": [-83.802763999999996, 44.56084749]
        },
        {"id": "camioncito 2",
        "timestamp": "2016-02-20T07:30:00.000-05:00",
        "pos": [-83.822763999999996, 44.52084749]
        },
    ]}
    #turn the results into valid JSON
    return jsonify(result)

@app.route('/')
def get_students():
    return 'hola tocayo'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

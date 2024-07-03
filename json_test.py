from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/data')
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

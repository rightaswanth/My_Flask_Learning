from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route('/user/<name>')
def hello_world(name):
    return f"Hello World, I am {escape(name)}"

@app.route('/user/post/<int:pin_id>')
def get_pin(pin_id):
    return f"{pin_id}"

@app.route('/user/<user_name>/<place>/<int:pin>')
def address(user_name, place, pin):
    return f"My name is {escape(user_name)} . I am From {escape(place)} . Pin code is {pin}"


if __name__ == '__main__':

    app.run(debug=True)
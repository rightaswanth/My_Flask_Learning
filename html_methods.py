from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return f"Login Succeses Full"
    else:
        return f"Http method is not valid"



if __name__ == '__main__':

    app.run(debug=True)
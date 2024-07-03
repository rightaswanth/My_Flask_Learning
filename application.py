from  flask import Flask,request,redirect,render_template

app = Flask(__name__)


@app.route('/hello/', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        data = request.data
        return f"Post request is succefull "
    else:
        return "Invalid Request"

if __name__ == '__main__':
    with app.test_request_context('/hello',method='GET'):
        assert request.path == '/hello'
        assert request.method == 'GET'
        print("Test request context is working correctlly")

    app.run(debug=True)



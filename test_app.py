from flask import Flask,request,render_template_string,render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return "Invalid request"




if __name__ == '__main__':

    app.run(debug=True)

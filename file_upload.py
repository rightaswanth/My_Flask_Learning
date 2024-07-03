from flask import Flask,request

app = Flask(__name__)

@app.route('/uploads', methods=['GET','POST'])
def file_enter():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/home/aswanth/PycharmProjects/My_Flask_Learning/new_numbers.txt')
        return f"File Uploaded Succesfully"



if __name__ == '__main__':

    app.run(debug=True)
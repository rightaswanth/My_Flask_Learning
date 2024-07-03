import  requests
my_files = {'file':open('number.txt','rb+')}
x = requests.post( 'http://127.0.0.1:5000/uploads',files=my_files)

print(x.status_code)
print(x.text)
print(x.request)
print(x.headers)
print(x)
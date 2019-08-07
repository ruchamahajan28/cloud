from flask import Flask
application = Flask(__NAME__)

@application.route('/')
def hello_world():
    return "Hello World in Python, Run as a POD in OpenShift\r\n", 200,
{ 'Content-Tpye': 'text/plain'}

if __name__ == "main":
    application.run(debug = True) 

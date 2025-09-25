from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "hello"

@app.route('/post/')
def index():
    return "hellopost"

if __name__=="__main__":
    app.run(debug=True)
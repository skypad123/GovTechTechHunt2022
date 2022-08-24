from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/one', methods = ['POST'])
def one():
    # CODE
    return None

@app.route('/two', methods = ['POST'])
def two():
    # CODE
    return None

if __name__ == '__main__':
    app.run()
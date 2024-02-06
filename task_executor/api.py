from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def main():
    app.run(debug=True, host='127.0.0.1', port=5000)


if __name__ == '__main__':
   main()

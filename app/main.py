from flask import Flask

# create sample api
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


# run app
if __name__ == "__main__":
    app.run(debug=True, port=8080)

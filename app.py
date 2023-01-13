from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome_to_itec():
    return {
        "message" : "Welcome to ITEC Mataram"
    }





if "__main__" == __name__:
    app.run(debug=True, port=2000)
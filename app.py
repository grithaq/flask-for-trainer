from flask import Flask

app = Flask(__name__)

list_pendaftar = []

@app.route("/")
def welcome_to_itec():
    return {
        "message" : "Welcome to ITEC Mataram"
    }

@app.route("/pendaftar")
def semua_pendaftar():
    return {
        "Pendaftar" : list_pendaftar
    }



if "__main__" == __name__:
    app.run(debug=True, port=2000)
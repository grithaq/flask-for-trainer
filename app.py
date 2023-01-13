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


@app.route('/tambah_peserta/<nama>')
def tambah_peserta(nama):
    list_pendaftar.append(nama)
    return {
        "message": f"List Pendaftar berhasil di update : {list_pendaftar}"
    }


@app.route("/delete/<nama>")
def delete_peserta(nama):
    list_pendaftar.remove(nama)
    return {
        "message": f"{nama} berhasil di hapus"
    }





if "__main__" == __name__:
    app.run(debug=True, port=2000)
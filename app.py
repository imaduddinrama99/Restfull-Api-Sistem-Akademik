from flask import Flask, render_template, request, redirect, url_for, flash
from supabase import create_client

app = Flask(__name__)
# Wajib menambahkan secret_key untuk mengaktifkan fitur flash message
app.secret_key = "kunci_rahasia_sistem_akademik"

url = "https://xsyqxfsorojdfvvxcqxz.supabase.co"
key = "sb_publishable_xUpq-I2dyYcPOxcopHWcGQ__PASVFai"

supabase = create_client(url, key)

@app.route("/")
def home():
    response = (
        supabase
        .table("mahasiswa")
        .select("*")
        .execute()
    )
    return render_template(
        "index.html",
        mahasiswa=response.data
    )

@app.route("/tambah", methods=["POST"])
def tambah_mahasiswa():
    nim = request.form.get("nim")
    nama = request.form.get("nama")
    prodi = request.form.get("prodi")
    angkatan = request.form.get("angkatan")

    supabase.table("mahasiswa").insert({
        "nim": nim,
        "nama": nama,
        "prodi": prodi,
        "angkatan": int(angkatan) if angkatan else None
    }).execute()

    # Mengirim notifikasi sukses tambah data ke frontend
    flash({"title": "Berhasil!", "text": "Data mahasiswa berhasil ditambahkan.", "icon": "success"})
    return redirect(url_for("home"))

@app.route("/edit/<id>")
def edit_mahasiswa(id):
    response = supabase.table("mahasiswa").select("*").eq("id", id).execute()
    if response.data:
        return render_template("edit.html", mhs=response.data[0])
    return redirect(url_for("home"))

@app.route("/update/<id>", methods=["POST"])
def update_mahasiswa(id):
    nim = request.form.get("nim")
    nama = request.form.get("nama")
    prodi = request.form.get("prodi")
    angkatan = request.form.get("angkatan")

    supabase.table("mahasiswa").update({
        "nim": nim,
        "nama": nama,
        "prodi": prodi,
        "angkatan": int(angkatan) if angkatan else None
    }).eq("id", id).execute()

    # Mengirim notifikasi sukses update data ke frontend
    flash({"title": "Berhasil Diperbarui!", "text": "Data mahasiswa berhasil diubah.", "icon": "success"})
    return redirect(url_for("home"))

@app.route("/hapus/<id>")
def hapus_mahasiswa(id):
    supabase.table("mahasiswa").delete().eq("id", id).execute()
    
    # Mengirim notifikasi sukses hapus data ke frontend
    flash({"title": "Terhapus!", "text": "Data mahasiswa telah dihapus.", "icon": "success"})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
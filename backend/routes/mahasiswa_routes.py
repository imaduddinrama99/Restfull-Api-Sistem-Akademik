from flask import Blueprint, request, jsonify
from services import mahasiswa_service

mahasiswa_bp = Blueprint('mahasiswa', __name__)

# Menggunakan /mahasiswa secara eksplisit
@mahasiswa_bp.route("/mahasiswa", methods=["GET"])
def get_mahasiswa():
    try:
        data = mahasiswa_service.get_all()
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@mahasiswa_bp.route("/mahasiswa/<id>", methods=["GET"])
def get_detail(id):
    try:
        data = mahasiswa_service.get_by_id(id)
        if data:
            return jsonify({"status": "success", "data": data}), 200
        return jsonify({"status": "error", "message": "Data tidak ditemukan"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@mahasiswa_bp.route("/mahasiswa", methods=["POST"])
def tambah():
    try:
        payload = request.json
        data_baru = {
            "nim": payload.get("nim"),
            "nama": payload.get("nama"),
            "prodi": payload.get("prodi"),
            "angkatan": int(payload.get("angkatan")) if payload.get("angkatan") else None
        }
        mahasiswa_service.insert(data_baru)
        return jsonify({"status": "success", "message": "Berhasil ditambahkan"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@mahasiswa_bp.route("/mahasiswa/<id>", methods=["PUT"])
def edit(id):
    try:
        payload = request.json
        data_update = {
            "nim": payload.get("nim"),
            "nama": payload.get("nama"),
            "prodi": payload.get("prodi"),
            "angkatan": int(payload.get("angkatan")) if payload.get("angkatan") else None
        }
        mahasiswa_service.update(id, data_update)
        return jsonify({"status": "success", "message": "Berhasil diubah"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@mahasiswa_bp.route("/mahasiswa/<id>", methods=["DELETE"])
def hapus(id):
    try:
        mahasiswa_service.delete(id)
        return jsonify({"status": "success", "message": "Berhasil dihapus"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
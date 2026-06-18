from flask import Flask
from flask_cors import CORS

# Import blueprint dari folder routes
from routes.mahasiswa_routes import mahasiswa_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

# Konfigurasi CORS agar tidak diblokir browser
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Daftarkan blueprint dengan prefix /api saja (lebih aman dari bug garis miring)
app.register_blueprint(mahasiswa_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
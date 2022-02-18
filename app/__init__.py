from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.model.user import User
from app.model.unit import Unit
from app.model.barang_satuan import BarangSatuan
from app.model.barang_kategori import BarangKategori
from app.model.armada_jenis import ArmadaJenis
from app import routes
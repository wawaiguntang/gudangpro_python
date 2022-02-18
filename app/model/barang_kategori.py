from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class BarangKategori(db.Model):
    __tablename__ = 'tbl_barang_kategori'
    idkategori = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nmkategori = db.Column(db.String(60), nullable=False)
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value, nullable=False)

    def to_json(self):
        json_user = {
            'idkategori': self.idkategori,
            'nmkategori': self.nmkategori,
            'publish': self.publish
        }

        return json_user

    def __repr__(self):
        return '<BarangKategori {}>'.format(self.idkategori)  
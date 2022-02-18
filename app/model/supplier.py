from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Supplier(db.Model):
    __tablename__ = 'tbl_supplier'
    idsupplier = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kdsupplier = db.Column(db.String(5), nullable=False)
    nmsupplier = db.Column(db.String(75), nullable=False)
    nmperson = db.Column(db.String(50), nullable=False)
    notelp = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    alamat_jalan = db.Column(db.String(75), nullable=True)
    kabupaten = db.Column(db.String(50), nullable=True)
    provinsi = db.Column(db.String(50), default="LAMPUNG", server_default="LAMPUNG", nullable=True)
    negara = db.Column(db.String(50), default="INDONESIA", server_default="INDONESIA", nullable=True)
    deposit = db.Column(db.Integer(11), default="0", server_default="0", nullable=False)
    rec_insert
    rec_update
    iduser
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)

    def to_json(self):
        json_user = {
            'iduser': self.iduser,
            'email': self.email,
            'password': self.password,
            'foto': self.foto,
            'level': self.level,
            'publish': self.publish
        }

        return json_user

    def __repr__(self):
        return '<User {}>'.format(self.iduser)  
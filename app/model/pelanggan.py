from app import db
import enum
from datetime import datetime  

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Pelanggan(db.Model):
    __tablename__ = 'tbl_pelanggan'
    idpelanggan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kdpelanggan = db.Column(db.String(5), nullable=False)
    nmpelanggan = db.Column(db.String(75), nullable=False)
    notelp = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    alamat_jalan = db.Column(db.String(75), nullable=True)
    kabupaten = db.Column(db.String(50), nullable=True)
    provinsi = db.Column(db.String(50), default="LAMPUNG", server_default="LAMPUNG", nullable=True)
    negara = db.Column(db.String(50), default="INDONESIA", server_default="INDONESIA", nullable=True)
    deposit = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    p_discount = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    rec_insert = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    rec_update = db.Column(db.DateTime, nullable=True )
    
    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), default="0", server_default="0")
    parent = db.relationship("User", back_populates="children")
    
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)
    
    children = db.relationship("TransaksiPenjualan", back_populates="parent")
    
    def to_json(self):
        json_pelanggan = {
            'idpelanggan': self.idpelanggan,
            'kdpelanggan': self.kdpelanggan,
            'nmpelanggan': self.nmpelanggan,
            'notelp': self.notelp,
            'email': self.email,
            'alamat_jalan': self.alamat_jalan,
            'kabupaten': self.kabupaten,
            'provinsi': self.provinsi,
            'negara': self.negara,
            'deposit': self.deposit,
            'p_discount': self.p_discount,
            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
            'iduser': self.iduser,
            'publish': self.publish
        }

        return json_pelanggan

    def __repr__(self):
        return '<Pelanggan {}>'.format(self.idpelanggan)  
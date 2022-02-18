from app import db
import enum
import datetime

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
    deposit = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    rec_insert = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    rec_update = db.Column(db.DateTime, nullable=True )
    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), default="0", server_default="0")
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)
    parent = db.relationship("User", back_populates="children")
    
    
    def to_json(self):
        json_supplier = {
            'idsupplier': self.idsupplier,
            'kdsupplier': self.kdsupplier,
            'nmsupplier': self.nmsupplier,
            'nmperson': self.nmperson,
            'notelp': self.notelp,
            'email': self.email,
            'alamat_jalan': self.alamat_jalan,
            'kabupaten': self.kabupaten,
            'provinsi': self.provinsi,
            'negara': self.negara,
            'deposit': self.deposit,
            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
            'iduser': self.iduser,
            'publish': self.publish
        }

        return json_supplier

    def __repr__(self):
        return '<Supplier {}>'.format(self.idsupplier)  
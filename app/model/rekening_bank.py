from app import db
import enum
from datetime import datetime  

class Publish(enum.Enum):
    T = "T"
    F = "F"

class RekeningBank(db.Model):
    __tablename__ = 'tbl_rekening_bank'
    idrekeningbank = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    norekening = db.Column(db.String(20), nullable=False)
    nmbank = db.Column(db.String(50), nullable=False)
    cabang = db.Column(db.String(75), nullable=False)
    nmnasabah = db.Column(db.String(75), nullable=False)
    rec_insert = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    rec_update = db.Column(db.DateTime, nullable=True )

    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), default="0", server_default="0")
    parent = db.relationship("User", back_populates="children")

    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)
    
    children = db.relationship("TransaksiPenjualanPembayaran", back_populates="parent")

    
    def to_json(self):
        json_supplier = {
            'idrekeningbank': self.idrekeningbank,
            'norekening': self.norekening,
            'nmbank': self.nmbank,
            'cabang': self.cabang,
            'nmnasabah': self.nmnasabah,
            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
            'iduser': self.iduser,
            'publish': self.publish
        }

        return json_supplier

    def __repr__(self):
        return '<RekeningBank {}>'.format(self.idrekeningbank)  
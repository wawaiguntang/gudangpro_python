from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class MetodeBayar(db.Model):
    __tablename__ = 'tbl_metode_bayar'
    idmetode_bayar = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    metode_bayar = db.Column(db.String(60), nullable=False)
    publish = db.Column(db.Enum(Publish),default=Publish.T.value, server_default=Publish.T.value, nullable=False)

    children = db.relationship("TransaksiPenjualanPembayaran", back_populates="parent")

    def to_json(self):
        json_metode_bayar = {
            'idmetode_bayar': self.idmetode_bayar,
            'metode_bayar': self.metode_bayar,
            'publish': self.publish
        }

        return json_metode_bayar

    def __repr__(self):
        return '<MetodeBayar {}>'.format(self.idmetode_bayar)  
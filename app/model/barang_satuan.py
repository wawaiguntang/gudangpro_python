from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class BarangSatuan(db.Model):
    __tablename__ = 'tbl_barang_satuan'
    idsatuan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nmsatuan = db.Column(db.String(60),  nullable=False)
    satuan = db.Column(db.String(60), nullable=False)
    kilogram = db.Column(db.Numeric(10,0), default="0", server_default="0", nullable=False)
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value, nullable=False)

    children = db.relationship("Barang", back_populates="parent")

    def to_json(self):
        json_barang_satuan = {
            'idsatuan': self.idsatuan,
            'nmsatuan': self.nmsatuan,
            'satuan' : self.satuan,
            'kilogram' : self.kilogram,
            'publish': self.publish
        }

        return json_barang_satuan

    def __repr__(self):
        return '<BarangSatuan {}>'.format(self.idsatuan)  
from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class StatusBayar(db.Model):
    __tablename__ = 'tbl_status_bayar'
    idstatus_bayar = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    status_bayar = db.Column(db.String(30), nullable=False)
    publish = db.Column(db.Enum(Publish),default=Publish.T.value, server_default=Publish.T.value, nullable=False)

    children = db.relationship("TransaksiPenjualanPembayaran", back_populates="parent")

    def to_json(self):
        json_status_bayar = {
            'idstatus_bayar': self.idstatus_bayar,
            'status_bayar': self.status_bayar,
            'publish': self.publish
        }

        return json_status_bayar

    def __repr__(self):
        return '<StatusBayar {}>'.format(self.idstatus_bayar)  
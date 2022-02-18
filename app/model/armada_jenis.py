from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class ArmadaJenis(db.Model):
    __tablename__ = 'tbl_armada_jenis'
    idjenis_armada = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nmjenis_armada = db.Column(db.String(60), nullable=False)
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value, nullable=False)

    def to_json(self):
        json_armada_jenis = {
            'idjenis_armada': self.idjenis_armada,
            'nmjenis_armada': self.nmjenis_armada,
            'publish': self.publish
        }

        return json_armada_jenis

    def __repr__(self):
        return '<ArmadaJenis {}>'.format(self.idjenis_armada)  
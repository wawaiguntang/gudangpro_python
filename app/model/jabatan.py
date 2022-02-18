from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Jabatan(db.Model):
    __tablename__ = 'tbl_jabatan'
    idjabatan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nmjabatan = db.Column(db.String(60), nullable=False)
    publish = db.Column(db.Enum(Publish),default=Publish.T.value, server_default=Publish.T.value, nullable=False)

    def to_json(self):
        json_user = {
            'idjabatan': self.idjabatan,
            'nmjabatan': self.nmjabatan,
            'publish': self.publish
        }

        return json_user

    def __repr__(self):
        return '<Jabatan {}>'.format(self.idjabatan)  
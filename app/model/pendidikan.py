from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Pendidikan(db.Model):
    __tablename__ = 'tbl_pendidikan'
    idpendidikan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nmpendidikan = db.Column(db.String(60), nullable=True)
    alias = db.Column(db.String(50), nullable=True)
    publish = db.Column(db.Enum(Publish),default=Publish.T.value, server_default=Publish.T.value, nullable=False)

    def to_json(self):
        json_user = {
            'idpendidikan': self.idpendidikan,
            'nmpendidikan': self.nmpendidikan,
            'alias': self.alias,
            'publish': self.publish
        }

        return json_user

    def __repr__(self):
        return '<Pendidikan {}>'.format(self.idpendidikan)  
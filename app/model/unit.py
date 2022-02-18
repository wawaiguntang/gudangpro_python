from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Unit(db.Model):
    __tablename__ = 'tbl_unit'
    idunit = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nmunit = db.Column(db.String(60), nullable=False)
    publish = db.Column(db.Enum(Publish),default=Publish.T.value, server_default=Publish.T.value, nullable=False)

    def to_json(self):
        json_user = {
            'idunit': self.idunit,
            'nmunit': self.nmunit,
            'publish': self.publish
        }

        return json_user

    def __repr__(self):
        return '<Unit {}>'.format(self.idunit)  
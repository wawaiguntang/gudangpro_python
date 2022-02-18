from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Level(enum.Enum):
    Pelanggan = "Pelanggan"
    Administrator = "Administrator"
    Manajer = "Manajer"
    Keuangan = "Keuangan"
    Gudang = "Gudang"
    SuperAdmin = "SuperAdmin"

class User(db.Model):
    __tablename__ = 'tbl_user'
    iduser = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    foto = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Enum(Level), nullable=False)
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)

    children = db.relationship("Supplier", back_populates="parent")
    children = db.relationship("Staf", back_populates="parent")

    def to_json(self):
        json_user = {
            'iduser': self.iduser,
            'email': self.email,
            'password': self.password,
            'foto': self.foto,
            'level': self.level,
            'publish': self.publish
        }

        return json_user

    def __repr__(self):
        return '<User {}>'.format(self.iduser)  
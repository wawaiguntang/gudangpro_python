from app import db
import enum
import datetime

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Sex(enum.Enum):
    L = "L"
    P = "P"

class Staf(db.Model):
    __tablename__ = 'tbl_staf'
    idstaf = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kdstaf = db.Column(db.String(6), nullable=False)
    nmstaf = db.Column(db.String(75), nullable=False)
    nik = db.Column(db.String(50), nullable=False)
    tempat_lahir = db.Column(db.String(30), nullable=False)
    tanggal_lahir = db.Column(db.Date, nullable=True)
    sex = db.Column(db.Enum(Sex), nullable=False)
    notelp = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    alamat_jalan = db.Column(db.String(75), nullable=True)
    kabupaten = db.Column(db.String(50), nullable=True)
    provinsi = db.Column(db.String(50), default="LAMPUNG", server_default="LAMPUNG", nullable=True)
    negara = db.Column(db.String(50), default="INDONESIA", server_default="INDONESIA", nullable=True)
    tgl_masuk = db.Column(db.Date, nullable=True)
    tgl_berhenti = db.Column(db.Date, nullable=True)

    idjabatan = db.Column(db.BigInteger, db.ForeignKey('tbl_jabatan.idjabatan'), default="0", server_default="0")
    parent = db.relationship("Jabatan", back_populates="children")

    idunit = db.Column(db.BigInteger, db.ForeignKey('tbl_unit.idunit'), default="0", server_default="0")
    parent = db.relationship("Unit", back_populates="children")

    idpendidikan = db.Column(db.BigInteger, db.ForeignKey('tbl_pendidikan.idpendidikan'), default="0", server_default="0")
    parent = db.relationship("Pendidikan", back_populates="children")

    rec_insert = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    rec_update = db.Column(db.DateTime, nullable=True )

    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), default="0", server_default="0")
    parent = db.relationship("User", back_populates="children")

    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)
    
    
    def to_json(self):
        json_staf = {
            'idstaf': self.idstaf,
            'kdstaf': self.kdstaf,
            'nmstaf': self.nmstaf,
            'nik': self.nik,
            'tempat_lahir': self.tempat_lahir,
            'tanggal_lahir': self.tanggal_lahir,
            'sex': self.sex,
            'notelp': self.notelp,
            'email': self.email,
            'alamat_jalan': self.alamat_jalan,
            'kabupaten': self.kabupaten,
            'provinsi': self.provinsi,
            'negara': self.negara,
            'tgl_masuk': self.tgl_masuk,
            'tgl_berhenti': self.tgl_berhenti,
            'idjabatan' : self.idjabatan,
            'idunit' : self.idunit,
            'idpendidikan' : self.idpendidikan,
            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
            'iduser': self.iduser,
            'publish': self.publish
        }

        return json_staf

    def __repr__(self):
        return '<Staf {}>'.format(self.idstaf)  
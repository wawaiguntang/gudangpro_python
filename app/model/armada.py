from unicodedata import name
from app import db
import enum

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Armada(db.Model):
    __tablename__ = 'tbl_armada'
    idarmada = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kdarmada = db.Column(db.String(10), nullable=True)
    nomor_plat = db.Column(db.String(11), nullable=True)

    idjenis_armada = db.Column(db.BigInteger, db.ForeignKey('tbl_armada_jenis.idjenis_armada'), default="0", server_default="0",nullable=False)
    parent = db.relationship("ArmadaJenis", back_populates="children")

    daya_angkut = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    nostnk = db.Column(db.String(30), nullable=True)
    tglpajak = db.Column(db.Date, nullable=True)

    idstaf = db.Column(db.BigInteger, db.ForeignKey('tbl_staf.idstaf'), default="0", server_default="0")
    parent = db.relationship("Staf", back_populates="children")

    kondisi_armada = db.Column(db.Enum("BAIK","RUSAK-RINGAN","RUSAK-BERAT", "PERBAIKAN", name="KondisiArmada"), default="BAIK", server_default="BAIK",nullable=False)
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)
    
    children = db.relationship("TransaksiPenjualanDo", back_populates="parent")
    
    def to_json(self):
        json_armada = {
            'idarmada': self.idarmada,
            'kdarmada': self.kdarmada,
            'nomor_plat': self.nomor_plat,
            'idjenis_armada': self.idjenis_armada,
            'daya_angkut': self.daya_angkut,
            'nostnk': self.nostnk,
            'tglpajak': self.tglpajak,
            'idstaf': self.idstaf,
            'kondisi_armada': self.kondisi_armada,
            'publish': self.publish
        }

        return json_armada

    def __repr__(self):
        return '<Armada {}>'.format(self.idarmada)  
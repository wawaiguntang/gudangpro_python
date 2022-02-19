from app import db
import enum
from datetime import datetime  

class Publish(enum.Enum):
    T = "T"
    F = "F"

class Barang(db.Model):
    __tablename__ = 'tbl_barang'
    idbarang = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kdbarang = db.Column(db.String(10), nullable=False)
    nmbarang = db.Column(db.String(75), nullable=False)
    merek = db.Column(db.String(75), nullable=False)

    idkategori = db.Column(db.BigInteger, db.ForeignKey('tbl_barang_kategori.idkategori'), default="0", server_default="0", nullable=False)
    parent = db.relationship("BarangKategori", back_populates="children")

    idsatuan = db.Column(db.BigInteger, db.ForeignKey('tbl_barang_satuan.idsatuan'), default="0", server_default="0", nullable=False)
    parent = db.relationship("BarangSatuan", back_populates="children")

    idsupplier = db.Column(db.BigInteger, db.ForeignKey('tbl_supplier.idsupplier'), nullable=False)
    parent = db.relationship("Supplier", back_populates="children")

    tonase = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    harga_net = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    harga_jual = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    stok = db.Column(db.Integer, default="0", server_default="0", nullable=False)

    rec_insert = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    rec_update = db.Column(db.DateTime, nullable=True )

    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), default="0", server_default="0")
    parent = db.relationship("User", back_populates="children")

    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)
    
    children = db.relationship("TransaksiPenjualanDetail", back_populates="parent")

    
    def to_json(self):
        json_barang = {
            'idbarang': self.idbarang,
            'kdbarang': self.kdbarang,
            'nmbarang': self.nmbarang,
            'merek': self.merek,
            'idkategori': self.idkategori,
            'idunit': self.idunit,
            'idsupplier': self.idsupplier,
            'tonase': self.tonase,
            'harga_net': self.harga_net,
            'harga_jual': self.harga_jual,
            'stok': self.stok,
            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
            'iduser': self.iduser,
            'publish': self.publish
        }

        return json_barang

    def __repr__(self):
        return '<Barang {}>'.format(self.idbarang)  
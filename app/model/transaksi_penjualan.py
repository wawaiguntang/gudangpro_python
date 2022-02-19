from unicodedata import name
from app import db
import enum
from datetime import datetime  

class Publish(enum.Enum):
    T = "T"
    F = "F"

class TransaksiPenjualan(db.Model):
    __tablename__ = 'tbl_transaksi_penjualan'
    idt_penjualan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nofaktur = db.Column(db.String(13), nullable=False)
    tgl_transaksi = db.Column(db.Date, nullable=False)

    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), nullable=False)
    parent = db.relationship("User", back_populates="children")

    idpelanggan = db.Column(db.BigInteger, db.ForeignKey('tbl_pelanggan.idpelanggan'), nullable=False)
    parent = db.relationship("Pelanggan", back_populates="children")

    keterangan = db.Column(db.String(255), nullable=True)
    total = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    jenis_do = db.Column(db.Enum("TAKEIT",'DELIVERY','KURIR'),default="TAKEIT", server_default="TAKEIT", nullable=False)
    rec_insert = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    rec_update = db.Column(db.DateTime, nullable=True )
    rec_delete = db.Column(db.DateTime, nullable=True )
    status_delete = db.Column(db.Enum("1","0", name="StatusDelete"), default="0", server_default="0",nullable=False )

    delay = db.Column(db.Enum(Publish), default=Publish.F.value, server_default=Publish.F.value,nullable=False)
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)

    children = db.relationship("TransaksiPenjualanDo", back_populates="parent")
    children = db.relationship("TransaksiPenjualanDetail", back_populates="parent")
    children = db.relationship("TransaksiPenjualanPembayaran", back_populates="parent")

    def to_json(self):
        json_t_penjualan = {
            'idt_penjualan': self.idt_penjualan,
            'nofaktur': self.nofaktur,
            'tgl_transaksi': self.tgl_transaksi,
            'iduser': self.iduser,
            'idpelanggan': self.idpelanggan,

            'keterangan': self.keterangan,
            'total': self.total,
            'jenis_do': self.jenis_do,
            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
            'rec_delete': self.rec_delete,
            'status_delete': self.status_delete,
       
            'delay': self.delay,
            'publish': self.publish
        }

        return json_t_penjualan

    def __repr__(self):
        return '<TransaksiPenjualan {}>'.format(self.idt_penjualan)  
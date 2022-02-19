from unicodedata import name
from app import db
import enum
from datetime import datetime  

class Publish(enum.Enum):
    T = "T"
    F = "F"

class TransaksiPenjualanDetail(db.Model):
    __tablename__ = 'tbl_transaksi_penjualan_detail'
    idtd_penjualan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)

    idt_penjualan = db.Column(db.BigInteger, db.ForeignKey('tbl_transaksi_penjualan.idt_penjualan'), nullable=False)
    parent = db.relationship("TransaksiPenjualan", back_populates="children")


    idbarang = db.Column(db.BigInteger, db.ForeignKey('tbl_barang.idbarang'), nullable=False)
    parent = db.relationship("Barang", back_populates="children")

    harga_jual = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    qty = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    tonase = db.Column(db.Integer, default="0", server_default="0", nullable=False)
    discount = db.Column(db.Integer, default="0", server_default="0", nullable=False)

    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), nullable=False)
    parent = db.relationship("User", back_populates="children")

    
    rec_insert = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    rec_update = db.Column(db.DateTime, nullable=True )

    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)
    
    children = db.relationship("Barang", back_populates="parent")
    
    def to_json(self):
        json_t_penjualan = {
            'idtd_penjualan': self.idtd_penjualan,
            'idt_penjualan': self.idt_penjualan,
            'idbarang': self.idbarang,
            'harga_jual': self.harga_jual,
            'qty': self.qty,

            'tonase': self.tonase,
            'discount': self.discount,
            'iduser': self.iduser,
            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
       
            'publish': self.publish
        }

        return json_t_penjualan

    def __repr__(self):
        return '<TransaksiPenjualanDetail {}>'.format(self.idtd_penjualan)  
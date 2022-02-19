from unicodedata import name
from app import db
import enum
from datetime import datetime  

class Publish(enum.Enum):
    T = "T"
    F = "F"

class TransaksiPenjualanPembayaran(db.Model):
    __tablename__ = 'tbl_transaksi_penjualan_pembayaran'
    idtp_penjualan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kdtp_penjualan = db.Column(db.String(13), nullable=True)
    
    idt_penjualan = db.Column(db.BigInteger, db.ForeignKey('tbl_transaksi_penjualan.idt_penjualan'), nullable=False)
    parent = db.relationship("TransaksiPenjualan", back_populates="children")
    
    tgl_pembayaran = db.Column(db.Date, nullable=False)

    idmetode_bayar = db.Column(db.BigInteger, db.ForeignKey('tbl_metode_bayar.idmetode_bayar'), default="0", server_default="0", nullable=False)
    parent = db.relationship("MetodeBayar", back_populates="children")

    idrekeningbank = db.Column(db.BigInteger, db.ForeignKey('tbl_rekening_bank.idrekeningbank'), default="0", server_default="0", nullable=False)
    parent = db.relationship("RekeningBank", back_populates="children")

    keterangan = db.Column(db.String(255), nullable=True)
    total = db.Column(db.Integer, default="0", server_default="0", nullable=False)

    idstatus_bayar = db.Column(db.BigInteger, db.ForeignKey('tbl_status_bayar.idstatus_bayar'), default="0", server_default="0", nullable=False)
    parent = db.relationship("StatusBayar", back_populates="children")

    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), nullable=False)
    parent = db.relationship("User", back_populates="children")

    rec_insert = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    rec_update = db.Column(db.DateTime, nullable=True )
    rec_delete = db.Column(db.DateTime, nullable=True )
    status_delete = db.Column(db.Enum("1","0", name="StatusDelete"), default="0", server_default="0",nullable=False )

    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)

    children = db.relationship("TransaksiPenjualanDo", back_populates="parent")

    def to_json(self):
        json_t_penjualan = {
            'idtp_penjualan': self.idtp_penjualan,
            'kdtp_penjualan': self.kdtp_penjualan,
            'idt_penjualan' : self.idt_penjualan,
            'tgl_pembayaran': self.tgl_pembayaran,
            'iduser': self.iduser,
            'idmetode_bayar': self.idmetode_bayar,

            'idrekeningbank': self.idrekeningbank,
            'total': self.total,
            'keterangan': self.keterangan,
            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
            'rec_delete': self.rec_delete,
            'status_delete': self.status_delete,
       
            'idstatus_bayar': self.idstatus_bayar,
            'publish': self.publish
        }

        return json_t_penjualan

    def __repr__(self):
        return '<TransaksiPenjualanPembayaran {}>'.format(self.idtp_penjualan)  
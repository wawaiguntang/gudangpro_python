from unicodedata import name
from app import db
import enum
from datetime import datetime  

class Publish(enum.Enum):
    T = "T"
    F = "F"

class TransaksiPenjualanDo(db.Model):
    __tablename__ = 'tbl_transaksi_penjualan_do'
    idtpdo_penjualan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kdtpdo_penjualan = db.Column(db.String(13), nullable=True)

    idtp_penjualan = db.Column(db.BigInteger, db.ForeignKey('tbl_transaksi_penjualan_pembayaran.idtp_penjualan'), nullable=False)
    parent = db.relationship("TransaksiPenjualanPembayaran", back_populates="children")

    idt_penjualan = db.Column(db.BigInteger, db.ForeignKey('tbl_transaksi_penjualan.idt_penjualan'), nullable=False)
    parent = db.relationship("TransaksiPenjualan", back_populates="children")

    tgl_buat = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    tgl_kirim = db.Column(db.DateTime, nullable=True )
    tgl_tiba = db.Column(db.DateTime, nullable=True )

    nmpenerima = db.Column(db.String(75), nullable=True)
    notelp = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(60), nullable=True)
    alamat_jalan = db.Column(db.String(75), nullable=True)
    kabupaten = db.Column(db.String(50), nullable=True)
    provinsi = db.Column(db.String(50), default="LAMPUNG", server_default="LAMPUNG", nullable=True)
    negara = db.Column(db.String(50), default="INDONESIA", server_default="INDONESIA", nullable=True)

    idarmada = db.Column(db.BigInteger, db.ForeignKey('tbl_armada.idarmada'), default="0", server_default="0", nullable=False)
    parent = db.relationship("Armada", back_populates="children")

    status_do = db.Column(db.Enum("LETTER",'LOADING','DELIVERY','ARRIVE','RETURN'),default="LETTER", server_default="LETTER", nullable=False)
    keterangan = db.Column(db.String(255), nullable=True)

    iduser = db.Column(db.BigInteger, db.ForeignKey('tbl_user.iduser'), nullable=False)
    parent = db.relationship("User", back_populates="children")

    rec_insert = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    rec_update = db.Column(db.DateTime, nullable=True )
    rec_delete = db.Column(db.DateTime, nullable=True )
    status_delete = db.Column(db.Enum("1","0", name="StatusDelete"), default="0", server_default="0",nullable=False )
    publish = db.Column(db.Enum(Publish), default=Publish.T.value, server_default=Publish.T.value,nullable=False)

    def to_json(self):
        json_t_penjualan = {
            'idtpdo_penjualan': self.idtpdo_penjualan,
            'kdtpdo_penjualan': self.kdtpdo_penjualan,
            'idtp_penjualan': self.idtp_penjualan,
            'idt_penjualan': self.idt_penjualan,

            'tgl_buat': self.tgl_buat,
            'tgl_kirim': self.tgl_kirim,
            'tgl_tiba': self.tgl_tiba,

            'nmpenerima': self.nmpenerima,
            'notelp': self.notelp,
            'email': self.email,
            'alamat_jalan': self.alamat_jalan,
            'kabupaten': self.kabupaten,
            'provinsi': self.provinsi,
            'negara': self.negara,

            'idarmada': self.idarmada,
            'status_do': self.status_do,
            'iduser': self.iduser,

            'rec_insert': self.rec_insert,
            'rec_update': self.rec_update,
            'rec_delete': self.rec_delete,
            'status_delete': self.status_delete,
            'publish': self.publish
        }

        return json_t_penjualan

    def __repr__(self):
        return '<TransaksiPenjualanDo {}>'.format(self.idtpdo_penjualan)  
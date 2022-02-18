"""empty message

Revision ID: ceaca5e42584
Revises: 964768b621e2
Create Date: 2022-02-18 15:36:14.363375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceaca5e42584'
down_revision = '964768b621e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_armada',
    sa.Column('idarmada', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('kdarmada', sa.String(length=10), nullable=True),
    sa.Column('nomor_plat', sa.String(length=11), nullable=True),
    sa.Column('idjenis_armada', sa.BigInteger(), server_default='0', nullable=True),
    sa.Column('daya_angkut', sa.Integer(), server_default='0', nullable=False),
    sa.Column('nostnk', sa.String(length=30), nullable=True),
    sa.Column('tglpajak', sa.Date(), nullable=True),
    sa.Column('idstaf', sa.BigInteger(), server_default='0', nullable=True),
    sa.Column('kondisi_armada', sa.Enum(name='kondisiarmada'), server_default='BAIK', nullable=False),
    sa.Column('publish', sa.Enum('T', 'F', name='publish'), server_default='T', nullable=False),
    sa.ForeignKeyConstraint(['idjenis_armada'], ['tbl_armada_jenis.idjenis_armada'], ),
    sa.ForeignKeyConstraint(['idstaf'], ['tbl_staf.idstaf'], ),
    sa.PrimaryKeyConstraint('idarmada')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_armada')
    # ### end Alembic commands ###
"""initial delete hora

Revision ID: 51fae6205148
Revises: 9aba8f634479
Create Date: 2024-09-18 15:51:40.117228

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '51fae6205148'
down_revision = '9aba8f634479'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('docente_aula', schema=None) as batch_op:
        batch_op.drop_column('Hora')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('docente_aula', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Hora', mssql.TIMESTAMP(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###

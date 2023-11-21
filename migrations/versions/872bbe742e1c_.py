"""empty message

Revision ID: 872bbe742e1c
Revises: 
Create Date: 2023-11-10 12:25:10.224439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872bbe742e1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###

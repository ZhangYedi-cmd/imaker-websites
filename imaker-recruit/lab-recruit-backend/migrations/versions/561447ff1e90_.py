"""empty message

Revision ID: 561447ff1e90
Revises: b5d2b7c321f8
Create Date: 2021-09-25 13:29:14.551487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '561447ff1e90'
down_revision = 'b5d2b7c321f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('rate', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'rate')
    # ### end Alembic commands ###

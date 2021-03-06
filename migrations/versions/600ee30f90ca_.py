"""empty message

Revision ID: 600ee30f90ca
Revises: 1055f2aa709a
Create Date: 2019-04-30 22:11:57.425204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '600ee30f90ca'
down_revision = '1055f2aa709a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('img_link', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'img_link')
    # ### end Alembic commands ###

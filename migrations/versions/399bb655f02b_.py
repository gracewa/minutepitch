"""empty message

Revision ID: 399bb655f02b
Revises: c4f799792502
Create Date: 2020-09-24 07:49:45.136766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '399bb655f02b'
down_revision = 'c4f799792502'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
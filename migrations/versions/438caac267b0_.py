"""empty message

Revision ID: 438caac267b0
Revises: 7275f81dfd21
Create Date: 2023-01-14 11:26:49.250544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '438caac267b0'
down_revision = '7275f81dfd21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###

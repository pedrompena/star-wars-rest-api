"""empty message

Revision ID: 21194b3cb4df
Revises: c97fa82b3d3d
Create Date: 2023-01-15 16:41:58.862112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21194b3cb4df'
down_revision = 'c97fa82b3d3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_favorites_people', schema=None) as batch_op:
        batch_op.drop_constraint('user_favorites_people_people_id_key', type_='unique')
        batch_op.drop_constraint('user_favorites_people_user_id_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_favorites_people', schema=None) as batch_op:
        batch_op.create_unique_constraint('user_favorites_people_user_id_key', ['user_id'])
        batch_op.create_unique_constraint('user_favorites_people_people_id_key', ['people_id'])

    # ### end Alembic commands ###
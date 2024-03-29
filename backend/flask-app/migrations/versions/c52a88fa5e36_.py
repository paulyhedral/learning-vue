"""empty message

Revision ID: c52a88fa5e36
Revises: 3bd56b699d4c
Create Date: 2019-11-09 10:50:00.171771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c52a88fa5e36'
down_revision = '3bd56b699d4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('surveys', sa.Column('creator_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'surveys', 'users', ['creator_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'surveys', type_='foreignkey')
    op.drop_column('surveys', 'creator_id')
    # ### end Alembic commands ###

"""empty message

Revision ID: b61545d1486d
Revises: c57b06aff3e2
Create Date: 2021-10-08 22:59:41.262657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b61545d1486d'
down_revision = 'c57b06aff3e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Movies',
    sa.Column('id', sa.TEXT(), nullable=False),
    sa.Column('image', sa.VARCHAR(), nullable=True),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('streaming_services', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Movies')
    # ### end Alembic commands ###
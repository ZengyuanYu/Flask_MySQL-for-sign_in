"""empty message

Revision ID: 1261a8046bbe
Revises: 
Create Date: 2018-01-30 11:39:59.650733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1261a8046bbe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('tags', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'tags')
    # ### end Alembic commands ###

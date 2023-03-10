"""empty message

Revision ID: 8bc770fd85c7
Revises: c8615174f498
Create Date: 2023-01-20 22:04:49.626027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bc770fd85c7'
down_revision = 'c8615174f498'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('scraps', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'scraps')
    # ### end Alembic commands ###

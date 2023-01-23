"""New revision

Revision ID: ef37a452cd79
Revises: 2e72a6574a1a
Create Date: 2023-01-22 20:56:57.837267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef37a452cd79'
down_revision = '2e72a6574a1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('color_id', sa.Integer(), nullable=True))
    op.drop_constraint('card_color_fkey', 'card', type_='foreignkey')
    op.create_foreign_key(None, 'card', 'color', ['color_id'], ['id'])
    op.drop_column('card', 'color')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('color', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'card', type_='foreignkey')
    op.create_foreign_key('card_color_fkey', 'card', 'color', ['color'], ['id'])
    op.drop_column('card', 'color_id')
    # ### end Alembic commands ###

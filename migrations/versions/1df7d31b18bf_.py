"""empty message

Revision ID: 1df7d31b18bf
Revises: 573c2025b244
Create Date: 2021-12-18 19:25:49.005474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1df7d31b18bf'
down_revision = '573c2025b244'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_comments', sa.Column('date_added', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post_comments', 'date_added')
    # ### end Alembic commands ###

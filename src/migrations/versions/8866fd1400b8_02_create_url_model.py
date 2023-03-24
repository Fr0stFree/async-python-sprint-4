"""02_create_url_model

Revision ID: 8866fd1400b8
Revises: 11bf8337a64e
Create Date: 2023-03-24 18:01:33.091776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8866fd1400b8'
down_revision = '11bf8337a64e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url',
    sa.Column('key', sa.UUID(), nullable=False),
    sa.Column('full_url', sa.String(length=255), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('key')
    )
    op.create_index(op.f('ix_url_full_url'), 'url', ['full_url'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_url_full_url'), table_name='url')
    op.drop_table('url')
    # ### end Alembic commands ###
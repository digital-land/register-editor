"""add reference model

Revision ID: 4c264728e0eb
Revises: 92327e91a369
Create Date: 2024-08-09 12:27:25.267755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c264728e0eb'
down_revision = '92327e91a369'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reference',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('dataset_id', sa.Text(), nullable=False),
    sa.Column('referencing_dataset', sa.Text(), nullable=False),
    sa.Column('specification', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['dataset.dataset'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reference')
    # ### end Alembic commands ###
"""rename field in reference model

Revision ID: 02ea78cc151c
Revises: 4c264728e0eb
Create Date: 2024-08-09 16:29:41.655566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02ea78cc151c'
down_revision = '4c264728e0eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reference', schema=None) as batch_op:
        batch_op.add_column(sa.Column('referenced_by', sa.Text(), nullable=False))
        batch_op.drop_column('referencing_dataset')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reference', schema=None) as batch_op:
        batch_op.add_column(sa.Column('referencing_dataset', sa.TEXT(), autoincrement=False, nullable=False))
        batch_op.drop_column('referenced_by')

    # ### end Alembic commands ###
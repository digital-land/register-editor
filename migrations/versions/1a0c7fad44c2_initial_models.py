"""initial models

Revision ID: 1a0c7fad44c2
Revises:
Create Date: 2023-08-21 11:39:55.975738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1a0c7fad44c2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "dataset",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "field",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "dataset_field",
        sa.Column("dataset_id", sa.Integer(), nullable=False),
        sa.Column("field_id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["dataset_id"],
            ["dataset.id"],
        ),
        sa.ForeignKeyConstraint(
            ["field_id"],
            ["field.id"],
        ),
        sa.PrimaryKeyConstraint("dataset_id", "field_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("dataset_field")
    op.drop_table("field")
    op.drop_table("dataset")
    # ### end Alembic commands ###

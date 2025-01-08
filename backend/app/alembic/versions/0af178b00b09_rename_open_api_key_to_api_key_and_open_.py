"""Rename open_api_key to api_key and open_api_base to base_url for better clarity and compatibility

Revision ID: 0af178b00b09
Revises: 725ae2e95b83
Create Date: 2024-12-24 17:33:16.965778

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0af178b00b09"
down_revision = "725ae2e95b83"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("member", "base_url")
    op.drop_column("member", "api_key")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "member", sa.Column("api_key", sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "member",
        sa.Column("base_url", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###

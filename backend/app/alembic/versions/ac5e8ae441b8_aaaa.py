"""aaaa

Revision ID: ac5e8ae441b8
Revises: fe2c95366646
Create Date: 2024-12-19 17:45:04.853852

"""

import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "ac5e8ae441b8"
down_revision = "fe2c95366646"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "thread",
        "query",
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        type_=sqlmodel.sql.sqltypes.AutoString(),
        nullable=False,
        existing_server_default=sa.text("'{}'::jsonb"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "thread",
        "query",
        existing_type=sqlmodel.sql.sqltypes.AutoString(),
        type_=postgresql.JSON(astext_type=sa.Text()),
        nullable=True,
        existing_server_default=sa.text("'{}'::jsonb"),
    )
    # ### end Alembic commands ###

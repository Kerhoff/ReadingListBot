"""Create tables

Revision ID: 5a8e541df3c2
Revises: 27e416f09959
Create Date: 2024-11-03 14:37:56.794967

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5a8e541df3c2"
down_revision: Union[str, None] = "27e416f09959"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the 'users' table
    op.create_table(
        "users",
        sa.Column("tg_user_id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("tg_username", sa.String(), unique=True, nullable=False),
    )

    # Create the 'reading_items' table
    op.create_table(
        "reading_items",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column(
            "user_id", sa.Integer(), sa.ForeignKey("users.tg_user_id"), nullable=False
        ),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("link", sa.String(), nullable=False),
        sa.Column("item_type", sa.String(), nullable=False),
        sa.Column("completed", sa.Boolean(), default=False, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_table("reading_items")
    op.drop_table("users")

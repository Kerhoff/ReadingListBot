"""Import data from sqlite

Revision ID: efe8595e52a0
Revises: 5a8e541df3c2
Create Date: 2024-11-03 19:45:33.213064

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import csv
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "efe8595e52a0"
down_revision: Union[str, None] = "5a8e541df3c2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Define the 'users' table
users = sa.Table(
    "users",
    sa.MetaData(),
    sa.Column("tg_user_id", sa.Integer(), primary_key=True, nullable=False),
    sa.Column("tg_username", sa.String(), unique=True, nullable=False),
)

# Define the 'reading_items' table
reading_items = sa.Table(
    "reading_items",
    sa.MetaData(),
    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column(
        "user_id", sa.Integer(), sa.ForeignKey("users.tg_user_id"), nullable=False
    ),
    sa.Column("title", sa.String(), nullable=False),
    sa.Column("link", sa.String(), nullable=False),
    sa.Column("item_type", sa.String(), nullable=False),
    sa.Column("completed", sa.Boolean(), default=False, nullable=False),
)


def upgrade() -> None:
    # Load data from CSV files
    with open("users.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header
        # users_data = [tuple(row) for row in csv_reader]
        users_data = [
            {"tg_user_id": int(row[2]), "tg_username": row[1]} for row in csv_reader
        ]
    # Insert data into the 'users' table
    op.bulk_insert(users, users_data)

    # Load data from CSV files
    with open("reading_items.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header
        # reading_items_data = [tuple(row) for row in csv_reader]
        reading_items_data = [
            {
                "id": int(row[0]),
                "user_id": int(row[1]),
                "title": row[2],
                "link": row[3],
                "item_type": row[4],
                "completed": bool(row[5]),
            }
            for row in csv_reader
        ]
    # Insert data into the 'reading_items' table
    op.bulk_insert(reading_items, reading_items_data)


def downgrade() -> None:
    op.execute("DELETE FROM reading_items")
    op.execute("DELETE FROM users")

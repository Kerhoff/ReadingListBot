from sqlalchemy import (
    DateTime,
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    relationship,
)
from datetime import datetime

# Define the base for declarative class
Base = declarative_base()


# Define the ReadingItem model
class ReadingItem(Base):
    __tablename__ = "reading_items"
    id = Column(Integer, primary_key=True)  # Unique identifier for the item
    user_id = Column(Integer, ForeignKey("users.tg_user_id"))  # Unique identifier for the user
    title = Column(String)  # Title of the item
    link = Column(String)  # URL of the item
    item_type = Column(String)  # Type of the item (e.g., book, article, video)
    completed = Column(Boolean, default=False)  # Whether the item has been read/watched/listened to
    created_at = Column(DateTime, default=datetime.now())  # Date and time the item was added
    # Relationship between ReadingItem and User
    user = relationship("User", back_populates="reading_items")


class User(Base):
    __tablename__ = "users"
    tg_user_id = Column(Integer, primary_key=True)  # Telegram ID of the user
    tg_username = Column(String, unique=True)  # Telegram username of the user
    # Relationship between User and ReadingItem
    reading_items = relationship("ReadingItem", back_populates="user")



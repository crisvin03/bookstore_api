from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base

# Define the "books" table structure using SQLAlchemy ORM
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)

    # Ensure no duplicate title-author pair exists
    __table_args__ = (
        UniqueConstraint('title', 'author', name='unique_title_author'),
    )

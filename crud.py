from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
import models, schemas

# Async: Get a single book by ID
async def get_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(models.Book).where(models.Book.id == book_id))
    return result.scalar_one_or_none()

# Async: Get a list of books with pagination
async def get_books(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Book).offset(skip).limit(limit))
    return result.scalars().all()

# Async: Create a new book
async def create_book(db: AsyncSession, book: schemas.BookCreate):
    # Check for existing book with same title and author
    result = await db.execute(
        select(models.Book).where(models.Book.title == book.title, models.Book.author == book.author)
    )
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Book already exists.")

    # Create and persist new book
    new_book = models.Book(**book.model_dump())
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book

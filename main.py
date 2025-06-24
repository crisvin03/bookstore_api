from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from contextlib import asynccontextmanager  

from database import engine, AsyncSessionLocal, Base
import models, schemas, crud

# Lifespan handler 
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

# Initialize FastAPI app using the lifespan handler
app = FastAPI(title="📚 Bookstore API", lifespan=lifespan)

# Dependency that provides an async database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Root route: Welcome message
@app.get("/", summary="Welcome to the Bookstore API")
async def read_root():
    return {
        "message": "📚 Welcome to the Bookstore API!",
        "description": "This API allows you to create, view, and manage books.",
        "endpoints": {
            "GET /books/": "List all books with pagination",
            "GET /books/{book_id}": "Retrieve a book by ID",
            "POST /books/": "Create a new book"
        },
        "note": "Explore via /docs or /redoc."
    }

# POST: Create a new book
@app.post("/books/", response_model=schemas.Book, summary="Create a new book")
async def create_book(book: schemas.BookCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_book(db=db, book=book)

# GET: Retrieve all books (paginated)
@app.get("/books/", response_model=List[schemas.Book], summary="Get all books with pagination")
async def read_books(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.get_books(db=db, skip=skip, limit=limit)

# GET: Retrieve a book by ID
@app.get("/books/{book_id}", response_model=schemas.Book, summary="Get a book by ID")
async def read_book(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await crud.get_book(db=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

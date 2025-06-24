from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Async SQLite database URL
DATABASE_URL = "sqlite+aiosqlite:///./books.db"

# Create an asynchronous engine instance
engine = create_async_engine(DATABASE_URL, echo=False)

# Create a session factory for async database interaction
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession  # Ensure sessions are asynchronous
)

# Base class for declaring database models
Base = declarative_base()

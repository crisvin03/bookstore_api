from pydantic import BaseModel, ConfigDict

# Base schema for shared book fields
class BookBase(BaseModel):
    title: str
    author: str

# Schema for book creation (input)
class BookCreate(BookBase):
    pass

# Schema for book response (output)
class Book(BookBase):
    id: int

    # Enable ORM mode for response serialization (Pydantic v2)
    model_config = ConfigDict(from_attributes=True)

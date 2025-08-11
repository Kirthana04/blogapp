from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class BlogCreate(BaseModel):
    title: str
    description: Optional[str]
    tags: Optional[List[str]]
    contents: Optional[str]
    image: Optional[str] = Field(None, description="Base64-encoded image string")

class BlogResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    tags: Optional[List[str]] = []
    contents: Optional[str]
    image: Optional[str] = Field(None, description="URL/path to the stored image file")
    deleted_flag: Optional[bool] = None
    created_at: Optional[datetime] = None

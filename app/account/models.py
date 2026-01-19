from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

# --- Base schemas for Pydantic ---
class UserBase(SQLModel):
    email: str
    name: str
    is_active: bool = True
    is_admin: bool = False

class UserCreate(UserBase):
    password: str  # plain password for creation

class UserOut(UserBase):
    id: int

# --- SQLModel ORM Table ---
class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    name: str = Field(nullable=False)
    hashed_password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    is_verified: bool = Field(default=False)


class RefreshToken(SQLModel, table=True):
    __tablename__ = "refresh_token"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=False, index=True)
    token: str = Field(nullable=False, index=True)
    expires_at: datetime = Field(nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    revoked: bool = Field(default=False)

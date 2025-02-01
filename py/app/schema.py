from sqlalchemy import Column, String, TIMESTAMP, Boolean, Integer, ForeignKey, func
from app.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    email_verified = Column(Boolean, nullable=False, default=False)
    tokens = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now()
    )


class Generation(Base):
    __tablename__ = "generation"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)
    prompt = Column(String, nullable=False)
    status = Column(String, nullable=False)  # pending, completed, failed
    image_url = Column(String)  # URL of generated image
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

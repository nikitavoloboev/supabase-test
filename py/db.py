import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Load the connection string from the environment variable.
# Ensure DATABASE_URL is set in your environment (or via load_dotenv() for local development).
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise EnvironmentError("DATABASE_URL environment variable not set.")

# Create an async engine.
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a sessionmaker factory that will produce AsyncSession instances.
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for model classes.
Base = declarative_base()

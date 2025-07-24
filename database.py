from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL (local file-based)
SQLALCHEMY_DATABASE_URL = "sqlite:///./customers.db"

# Create SQLAlchemy engine (check_same_thread=False is required for SQLite with FastAPI)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Create a configured "SessionLocal" class for database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for model definitions (used in models.py)
Base = declarative_base()

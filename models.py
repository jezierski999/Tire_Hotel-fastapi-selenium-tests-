from sqlalchemy import Column, Integer, String
from database import Base

class Customer(Base):
    __tablename__ = "customers"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique customer ID

    # Basic customer info
    surname = Column(String, index=True)
    firstname = Column(String, index=True)
    address = Column(String, index=True)
    season = Column(String, index=True)     # Summer or winter tire storage
    rims = Column(String, index=True)       # Rim type (steel, alloy, etc.)

    # Front tires
    brand_front = Column(String, index=True)
    width_front = Column(String, index=True)
    ratio_front = Column(String, index=True)
    diameter_front = Column(String, index=True)

    # Tire positions (optional flags, e.g., presence or damage info)
    fl = Column(String, index=True)  # Front Left
    fr = Column(String, index=True)  # Front Right
    rl = Column(String, index=True)  # Rear Left
    rr = Column(String, index=True)  # Rear Right

    # Rear tires
    brand_rear = Column(String, index=True)
    width_rear = Column(String, index=True)
    ratio_rear = Column(String, index=True)
    diameter_rear = Column(String, index=True)

    # Additional notes (e.g., condition, remarks)
    note = Column(String, index=True)

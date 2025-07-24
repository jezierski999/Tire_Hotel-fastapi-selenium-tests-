from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import database

app = FastAPI()

# Enable CORS for development (in production, restrict origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Replace with allowed frontend domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create all tables in the database
models.Base.metadata.create_all(bind=database.engine)


# Dependency that provides a new DB session for each request
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET /customers - Retrieve all customers
@app.get("/customers/")
def read_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()


# POST /customers - Create a new customer
@app.post("/customers/")
def create_customer(customer: dict, db: Session = Depends(get_db)):
    db_customer = models.Customer(
        surname=customer["surname"],
        firstname=customer["firstname"],
        address=customer["address"],
        season=customer["season"],
        rims=customer["rims"],
        brand_front=customer["brand_front"],
        width_front=customer["width_front"],
        ratio_front=customer["ratio_front"],
        diameter_front=customer["diameter_front"],
        fl=customer["fl"],
        fr=customer["fr"],
        rl=customer["rl"],
        rr=customer["rr"],
        brand_rear=customer["brand_rear"],
        width_rear=customer["width_rear"],
        ratio_rear=customer["ratio_rear"],
        diameter_rear=customer["diameter_rear"],
        note=customer["note"],
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


# DELETE /customers/{customer_id} - Delete a customer by ID
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.get(models.Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted"}


# PUT /customers/{customer_id} - Update an existing customer
@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, updated_data: dict, db: Session = Depends(get_db)):
    customer = db.get(models.Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Update only provided fields
    customer.surname = updated_data.get("surname", customer.surname)
    customer.firstname = updated_data.get("firstname", customer.firstname)
    customer.address = updated_data.get("address", customer.address)
    customer.season = updated_data.get("season", customer.season)
    customer.rims = updated_data.get("rims", customer.rims)
    customer.brand_front = updated_data.get("brand_front", customer.brand_front)
    customer.width_front = updated_data.get("width_front", customer.width_front)
    customer.ratio_front = updated_data.get("ratio_front", customer.ratio_front)
    customer.diameter_front = updated_data.get("diameter_front", customer.diameter_front)
    customer.fl = updated_data.get("fl", customer.fl)
    customer.fr = updated_data.get("fr", customer.fr)
    customer.rl = updated_data.get("rl", customer.rl)
    customer.rr = updated_data.get("rr", customer.rr)
    customer.brand_rear = updated_data.get("brand_rear", customer.brand_rear)
    customer.width_rear = updated_data.get("width_rear", customer.width_rear)
    customer.ratio_rear = updated_data.get("ratio_rear", customer.ratio_rear)
    customer.diameter_rear = updated_data.get("diameter_rear", customer.diameter_rear)
    customer.note = updated_data.get("note", customer.note)

    db.commit()
    db.refresh(customer)
    return customer

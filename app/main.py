from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
from typing import List

app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create address
@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    new_address = models.Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


# Read addresses
@app.get("/addresses/", response_model=List[schemas.Address])
def read_addresses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    addresses = db.query(models.Address).offset(skip).limit(limit).all()
    return addresses


# Update address
@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(address_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)):
    existing_address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not existing_address:
        raise HTTPException(status_code=404, detail="Address not found")
    for key, value in address.dict().items():
        setattr(existing_address, key, value)
    db.commit()
    db.refresh(existing_address)
    return existing_address


@app.delete("/addresses/{address_id}", response_model=schemas.Address)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    existing_address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not existing_address:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(existing_address)
    db.commit()
    return existing_address


@app.get("/addresses/nearby", response_model=List[schemas.Address])
def get_nearby_addresses(latitude: float, longitude: float, distance: float, db: Session = Depends(get_db)):
    addresses = db.query(models.Address).all()
    nearby_addresses = []
    for address in addresses:
        if ((address.latitude - latitude) ** 2 + (address.longitude - longitude) ** 2) ** 0.5 <= distance:
            nearby_addresses.append(address)
    return nearby_addresses

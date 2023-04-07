from pydantic import BaseModel


class AddressBase(BaseModel):
    latitude: float
    longitude: float
    description: str


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, Field
from datetime import date

class MedicineCreate(BaseModel):
    name: str = Field(..., description="Name of the medicine")
    price: float = Field(..., description="Price of the medicine")
    power: int = Field(..., description="Power of the medicine")
    quantity: int = Field(..., description="Quantity of the medicine")
    mfd: date = Field(..., description="Manufacturing date")
    exp: date = Field(..., description="Expiry date")

class MedicineUpdate(MedicineCreate):
    id: int = Field(..., description="ID of the medicine to update")

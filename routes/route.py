from fastapi import APIRouter, HTTPException
from schemas.schema import MedicineCreate, MedicineUpdate
from views.view import (
    create_medicine,
    get_all_medicines,
    get_medicine_by_id,
    update_medicine,
    delete_medicine
)

router = APIRouter()

@router.post("/")
def create(med: MedicineCreate):
    medicine = create_medicine(**med.dict())
    return {"message": "Medicine added", "medicine": medicine}

@router.get("/")
def get_all():
    return get_all_medicines()

@router.get("/{med_id}")
def get_one(med_id: int):
    medicine = get_medicine_by_id(med_id)
    if medicine:
        return medicine
    raise HTTPException(status_code=404, detail="Medicine not found")

@router.put("/")
def update(med: MedicineUpdate):
    med_id = med.id
    update_data = med.dict(exclude={"id"})
    updated = update_medicine(med_id, **update_data)
    if updated:
        return {"message": "Medicine updated", "medicine": updated}
    raise HTTPException(status_code=404, detail="Medicine not found")

@router.delete("/{med_id}")
def delete(med_id: int):
    success = delete_medicine(med_id)
    if success:
        return {"message": "Medicine deleted"}
    raise HTTPException(status_code=404, detail="Medicine not found")

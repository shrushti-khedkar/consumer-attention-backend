from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import require_role
from app.models import models, schemas

router = APIRouter(tags=["Store Layout"])


@router.post("/stores", response_model=schemas.StoreResponse)
def create_store(
    store: schemas.StoreCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_role(["StoreManager", "SuperAdmin"])),
):
    new_store = models.Store(name=store.name, location=store.location)
    db.add(new_store)
    db.commit()
    db.refresh(new_store)
    return new_store


# ---------- Zone ----------
@router.post("/zones", response_model=schemas.ZoneResponse)
def create_zone(zone: schemas.ZoneCreate, db: Session = Depends(get_db)):
    store = db.query(models.Store).filter(models.Store.id == zone.store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")

    new_zone = models.Zone(store_id=zone.store_id, name=zone.name)
    db.add(new_zone)
    db.commit()
    db.refresh(new_zone)
    return new_zone


@router.get("/zones", response_model=list[schemas.ZoneResponse])
def list_zones(db: Session = Depends(get_db)):
    return db.query(models.Zone).all()


# ---------- Shelf ----------
@router.post("/shelves", response_model=schemas.ShelfResponse)
def create_shelf(shelf: schemas.ShelfCreate, db: Session = Depends(get_db)):
    zone = db.query(models.Zone).filter(models.Zone.id == shelf.zone_id).first()
    if not zone:
        raise HTTPException(status_code=404, detail="Zone not found")

    new_shelf = models.Shelf(zone_id=shelf.zone_id, name=shelf.name)
    db.add(new_shelf)
    db.commit()
    db.refresh(new_shelf)
    return new_shelf


@router.get("/shelves", response_model=list[schemas.ShelfResponse])
def list_shelves(db: Session = Depends(get_db)):
    return db.query(models.Shelf).all()


# ---------- Camera ----------
@router.post("/cameras", response_model=schemas.CameraResponse)
def create_camera(camera: schemas.CameraCreate, db: Session = Depends(get_db)):
    store = db.query(models.Store).filter(models.Store.id == camera.store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")

    new_camera = models.Camera(
        store_id=camera.store_id,
        zone_id=camera.zone_id,
        name=camera.name,
        location_description=camera.location_description,
    )
    db.add(new_camera)
    db.commit()
    db.refresh(new_camera)
    return new_camera


@router.get("/cameras", response_model=list[schemas.CameraResponse])
def list_cameras(db: Session = Depends(get_db)):
    return db.query(models.Camera).all()
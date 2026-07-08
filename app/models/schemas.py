from pydantic import BaseModel, EmailStr


# ---------- User ----------
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


# ---------- Store ----------
class StoreCreate(BaseModel):
    name: str
    location: str

class StoreResponse(BaseModel):
    id: int
    name: str
    location: str

    class Config:
        from_attributes = True


# ---------- Zone ----------
class ZoneCreate(BaseModel):
    store_id: int
    name: str

class ZoneResponse(BaseModel):
    id: int
    store_id: int
    name: str

    class Config:
        from_attributes = True


# ---------- Shelf ----------
class ShelfCreate(BaseModel):
    zone_id: int
    name: str

class ShelfResponse(BaseModel):
    id: int
    zone_id: int
    name: str

    class Config:
        from_attributes = True


# ---------- Camera ----------
class CameraCreate(BaseModel):
    store_id: int
    zone_id: int | None = None
    name: str
    location_description: str | None = None

class CameraResponse(BaseModel):
    id: int
    store_id: int
    zone_id: int | None
    name: str
    location_description: str | None

    class Config:
        from_attributes = True
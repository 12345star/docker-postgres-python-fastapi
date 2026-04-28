from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user_schema import UserCreate, UserResponse
from app.crud.user_crud import UserCRUD
from app.core.database import get_db, init_db

app = FastAPI(title="User Management API", version="1.0.0")


# --- Evento de inicio: crea las tablas automáticamente ---
@app.on_event("startup")
async def startup_event():
    await init_db()


@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Creates a new user record in the system.
    """
    try:
        new_user = await UserCRUD.create_user(db, user_data)
        return new_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@app.get("/users/", response_model=List[UserResponse], tags=["Users"])
async def read_users(db: AsyncSession = Depends(get_db)):
    """
    Retrieves a list of all users.
    """
    users = await UserCRUD.get_all_users(db)
    return users



from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.models import User
from app.schemas.user_schema import UserCreate, UserUpdate
from typing import Optional, List

class UserCRUD:
    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    @staticmethod
    async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
        existing_user = await UserCRUD.get_user_by_email(db, user_data.email)
        if existing_user:
            raise Exception("Email already registered")

        new_user = User(name=user_data.name, email=user_data.email)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    @staticmethod
    async def get_all_users(db: AsyncSession) -> List[User]:
        result = await db.execute(select(User))
        return result.scalars().all()


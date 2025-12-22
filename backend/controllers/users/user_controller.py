-----------------------------------------------
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.models.user import User
from backend.services.users.user_service import UserService
from backend.repositories.users.user_repository import UserRepository

router = APIRouter()

# Dependency injection
def get_user_service() -> UserService:
    repository = UserRepository()
    return UserService(repository)

@router.post("/", response_model=User)
def create_user(
    id: int, 
    name: str, 
    email: str, 
    is_active: bool, 
    user_service: UserService = Depends(get_user_service)
) -> User:
    return user_service.create_user(id, name, email, is_active)

@router.get("/{user_id}", response_model=User)
def get_user(
    user_id: int, 
    user_service: UserService = Depends(get_user_service)
) -> User:
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[User])
def list_users(
    user_service: UserService = Depends(get_user_service)
) -> List[User]:
    return user_service.get_all_users()
```
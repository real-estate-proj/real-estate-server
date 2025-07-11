from sqlalchemy.orm import Session
from typing import Optional
from models.user import User
from schemas.auth.register_schema import RegisterRequestSchema
from core.security.security import hash_password


def createNewUser  (user: RegisterRequestSchema, database: Session, table=User) -> Optional[User]:
    hashed_pwd = hash_password (user.password)
    user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password_hash=hashed_pwd,
        role=user.role,
        avatar_url=user.avatar_url,
        created_at=user.created_at,
        is_verified = False
    )
    database.add (user)
    database.commit ()
    database.refresh (user)
    return user

def getUser(attributes: dict, database: Session, table=User) -> Optional[User]:
    query = database.query(table)

    for attr, value in attributes.items():
        if hasattr(table, attr):
            query = query.filter(getattr(table, attr) == value)

    return query.first()


def updateUserStatus(email: str, newStatus, database: Session):
    instance = database.query(User).filter(User.email == email).first()
    
    if not instance:
        return None  
    
    instance.is_verified = newStatus
    database.commit()
    database.refresh(instance)
    return instance

def updateUserPassword (email, newpassword, database: Session):
    user = database.query (User).filter (User.email == email).first ()

    if not user:
        return None
    
    hashpassword = hash_password (newpassword)
    user.password_hash  = hashpassword

    database.commit ()
    database.refresh (user)
    return user


def deleteUser ():
    pass
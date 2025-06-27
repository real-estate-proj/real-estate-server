from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.auth import RevokedToken
from core.database.session import init_database


def revoke_token (access_token, refresh_token, db: Session):
    revokedToken = RevokedToken (
        access_token=access_token,
        refresh_token=refresh_token
    )
    db.add (revokedToken)
    db.commit ()
    db.refresh (revokedToken)

def is_revoked (access_token, refresh_token, db: Session):
    token = db.query(RevokedToken).filter(
        or_(RevokedToken.access_token == access_token, RevokedToken.refresh_token == refresh_token)
    ).first()

    if not token:
        return False
    return True

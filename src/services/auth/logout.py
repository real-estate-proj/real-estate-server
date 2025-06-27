from crud.auth.token import revoke_token
from core.security.security import decode_token

def signout (access, refresh, db, exception, tokenException, userException, user):
    if refresh == "":
        raise exception
    refreshPayload = decode_token (refresh)

    if not refreshPayload or refreshPayload["type"] != 'refresh':
        raise tokenException
    
    if refreshPayload["email"] != user.email:
        raise userException
    
    revoke_token (access_token=access, refresh_token=refresh, db=db)
    return True

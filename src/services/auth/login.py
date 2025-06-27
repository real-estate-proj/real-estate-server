from core.security.security import verify_password, create_access_token, create_refresh_token, decode_token
from crud.user.user import getUser

def loginUser (email, password, db, userException, passwordException):
    user = getUser ({"email": email}, db)
    if not user:
        raise userException
    
    if not verify_password(password, user.password_hash):
        raise passwordException
    
    acessToken = create_access_token ({
        "email": user.email,
        "name": user.name,
        "role": user.role,
        "is_verified": user.is_verified
    })

    refreshToken = create_refresh_token ({
        "email": user.email,
        "name": user.name,
        "role": user.role,
        "is_verified": user.is_verified
    })

    return {
        "accesstoken": acessToken,
        "refreshtoken": refreshToken
    }

def refreshToken (token, exception):
    user_data = decode_token (token.refresh_token)
    if not user_data:
        raise exception
    accessToken = create_access_token ({**user_data})
    
    return {
        "accesstoken": accessToken,
    }

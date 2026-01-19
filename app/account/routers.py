from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.account.services import (
    create_user,
    authenticate_user,
    process_email_verification,
    verify_email_token,
    change_password,
    process_password_reset,
    reset_password_with_token,
)
from app.account.models import UserCreate, UserOut
from app.account.utils import create_tokens, verify_refresh_token, revoke_refresh_token
from app.account.dependencies import get_current_user, require_admin
from app.db.config import get_session

router = APIRouter(prefix="/account", tags=["Account"])

@router.post("/register", response_model=UserOut)
def register(session: Session = Depends(get_session), user: UserCreate = None):
    return create_user(session, user)

@router.post("/login")
def login(session: Session = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    tokens = create_tokens(session, user)
    response = JSONResponse(content={"access_token": tokens["access_token"]})
    response.set_cookie(
        "refresh_token", tokens["refresh_token"], httponly=True, secure=True, samesite="lax"
    )
    return response

@router.post("/refresh")
def refresh_token(session: Session = Depends(get_session), request: Request = None):
    token = request.cookies.get("refresh_token")
    if not token:
        raise HTTPException(status_code=404, detail="Missing Refresh Token")
    user = verify_refresh_token(session, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired Refresh token")
    return create_tokens(session, user)

@router.get("/me", response_model=UserOut)
def me(user=Depends(get_current_user)):
    return user

@router.post("/verify-request")
def send_verification_email(user=Depends(get_current_user)):
    return process_email_verification(user)

@router.get("/verify")
def verify_email(session: Session = Depends(get_session), token: str = None):
    return verify_email_token(session, token)

@router.post("/change-password")
def password_change(
    session: Session = Depends(get_session), new_password: str = None, user=Depends(get_current_user)
):
    change_password(session, user, new_password)
    return {"msg": "Password Changed Successfully"}

@router.post("/forgot-password")
def forgot_password(session: Session = Depends(get_session), email: str = None):
    return process_password_reset(session, email)

@router.post("/reset-password")
def reset_password(
    session: Session = Depends(get_session), token: str = None, new_password: str = None
):
    return reset_password_with_token(session, token, new_password)

@router.get("/admin")
def admin(user=Depends(require_admin)):
    return {"msg": f"Welcome Admin: {user.name}"}

@router.post("/logout")
def logout(session: Session = Depends(get_session), request: Request = None):
    token = request.cookies.get("refresh_token")
    if token:
        revoke_refresh_token(session, token)
    response = JSONResponse(content={"detail": "logged out"})
    response.delete_cookie("refresh_token")
    return response

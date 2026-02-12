from flask import Blueprint, current_app, redirect, session, url_for
from flask_login import login_user, logout_user
from sqlalchemy import select

from auth.google_auth import init_oauth
from database.database import new_session
from models.user import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login")
def login():
    google = init_oauth(current_app)
    redirect_uri = url_for("auth.callback", _external=True)
    print(f"DEBUG: Generated redirect URI: {redirect_uri}")
    return google.authorize_redirect(redirect_uri)


@auth_bp.route("/callback")
def callback():
    google = init_oauth(current_app)
    token = google.authorize_access_token()
    user_info = token.get("userinfo")

    with new_session() as session:
        stmt = select(User).filter_by(email=user_info["email"])
        user = session.execute(stmt).scalar_one_or_none()

        if not user:
            user = User(
                email=user_info["email"],
                name=user_info["name"],
                google_id=user_info["sub"],
                avatar_url=user_info["picture"],
            )
            session.add(user)
            session.commit()
            session.refresh(user)

        login_user(user)

    return redirect(url_for("profile"))


@auth_bp.route("/logout")
def logout():
    session.clear()
    logout_user()
    return redirect(url_for("index"))

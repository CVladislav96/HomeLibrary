from flask_login import LoginManager

from database.database import new_session
from models.user import User


def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        with new_session() as session:
            return session.get(User, int(user_id))

    return login_manager

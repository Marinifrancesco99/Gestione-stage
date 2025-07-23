from app.dao.user_dao import UsersDAO
from app.utils.auth import hash_password, verify_password, generate_jwt


class AuthService:
    @staticmethod
    def register_user(name, email, password, role):
        if role != "studente":
            raise ValueError("Non puoi registrarti come admin, scuola o tutor.")

        if not all([name, email, password]):
            raise ValueError("Tutti i campi eccetto role sono obbligatori.")

        hashed = hash_password(password)
        return UsersDAO.create_user(name, email, hashed, role)
    
    
    
    @staticmethod
    def login_user(email, password):
        user = UsersDAO.get_user_by_email(email)
        
        if not user or not verify_password(password, user.password):
            return None
        
        token = generate_jwt(user.id, user.role)
        return token, user

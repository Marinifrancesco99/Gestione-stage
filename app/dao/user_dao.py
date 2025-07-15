from app import db
from app.model.users import User

class UsersDAO:
    # get all users
    @staticmethod
    def get_all_users():
        return User.query.all()

    # get a user by id
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    # get a user by email
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    # Create a new user
    @staticmethod
    def create_user(name, email, password, role):
        new_user = User(
            name=name,
            email=email,
            password=password,
            role=role
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    # Update an existing user
    @staticmethod
    def update_user(user_id, **kwargs):
        user = User.query.get(user_id)
        if not user:
            return None

        for key, value in kwargs.items():
            if hasattr(user, key) and value is not None:
                setattr(user, key, value)

        db.session.commit()
        return user

    # Delete a user
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return None

        db.session.delete(user)
        db.session.commit()
        return user

    # Get tutor for a specific user
    @staticmethod
    def get_tutor_for_user(user_id):
        user = User.query.get(user_id)
        return user.tutor if user else None

    # Get student for a specific user
    @staticmethod
    def get_student_for_user(user_id):
        user = User.query.get(user_id)
        return user.student if user else None
    
    @staticmethod
    def get_users_by_role(role):
        """Restituisce tutti gli utenti che hanno un determinato ruolo."""
        return User.query.filter_by(role=role).all()

    @staticmethod
    def get_all_tutors():
        """Restituisce tutti gli utenti con ruolo tutor."""
        return UsersDAO.get_users_by_role('tutor')

    @staticmethod
    def get_all_students():
        """Restituisce tutti gli utenti con ruolo student."""
        return UsersDAO.get_users_by_role('student')

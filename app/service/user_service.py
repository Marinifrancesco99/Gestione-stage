from app.dao.user_dao import UsersDAO
from app.exceptions.not_found import NotFoundException

class UserService:
    @staticmethod
    def get_all_users():
        return UsersDAO.get_all_users()
    
    @staticmethod
    def get_user_by_id(user_id):
        return UsersDAO.get_user_by_id(user_id)
    
    @staticmethod
    def get_user_by_email(email):   
        return UsersDAO.get_user_by_email(email)
    
    @staticmethod
    def update_user(user_id, **kwargs):
        user = UsersDAO.get_user_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        return UsersDAO.update_user(user_id, **kwargs)
    
    @staticmethod
    def delete_user(user_id):
        user = UsersDAO.get_user_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        UsersDAO.delete_user(user_id)
        return True
    
    @staticmethod
    def get_tutor_for_user(user_id):
        user = UsersDAO.get_user_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        return UsersDAO.get_tutor_for_user(user_id)
    
    @staticmethod
    def get_student_for_user(user_id):
        user = UsersDAO.get_user_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        return UsersDAO.get_student_for_user(user_id)
    
    @staticmethod
    def get_users_by_role(role):
        return UsersDAO.get_users_by_role(role)
    
    @staticmethod
    def get_all_tutors():
        return UsersDAO.get_all_tutors()
    
    @staticmethod
    def get_all_students():
        return UsersDAO.get_all_students()
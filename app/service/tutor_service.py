from app.dao.tutor_dao import TutorsDAO
from app.exceptions.not_found import NotFoundException

class TutorService:
    @staticmethod
    def get_all_tutors():
        return TutorsDAO.get_all_tutors()
    
    @staticmethod
    def get_tutor_by_id(tutor_id):
        return TutorsDAO.get_tutor_by_id(tutor_id)
    
    @staticmethod
    def get_tutor_by_email(email):
        return TutorsDAO.get_by_email(email)
    
    @staticmethod
    def create_tutor(name, surname, email, role, user_id=None, company_id=None):
        return TutorsDAO.create_tutor(name, surname, email, role, user_id, company_id)
    
    @staticmethod
    def update_tutor(tutor_id, **kwargs):
        tutor = TutorsDAO.get_tutor_by_id(tutor_id)
        if not tutor:
            raise NotFoundException("Tutor not found")
        return TutorsDAO.update_tutor(tutor_id, **kwargs)
    
    @staticmethod
    def delete_tutor(tutor_id):
        tutor = TutorsDAO.get_tutor_by_id(tutor_id)
        if not tutor:
            raise NotFoundException("Tutor not found")
        TutorsDAO.delete_tutor(tutor_id)
        return True
    
    @staticmethod
    def get_attendance_logs_for_tutor(tutor_id):
        tutor = TutorsDAO.get_tutor_by_id(tutor_id)
        if not tutor:
            raise NotFoundException("Tutor not found")
        return TutorsDAO.get_attendance_logs_for_tutor(tutor_id)
    
    @staticmethod
    def get_internship_for_tutor(tutor_id):
        tutor = TutorsDAO.get_tutor_by_id(tutor_id)
        if not tutor:
            raise NotFoundException("Tutor not found")
        return TutorsDAO.get_internship_for_tutor(tutor_id)
    
    @staticmethod
    def get_company_for_tutor(tutor_id):
        tutor = TutorsDAO.get_tutor_by_id(tutor_id)
        if not tutor:
            raise NotFoundException("Tutor not found")
        return TutorsDAO.get_company_for_tutor(tutor_id)
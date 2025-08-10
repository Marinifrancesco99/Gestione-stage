from app.dao.professors_dao import ProfessorsDAO
from app.exceptions.not_found import NotFoundException

class ProfessorService:
    @staticmethod
    def get_professor_by_id(professor_id):
        return ProfessorsDAO.get_professor_by_id(professor_id)
    
    @staticmethod
    def get_all_professors():
        return ProfessorsDAO.get_all_professors()
    
    @staticmethod
    def create_professor(name, surname, email, phone=None, vote=None, evaluation=None, note=None):
        return ProfessorsDAO.create_professor(name, surname, email, phone, vote, evaluation, note)
    
    @staticmethod
    def update_professor(professor_id, name=None, surname=None, email=None, phone=None, vote=None, evaluation=None, note=None):
        professor = ProfessorsDAO.get_professor_by_id(professor_id)
        if not professor:
            raise NotFoundException("Professor not found")
        return ProfessorsDAO.update_professor(professor_id, name, surname, email, phone, vote, evaluation, note)
    
    @staticmethod
    def delete_professor(professor_id):
        professor = ProfessorsDAO.get_professor_by_id(professor_id)
        if not professor:
            raise NotFoundException("Professor not found")
        return ProfessorsDAO.delete_professor(professor_id)
    
    @staticmethod
    def get_professor_by_email(email):
        professor = ProfessorsDAO.get_by_email(email)
        if not professor:
            raise NotFoundException("Professor with this email does not exist")
        return professor
    
    @staticmethod
    def get_by_course(course_id):
        professor = ProfessorsDAO.get_by_course(course_id)
        if not professor:
            raise NotFoundException("No professor found for this course")
        return professor
    
    @staticmethod
    def add_course(professor_id, course):
        professor = ProfessorsDAO.get_professor_by_id(professor_id)
        if not professor:
            raise NotFoundException("Professor not found")
        if not course:
            raise NotFoundException("Course not found")
        return ProfessorsDAO.add_course(professor_id, course)
    
    @staticmethod
    def remove_course(professor_id, course):
        professor = ProfessorsDAO.get_professor_by_id(professor_id)
        if not professor:
            raise NotFoundException("Professor not found")
        if not course:
            raise NotFoundException("Course not found")
        return ProfessorsDAO.remove_course(professor_id, course)
        
    
    
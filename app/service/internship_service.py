from app.dao.internships_dao import InternshipsDAO
from app.exceptions.not_found import NotFoundException

class InternshipService:
    @staticmethod
    def get_internship_by_id(internship_id):
        return InternshipsDAO.get_internship_by_id(internship_id)
    
    @staticmethod
    def get_all_internships():
        return InternshipsDAO.get_all_internships()
    
    @staticmethod
    def save_internship(start_date, end_date, status, company_id, tutor_id, student_id):
        return InternshipsDAO.create_internship(start_date, end_date, status, company_id, tutor_id, student_id)
    
    @staticmethod
    def update_internship(internship_id, start_date=None, end_date=None, status=None, company_id=None, tutor_id=None, student_id=None):
        internship = InternshipsDAO.get_internship_by_id(internship_id)
        if not internship:
            raise NotFoundException(f"Internship with id {internship_id} not found.")
        return InternshipsDAO.update_internship(internship_id, start_date, end_date, status, company_id, tutor_id, student_id)
    
    @staticmethod
    def delete_internship(internship_id):
        internship = InternshipsDAO.get_internship_by_id(internship_id)
        if not internship:
            raise NotFoundException(f"Internship with id {internship_id} not found.")
        InternshipsDAO.delete_internship(internship_id)
        return True
    
    @staticmethod
    def get_by_student(student_id):
        internship = InternshipsDAO.get_by_student(student_id)
        if not internship:
            raise NotFoundException(f"No internships found for student ID {student_id}.")
        return internship
    
    @staticmethod
    def get_by_company(company_id):
        internship = InternshipsDAO.get_by_company(company_id)
        if not internship:
            raise NotFoundException(f"No internships found for company ID {company_id}.")
        return internship
    
    @staticmethod
    def get_by_tutor(tutor_id):
        internship = InternshipsDAO.get_by_tutor(tutor_id)
        if not internship:
            raise NotFoundException(f"No internships found for tutor ID {tutor_id}.")
        return internship
    
    @staticmethod
    def get_by_status(status):
        internship = InternshipsDAO.get_by_status(status)
        if not internship:
            raise NotFoundException(f"No internships found for status {status}.")
        return internship
    
    @staticmethod
    def get_by_date_range(start_date, end_date):
        internship = InternshipsDAO.get_by_date_range(start_date, end_date)
        if not internship:
            raise NotFoundException("No internship in range.")
        return internship
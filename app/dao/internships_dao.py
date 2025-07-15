from app import db
from app.model.internships import Internship

class InternshipsDAO:
    @staticmethod
    def get_internship_by_id(internship_id):
        return Internship.query.get(internship_id)

    @staticmethod
    def get_all_internships():
        return Internship.query.all()

    @staticmethod
    def create_internship(start_date, end_date, status, company_id, tutor_id, student_id):
        internship= Internship(
            start_date=start_date,
            end_date=end_date,
            status=status,
            company_id=company_id,
            tutor_id=tutor_id,
            student_id=student_id
        )
        db.session.add(internship)
        db.session.commit()
        return internship

    @staticmethod
    def update_internship(internship_id, start_date=None, end_date=None, status=None, company_id=None, tutor_id=None, student_id=None):
        internship= Internship.query.get(internship_id)
        if not internship:
            return None
        
        if start_date is not None:
            internship.start_date = start_date
        if end_date is not None:
            internship.end_date = end_date
        if status is not None:
            internship.status = status
        if tutor_id is not None:
            internship.tutor_id = tutor_id
        if company_id is not None:
            internship.company_id = company_id
        if student_id is not None:
            internship.student_id = student_id
        
        db.session.commit()
        return internship

    @staticmethod
    def delete_internship(internship_id):
        internship = Internship.query.get(internship_id)
        if not internship:
            return None
        
        db.session.delete(internship)
        db.session.commit()
        return internship
    
        # get all internships for a specific student
    @staticmethod
    def get_by_student(student_id):
        return Internship.query.filter_by(student_id=student_id).all()

    # get all internships for a specific company
    @staticmethod
    def get_by_company(company_id):
        return Internship.query.filter_by(company_id=company_id).all()
    
    # get all internships for a specific tutor
    @staticmethod
    def get_by_tutor(tutor_id):
        return Internship.query.filter_by(tutor_id=tutor_id).all()
    
    # get all internships with a specific status
    @staticmethod
    def get_by_status(status):
        return Internship.query.filter_by(status=status).all()
    
    # get all internships within a date range
    @staticmethod
    def get_by_date_range(start_date, end_date):
        return Internship.query.filter(Internship.start_date >= start_date, Internship.end_date <= end_date).all()
    
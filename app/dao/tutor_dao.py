from app import db
from app.model.tutor import Tutor
from app.model.user import User
from app.model.internships import Internship
from app.model.attendanceLogs import AttendanceLogs
from app.model.companies import Companies

class TutorsDAO:
    #get all tutors
    @staticmethod
    def get_all_tutors():
        return Tutor.query.all()

    # get a tutor by id
    @staticmethod
    def get_tutor_by_id(tutor_id):
        return Tutor.query.get(tutor_id)

    # get a tutor by email
    @staticmethod
    def get_by_email(email):
        return Tutor.query.filter_by(email=email).first()

    # Create a new tutor
    @staticmethod
    def create_tutor(name, surname, email, role, user_id=None, company_id=None):
        new_tutor = Tutor(
            name=name,
            surname=surname,
            email=email,
            role=role,
            user_id=user_id,
            company_id=company_id
        )
        db.session.add(new_tutor)
        db.session.commit()
        return new_tutor

    # Update an existing tutor
    @staticmethod
    def update_tutor(tutor_id, **kwargs):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return None

        for key, value in kwargs.items():
            if hasattr(tutor, key) and value is not None:
                setattr(tutor, key, value)

        db.session.commit()
        return tutor

    # Delete a tutor
    @staticmethod
    def delete_tutor(tutor_id):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return None

        db.session.delete(tutor)
        db.session.commit()
        return tutor

    # Get all attendance logs for a specific tutor
    @staticmethod
    def get_attendance_logs_for_tutor(tutor_id):
        tutor = Tutor.query.get(tutor_id)
        return tutor.attendance_logs if tutor else []

    # Get all internships for a specific tutor
    @staticmethod
    def get_internship_for_tutor(tutor_id):
        tutor = Tutor.query.get(tutor_id)
        return tutor.internship if tutor else None

    # get company for a specific tutor
    @staticmethod
    def get_company_for_tutor(tutor_id):
        tutor = Tutor.query.get(tutor_id)
        return tutor.company if tutor else None

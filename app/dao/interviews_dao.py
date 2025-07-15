from app import db
from app.model.interviews import Interview

class InterviewsDAO:
    @staticmethod
    def get_interview_by_id(interview_id):
        return Interview.query.get(interview_id)

    @staticmethod
    def get_all_interviews():
        return Interview.query.all()

    @staticmethod
    def add_interview(date, result, note, company_id, student_id):
        interview = Interview(
            date=date,
            result=result,
            note=note,
            company_id=company_id,
            student_id=student_id
        )
        db.session.add(interview)
        db.session.commit()
        return interview

    @staticmethod
    def update_interview(interview_id, date=None, result=None, notes=None, company_id=None, student_id=None):
        interview= Interview.query.get(interview_id)
        if not interview:
            return None
        
        if date is not None:
            interview.date = date
        if result is not None:
            interview.result = result
        if notes is not None:
            interview.notes = notes
        if company_id is not None:
            interview.company_id = company_id
        if student_id is not None:
            interview.student_id = student_id
        
        db.session.commit()
        return interview

    @staticmethod
    def delete_interview(interview):
        db.session.delete(interview)
        db.session.commit()

    # get interviews by student
    @staticmethod
    def get_by_student(student_id):
        return Interview.query.filter_by(student_id=student_id).all()
    
    # get interviews by company
    @staticmethod
    def get_by_company(company_id):
        return Interview.query.filter_by(company_id=company_id).all()
    
    # get interviews by date
    @staticmethod
    def get_by_date(interview_date):
        return Interview.query.filter_by(date=interview_date).all()
    
    @staticmethod
    def get_by_result(result_text):
        return Interview.query.filter_by(result=result_text).all()



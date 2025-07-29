from app.dao.interviews_dao import InterviewsDAO

class InterviewsService:
    @staticmethod
    def get_interview_by_id(interview_id):
        return InterviewsDAO.get_interview_by_id(interview_id)
    
    @staticmethod
    def get_all_interviews():
        return InterviewsDAO.get_all_interviews()
    
    @staticmethod
    def save_interview(date, result, note, company_id, student_id):
        return InterviewsDAO.add_interview(date, result, note, company_id, student_id)
    
    @staticmethod
    def update_interview(interview_id, date=None, result=None, notes=None, company_id=None, student_id=None):
        interview = InterviewsDAO.get_interview_by_id(interview_id)
        if not interview:
            raise ValueError(f"No interview found for interview id {interview_id}.")
        return InterviewsDAO.update_interview(interview_id, date, result, notes, company_id, student_id)
    
    @staticmethod
    def delete_interview(interview_id):
        interview = InterviewsDAO.get_interview_by_id(interview_id)
        if not interview:
            raise ValueError(f"No interview found for interview id {interview_id}.")
        InterviewsDAO.delete_interview(interview)
        return True
    
    @staticmethod
    def get_interviews_by_student(student_id):
        interviews = InterviewsDAO.get_by_student(student_id)
        if not interviews:
            raise ValueError(f"No interviews found for student id {student_id}.")
        return interviews
    
    @staticmethod
    def get_interviews_by_company(company_id):
        interviews = InterviewsDAO.get_by_company(company_id)
        if not interviews:
            raise ValueError(f"No interviews found for company id {company_id}.")
        return interviews
    
    @staticmethod
    def get_interviews_by_date(date):
        interviews = InterviewsDAO.get_by_date(date)
        if not interviews:
            raise ValueError(f"No interviews found for date {date}.")
        return interviews
    
    @staticmethod
    def get_by_result(result_text):
        interviews = InterviewsDAO.get_by_result(result_text)
        if not interviews:
            raise ValueError(f"No interviews found with result {result_text}.")
        return interviews
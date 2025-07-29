from app.dao.students_dao import StudentsDAO

class StudentsService:
    @staticmethod
    def get_all_students():
        return StudentsDAO.get_all_students()
    
    @staticmethod
    def get_student_by_id(student_id):
        student = StudentsDAO.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        return student
    
    @staticmethod
    def get_student_by_email(email):
        return StudentsDAO.get_by_email(email)
    
    @staticmethod
    def create_student(name, surname, email, phone, status, user_id=None, class_id=None):
        return StudentsDAO.create_student(name, surname, email, phone, status, user_id, class_id)
    
    @staticmethod
    def update_student(student_id, **kwargs):
        student = StudentsDAO.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        return StudentsDAO.update_student(student_id, **kwargs)
    
    @staticmethod
    def delete_student(student_id):
        student = StudentsDAO.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        StudentsDAO.delete_student(student_id)
        return True
    
    @staticmethod
    def get_interviews_for_student(student_id):
        student = StudentsDAO.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        return StudentsDAO.get_interviews_for_student(student_id)
    
    @staticmethod
    def get_internship_for_student(student_id):
        student = StudentsDAO.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        return StudentsDAO.get_internship_for_student(student_id)
    
    @staticmethod
    def get_class_for_student(student_id):
        student = StudentsDAO.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        return StudentsDAO.get_class_for_student(student_id)
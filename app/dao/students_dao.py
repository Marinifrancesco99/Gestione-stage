from app import db
from app.model.students import Student
from app.model.classes import Classes
from app.model.internships import Internship
from app.model.interviews import Interview


class StudentsDAO:
    # get all students
    @staticmethod
    def get_all_students():
        return Student.query.all()

    # get a student by id
    @staticmethod
    def get_student_by_id(student_id):
        return Student.query.get(student_id)

    # get a student by email
    @staticmethod
    def get_by_email(email):
        return Student.query.filter_by(email=email).first()

    # create a new student
    @staticmethod
    def create_student(name, surname, email, phone, status, user_id=None, class_id=None):
        new_student = Student(
            name=name,
            surname=surname,
            email=email,
            phone=phone,
            status=status,
            user_id=user_id,
            class_id=class_id
        )
        db.session.add(new_student)
        db.session.commit()
        return new_student

    # update a student
    @staticmethod
    def update_student(student_id, **kwargs):
        student = Student.query.get(student_id)
        if not student:
            return None
        
        for key, value in kwargs.items():
            if hasattr(student, key) and value is not None:
                setattr(student, key, value)
        
        db.session.commit()
        return student

    # delete a student
    @staticmethod
    def delete_student(student_id):
        student = Student.query.get(student_id)
        if not student:
            return None
        
        db.session.delete(student)
        db.session.commit()
        return student

    #   get all interviews for a specific student
    @staticmethod
    def get_interviews_for_student(student_id):
        student = Student.query.get(student_id)
        return student.interview if student else []

    # get internship for a specific student
    @staticmethod
    def get_internship_for_student(student_id):
        student = Student.query.get(student_id)
        return student.internship if student else None

    # get class for a specific student
    @staticmethod
    def get_class_for_student(student_id):
        student = Student.query.get(student_id)
        return student.classe if student else None


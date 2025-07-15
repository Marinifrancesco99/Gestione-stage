from app import db
from app.model.professors import Professor

class ProfessorsDAO:
    @staticmethod
    def get_professor_by_id(professor_id):
        return Professor.query.get(professor_id)

    @staticmethod
    def get_all_professors():
        return Professor.query.all()

    @staticmethod
    def create_professor(name, surname, email, phone=None, vote=None, evaluation=None, note=None):
        professor = Professor(
            name=name,
            surname=surname,
            email=email,
            phone=phone,
            vote=vote,
            evaluation=evaluation,
            note=note
        )
        db.session.add(professor)
        db.session.commit()
        return professor

    @staticmethod
    def update_professor(professor_id, name=None, surname=None, email=None, phone=None, vote=None, evaluation=None, note=None):
        professor = Professor.query.get(professor_id)
        if not professor:
            return None
        
        if name is not None:
            professor.name = name
        if surname is not None:
            professor.surname = surname
        if email is not None:
            professor.email = email
        if phone is not None:
            professor.phone = phone
        if vote is not None:
            professor.vote = vote
        if evaluation is not None:
            professor.evaluation = evaluation
        if note is not None:
            professor.note = note

        db.session.commit()
        return professor

    @staticmethod
    def delete_professor(professor_id):
        professor = Professor.query.get(professor_id)
        if not professor:
            return None
        
        db.session.delete(professor)
        db.session.commit()
        return professor

    # get al professor for a email
    @staticmethod
    def get_by_email(email):
        return Professor.query.filter_by(email=email).first()

    # Get all professors for a specific course
    @staticmethod
    def get_by_course(course_id):
        return Professor.query.filter(Professor.courses.any(id=course_id)).all()

    # add a course to a professor (N:N)  Quando vuoi associare un corso esistente a un professore (es. da interfaccia admin)
    @staticmethod
    def add_course(professor_id, course):
        professor = Professor.query.get(professor_id)
        if professor and course not in professor.courses:
            professor.courses.append(course)
            db.session.commit()
        return professor

    # remove a course from a professor (N:N)  Quando vuoi rimuovere un corso associato a un professore (es. da interfaccia admin)
    @staticmethod
    def remove_course(professor_id, course):
        professor = Professor.query.get(professor_id)
        if professor and course in professor.courses:
            professor.courses.remove(course)
            db.session.commit()
        return professor

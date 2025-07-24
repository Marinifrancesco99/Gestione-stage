from app.dao.classes_dao import ClassesDAO

class ClassesService:
    @staticmethod
    def get_all_classes():
        return ClassesDAO.get_all_classes()

    @staticmethod
    def get_class_by_id(id):
        the_class = ClassesDAO.get_classes_by_id(id)
        if not the_class:
            raise ValueError(f"Class with id {id} not found.")
        return the_class

    @staticmethod
    def save_class(name, course_id):
        return ClassesDAO.create_class(name, course_id)

    @staticmethod
    def update_class(id, name=None):
        existing_class = ClassesDAO.get_classes_by_id(id)
        if not existing_class:
            raise ValueError(f"Class with id {id} not found.")
        return ClassesDAO.update_class(id, name)

    @staticmethod
    def delete_class(id):
        the_class = ClassesDAO.get_classes_by_id(id)
        if not the_class:
            raise ValueError(f"Class with id {id} not found.")
        ClassesDAO.delete_class(id)
        return True

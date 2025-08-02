from flask import jsonify
from app.service.classes_service import ClassesService

class ClassesController:
    @staticmethod
    def get_all_classes():
        classes = ClassesService.get_all_classes()
        return jsonify([log.to_dict() for log in classes]), 200
    
    @staticmethod
    def get_class_by_id(id):
        classe = ClassesService.get_class_by_id(id)
        return jsonify(classe.to_dict()), 200
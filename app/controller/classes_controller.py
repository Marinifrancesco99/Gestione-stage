from flask import jsonify, request
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
    
    @staticmethod
    def save_class():
        data = request.get_json()
        classe = ClassesService.save_class(
            name=data["name"],
            course_id=data["course_id"]
        )
        return jsonify(classe.to_dict()), 201
    
    @staticmethod
    def update_class(id):
        data = request.get_json()
        classe = ClassesService.update_class(
            id=id,
            name=data["name"],
            course_id=data["course_id"]
        )
        return jsonify(classe.to_dict()), 200
    
    @staticmethod
    def delete_class(id):
        ClassesService.delete_class(id)
        return jsonify({"message": "Class deleted successfully"}), 200


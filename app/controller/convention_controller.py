from flask import jsonify, request
from app.service.convention_service import ConventionService

class ConventionController:
    @staticmethod
    def get_all_conventions():
        conventions = ConventionService.get_all_conventions()
        return jsonify([con.to_dict() for con in conventions]), 200
    
    @staticmethod
    def get_convention_by_id(id):
        convention = ConventionService.get_convention_by_id(id)
        return jsonify(convention.to_dict()), 200
    
    @staticmethod
    def save_convention():
        data = request.get_json()
        convention = ConventionService.save_convention(
            internship_id=data["internship_id"],
            document_filename=data["document_filename"],
            note=data.get("note")
        )
        return jsonify(convention.to_dict()), 201

    @staticmethod
    def update_convention(id):
        data = request.get_json()
        convention = ConventionService.update_convention(
            id=id,
            downloaded=data["downloaded"],
            signed=data["signed"],
            download_date=data["download_date"],
            signed_date=data["signed_date"],
            signed_by=data["signed_by"],
            note=data.get("note"),
            document_filename=data["document_filename"]
        )
        return jsonify(convention.to_dict()), 200
    
    @staticmethod
    def delete_convention(id):
        ConventionService.delete_convention(id)
        return jsonify({"message": "Convention deleted successfully"}), 200
    
    @staticmethod
    def get_signed_conventions():
        conventions = ConventionService.get_signed_conventions()
        return jsonify([conv.to_dict() for conv in conventions])
    
    @staticmethod
    def get_downloaded_conventions():
        conventions = ConventionService.get_downloaded_conventions()
        return jsonify([con.to_dict() for con in conventions])
    
    @staticmethod
    def get_conventions_by_internship_id(internship_id):
        conventions = ConventionService.get_conventions_by_internship_id(internship_id)
        return jsonify([con.to_dict() for con in conventions])
    
    @staticmethod
    def get_conventions_by_user_id(user_id):
        conventions = ConventionService.get_conventions_by_user_id(user_id)
        return jsonify([con.to_dict() for con in conventions])
    
    @staticmethod
    def get_downloaded_but_not_signed():
        conventions = ConventionService.get_downloaded_but_not_signed()
        return jsonify([con.to_dict() for con in conventions])
    
    @staticmethod
    def get_conventions_by_document_filename(document_filename):
        conventions = ConventionService.get_conventions_by_document_filename(document_filename)
        return jsonify([conv.to_dict() for conv in conventions])


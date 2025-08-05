from flask import jsonify, request
from app.service.companyTipes_service import CompanyTypesService

class CompanyTipesController:
    @staticmethod
    def get_all_company_tipes():
        company_types = CompanyTypesService.get_all_company_tipes()
        return jsonify([types.to_dict() for types in company_types]), 200
    
    @staticmethod
    def get_company_type_by_id(id):
        company_type = CompanyTypesService.get_company_type_by_id(id)
        return jsonify(company_type.to_dict()), 200
    
    @staticmethod
    def save_company_type():
        data = request.get_json()
        company_type = CompanyTypesService.save_company_type(
            name=data["name"]
        )
        return jsonify(company_type.to_dict()), 201
    
    @staticmethod
    def update_company_type(id):
        data = request.get_json()
        company_type = CompanyTypesService.update_company_type(
            id=id,
            name=data["name"]
        )
        return jsonify(company_type.to_dict()), 200
    
    @staticmethod
    def delete_company_type(id):
        CompanyTypesService.delete_company_type(id)
        return jsonify({"message": "Company Types deleted successfully"}), 200
        
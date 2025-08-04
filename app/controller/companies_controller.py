from flask import jsonify, request
from app.service.companies_service import CompaniesService

class CompaniesController:
    @staticmethod
    def get_all_companies():
        companies = CompaniesService.get_all_companies()
        return jsonify([com.to_dict() for com in companies]), 200
    
    @staticmethod
    def get_company_by_id(id):
        company = CompaniesService.get_company_by_id(id)
        return jsonify(company.to_dict()), 200
    
    @staticmethod 
    def save_company():
        data = request.get_json()
        company = CompaniesService.save_company(
            number=data["number"],
            companyName=data["companyName"],
            address=data["address"],
            email=data["email"],
            province=data["province"],
            note=data["note"],
            city=data["city"],
            cap=data["cap"],
            partitaIVA=data["partitaIVA"],
            type_id=data["type_id"]
        )
        return jsonify(company.to_dict()), 201
    
    @staticmethod
    def update_company(id):
        data = request.get_json()
        company = CompaniesService.update_company(
            id=id,
            number=data["number"],
            companyName=data["companyName"],
            address=data["address"],
            email=data["email"],
            province=data["province"],
            note=data["note"],
            city=data["city"],
            cap=data["cap"],
            partitaIVA=data["partitaIVA"],
            type_id=data["type_id"]
        )
        return jsonify(company.to_dict()), 200
    
    @staticmethod
    def delete_company(id):
        CompaniesService.delete_company(id)
        return jsonify({"message": "Company deleted successfully"}), 200
    
    @staticmethod
    def search_by_sector(sector):
        companies= CompaniesService.search_by_sector(sector)
        return jsonify([com.to_dict() for com in companies]), 200
    
    @staticmethod
    def search_by_city(city):
        companies = CompaniesService.search_by_city(city)
        return jsonify([com.to_dict() for com in companies]), 200
    
    @staticmethod
    def search_by_name(name):
        companies = CompaniesService.search_by_name(name)
        return jsonify([com.to_dict() for com in companies]), 200
    
    @staticmethod
    def search_by_min_students(min_students):
        companies = CompaniesService.search_by_min_students(min_students)
        return jsonify([com.to_dict() for com in companies]), 200
    
    @staticmethod
    def search_available_in_period(start_date, end_date):
        companies = CompaniesService.search_available_in_period(start_date, end_date)
        return jsonify([com.to_dict() for com in companies]), 200
    
    @staticmethod
    def advanced_search(sector=None, city=None, min_students=None):
        sector = request.args.get("sector")
        city = request.args.get("city")
        min_students = request.args.get("min_students", type=int)
        
        companies = CompaniesService.advanced_search(sector, city, min_students)
        return jsonify([com.to_dict() for com in companies]), 200
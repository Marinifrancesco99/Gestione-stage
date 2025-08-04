from flask import Blueprint, request
from app.controller.companies_controller import CompaniesController
from app.utils.decorators import token_required, roles_required

companies_bp = Blueprint('companies', __name__)

@companies_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_companies():
    return CompaniesController.get_all_companies()

@companies_bp.route("/<int:id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_company_by_id(id):
    return CompaniesController.get_company_by_id(id)

@companies_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def save_company():
    return CompaniesController.save_company()

@companies_bp.route("/<int:id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_company(id):
    return CompaniesController.update_company(id)

@companies_bp.route("/<int:id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_company(id):
    return CompaniesController.delete_company(id)

@companies_bp.route("/sector/<string:sector>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def search_by_sector(sector):
    return CompaniesController.search_by_sector(sector)

@companies_bp.route("/city/<string:city>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def search_by_city(city):
    return CompaniesController.search_by_city(city)

@companies_bp.route("/name/<string:name>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def search_by_name(name):
    return CompaniesController.search_by_name(name)

@companies_bp.route("/min-students/<int:min_students>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def search_by_min_students(min_students):
    return CompaniesController.search_by_min_students(min_students)


@companies_bp.route("/available", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def search_available_in_period():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    return CompaniesController.search_available_in_period(start_date, end_date)


@companies_bp.route("/advanced-search", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def advanced_search():
    return CompaniesController.advanced_search()

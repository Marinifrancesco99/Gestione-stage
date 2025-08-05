from flask import Blueprint
from app.controller.companyTipes_controller import CompanyTipesController
from app.utils.decorators import token_required, roles_required

companyTipes_bp = Blueprint('companyTipes', __name__)

@companyTipes_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_company_tipes():
    return CompanyTipesController.get_all_company_tipes()

@companyTipes_bp.route("/<int:id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_company_tipe_by_id(id):
    return CompanyTipesController.get_company_type_by_id(id)

@companyTipes_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def save_company_tipe():
    return CompanyTipesController.save_company_type()

@companyTipes_bp.route("/<int:id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_company_tipe(id):
    return CompanyTipesController.update_company_type(id)

@companyTipes_bp.route("/<int:id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_company_tipes(id):
    return CompanyTipesController.delete_company_type(id)
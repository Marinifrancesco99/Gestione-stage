from app import db
from app.model.companyTipes import CompanyTypes

class CompanyTypesDao:
    # get all company types
    @staticmethod
    def get_all_company_types():
        return CompanyTypes.query.all()

    # get company type by id
    @staticmethod
    def get_company_type_by_id(id):
        return CompanyTypes.query.get(id)

    # create a new company type
    @staticmethod
    def create_company_type(name):
        company_type = CompanyTypes(
            name=name
        )
        db.session.add(company_type)
        db.session.commit() 
        return company_type

    # update company type by id
    @staticmethod
    def update_company_type(id, name=None):
        company_type = CompanyTypes.query.get(id)
        if not company_type:
            return None

        if name is not None:
            company_type.name = name

        db.session.commit()
        return company_type

    # delete company type by id
    @staticmethod
    def delete_company_type(id):
        company_type = CompanyTypes.query.get(id)
        if not company_type:
            return None

        db.session.delete(company_type)
        db.session.commit()
        return company_type
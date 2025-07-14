from app import db
from app.model.companyTipes import CompanyTypes

# get all company types
def get_all_company_types():
    return CompanyTypes.query.all()

# get company type by id
def get_company_type_by_id(id):
    return CompanyTypes.query.get(id)

# create a new company type
def create_company_type(name):
    type = CompanyTypes(
        name=name
    )
    db.session.add(type)
    db.session.commit() 
    return type

# update company type by id
def update_company_type(id, name=None):
    type = CompanyTypes.query.get(id)
    if not type:
        return None

    if name is not None:
        type.name = name

    db.session.commit()
    return type

# delete company type by id
def delete_company_type(id):
    type = CompanyTypes.query.get(id)
    if not type:
        return None

    db.session.delete(type)
    db.session.commit()
    return type
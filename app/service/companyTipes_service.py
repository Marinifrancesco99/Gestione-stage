from app.dao.companyTipes_dao import CompanyTypesDao

class CompanyTypesService:
    @staticmethod
    def get_all_company_tipes():
        return CompanyTypesDao.get_all_company_types()
    
    @staticmethod
    def get_company_type_by_id(id):
        company_type = CompanyTypesDao.get_company_type_by_id(id)
        if not company_type:
            raise ValueError(f"Company Type with id {id} not found.")
        return company_type
    
    @staticmethod
    def save_company_type(name):
        return CompanyTypesDao.create_company_type(name)
    
    @staticmethod
    def update_company_type(id, name=None):
        existing_company_type = CompanyTypesDao.get_company_type_by_id(id)
        if not existing_company_type:
            raise ValueError(f"Company Type with id {id} not found.")
        return CompanyTypesDao.update_company_type(id, name)
    
    @staticmethod
    def delete_company_type(id):
        company_type = CompanyTypesDao.get_company_type_by_id(id)
        if not company_type:
            raise ValueError(f"Company Type with id {id} not found.")
        CompanyTypesDao.delete_company_type(id)
        return True
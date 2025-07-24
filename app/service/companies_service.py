from app.dao.companies_dao import CompaniesDAO

class CompaniesService:
    @staticmethod
    def get_all_companies():
        return CompaniesDAO.get_all_companies()
    
    @staticmethod
    def get_company_by_id(id):
        company = CompaniesDAO.get_company_by_id(id)
        if not company:
            raise ValueError(f"Company not found with id: {id}")
        return company
    
    @staticmethod
    def save_company(number, companyName, address, email, province, note, city, cap, partitaIVA, type_id):
        return CompaniesDAO.create_company(number, companyName, address, email, province, note, city, cap, partitaIVA, type_id)
    
    @staticmethod
    def update_company(id, number=None, companyName=None, address=None, email=None, province=None, note=None, city=None, cap=None, partitaIVA=None, type_id=None):
        existing_company = CompaniesDAO.get_company_by_id(id)
        if not existing_company:
            raise ValueError(f"Company not found with id: {id}")
        return CompaniesDAO.update_company(id, number, companyName, address, email, province, note, city, cap, partitaIVA, type_id)
    
    @staticmethod
    def delete_company(id):
        company = CompaniesDAO.get_company_by_id(id)
        if not company:
            raise ValueError(f"Company not found with id: {id}")
        CompaniesDAO.delete_company(id)
        return True
    
    @staticmethod
    def search_by_sector(sector):
        companies = CompaniesDAO.search_by_sector(sector)
        if not companies:
            raise ValueError(f"No companies found for sector: {sector}")
        return companies
    
    @staticmethod
    def search_by_city(city):
        companies = CompaniesDAO.search_by_city(city)
        if not companies:
            raise ValueError(f"No companies found in city: {city}")
        return companies
    
    @staticmethod
    def search_by_name(name):
        companies = CompaniesDAO.search_by_name(name)
        if not companies:
            raise ValueError(f"No companies found with name: {name}")
        return companies
    
    @staticmethod
    def search_by_min_students(min_students):
        companies = CompaniesDAO.search_by_min_students(min_students)
        if not companies:
            raise ValueError(f"No companies found with minimum students: {min_students}")
        return companies
    
    @staticmethod
    def search_available_in_period(start_date, end_date):
        companies = CompaniesDAO.search_available_in_period(start_date, end_date)
        if not companies:
            raise ValueError(f"No companies available in the period from {start_date} to {end_date}")
        return companies
    
    @staticmethod
    def advanced_search(sector=None, city=None, min_students=None):
        companies = CompaniesDAO.advanced_search(sector, city, min_students)
        if not companies:
            raise ValueError("No companies found for the given search criteria")
        return companies
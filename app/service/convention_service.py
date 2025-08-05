from app.dao.convention_dao import ConventionDao
from app.exceptions.not_found import NotFoundException

class ConventionService:
    @staticmethod
    def get_all_conventions():
        return ConventionDao.get_all_conventions()
    
    @staticmethod
    def get_convention_by_id(id):
        convention = ConventionDao.get_convention_by_id(id)
        if not convention:
            raise NotFoundException (f"Convention with id: {id} not found.")
        return convention
    
    @staticmethod
    def save_convention(internship_id, document_filename=None, note=None):
        return ConventionDao.create_convention(internship_id, document_filename, note)
    
    @staticmethod
    def update_convention(id, downloaded=None, signed=None, download_date=None, signed_date=None, signed_by=None, note=None, document_filename=None):
        convention = ConventionDao.get_convention_by_id(id)
        if not convention:
            raise NotFoundException (f"Convention with id: {id} not found.")
        return ConventionDao.update_convention(
            id, downloaded, signed, download_date, signed_date, signed_by, note, document_filename
        )
        
    @staticmethod
    def delete_convention(id):
        convention = ConventionDao.get_convention_by_id(id)
        if not convention:
            raise NotFoundException (f"Convention with id: {id} not found.")
        return ConventionDao.delete_convention(id)
    
    @staticmethod
    def get_signed_conventions():
        return ConventionDao.get_signed_conventions()
    
    @staticmethod
    def get_downloaded_conventions():
        return ConventionDao.get_downloaded_conventions()
    
    @staticmethod
    def get_conventions_by_internship_id(internship_id):
        conventions = ConventionDao.get_conventions_by_internship_id(internship_id)
        if not conventions:
            raise NotFoundException (f"Convention with id: {internship_id} not found.")
        return conventions
    
    @staticmethod
    def get_conventions_by_user_id(user_id):
        conventions = ConventionDao.get_conventions_by_user_id(user_id)
        if not conventions:
            raise NotFoundException (f"Convention with id: {user_id} not found.")
        return conventions
    
    @staticmethod
    def get_downloaded_but_not_signed():
        return ConventionDao.get_downloaded_but_not_signed()
    
    @staticmethod
    def get_conventions_by_document_filename(document_filename):
        conventions = ConventionDao.get_conventions_by_document_filename(document_filename)
        if not conventions:
            raise NotFoundException (f"Convention with id: {document_filename} not found.")
        return conventions
    
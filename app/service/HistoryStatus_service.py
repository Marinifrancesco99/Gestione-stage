from app.dao.HistoryStatus_dao import HistoryStatusDAO

class HistoryStatusService:
    @staticmethod
    def get_all_history_status():
        return HistoryStatusDAO.get_all_history_status()
    
    @staticmethod
    def get_history_status_by_id(status_id):
        status = HistoryStatusDAO.get_history_status_by_id(status_id)
        if not status:
            raise ValueError(f"History status with ID {status_id} not found.")
        return status
    
    @staticmethod
    def get_by_internship(internship_id):
        statues = HistoryStatusDAO.get_by_internship(internship_id)
        if not statues:
            raise ValueError(f"No history statuses found for internship ID {internship_id}.")
        return statues
    
    @staticmethod
    def save_history_status(internship_id, status, changed_by=None, note=None, reason=None):
        return HistoryStatusDAO.create_history_status(
            internship_id, status, changed_by, note, reason
        )
        
    @staticmethod
    def update_history_status(status_id, status=None, changed_by=None, note=None, reason=None):
        existing_status = HistoryStatusDAO.get_history_status_by_id(status_id)
        if not existing_status:
            raise ValueError(f"History status with ID {status_id} not found.")
        return HistoryStatusDAO.update_history_status(
            status_id, status, changed_by, note, reason
        )
    
    @staticmethod
    def delete_status(status_id):
        existing_status = HistoryStatusDAO.get_history_status_by_id(status_id)
        if not existing_status:
            raise ValueError(f"History status with ID {status_id} not found.")
        HistoryStatusDAO.delete_status(status_id)
        return True
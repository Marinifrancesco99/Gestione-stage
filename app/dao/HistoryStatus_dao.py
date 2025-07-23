from app.extension import db
from app.model.HistoryStatus import HistoryStatus
from datetime import datetime

class HistoryStatusDAO:
    @staticmethod
    def get_all_history_status():
        return HistoryStatus.query.all()
    
    @staticmethod
    def get_history_status_by_id(status_id):
        return HistoryStatus.query.get(status_id)
    
    # Ottieni tutti gli status per uno specifico internship dal più recente al più vecchio
    @staticmethod
    def get_by_internship(internship_id):
        return HistoryStatus.query.filter_by(internship_id=internship_id).order_by(HistoryStatus.changed_at.desc()).all()
    
    @staticmethod
    def create_history_status(internship_id, status, changed_by=None, note=None, reason=None):
        new_status=HistoryStatus(
            internship_id=internship_id,
            status=status,
            changed_by=changed_by,
            note=note,
            reason=reason,
            changed_at=datetime.utcnow()
        )
        db.session.add(new_status)
        db.session.commit()
        return new_status
    
    @staticmethod
    def update_history_status(status_id, status=None, changed_by=None, note=None, reason=None):
        history_status = HistoryStatus.query.get(status_id)
        if not history_status:
            return None
        
        if status is not None:
            history_status.status = status
        if changed_by is not None:
            history_status.changed_by = changed_by
        if note is not None:
            history_status.note = note
        if reason is not None:
            history_status.reason = reason
        
        history_status.changed_at = datetime.utcnow()
        db.session.commit()
        return history_status
    
    @staticmethod
    def delete_status(status_id):
        history_status = HistoryStatus.query.get(status_id)
        if not history_status:
            return False

        db.session.delete(history_status)
        db.session.commit()
        return True
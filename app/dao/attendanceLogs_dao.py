from app import db
from app.model.attendanceLogs import AttendanceLogs


class AttendanceLogDAO:
    @staticmethod
    def get_all_attendanceLogs():
        return AttendanceLogs.query.all()

    @staticmethod
    def get_attendanceLog_by_id(id):
        return AttendanceLogs.query.get(id)

    @staticmethod
    def create_attendanceLog(date, start_time, end_time, notes, register_signature, tutor_id, internship_id, validation=False):
        new_log = AttendanceLogs(
            date=date,
            start_time=start_time,
            end_time=end_time,
            notes=notes,
            validation=validation,
            register_signature=register_signature,
            tutor_id=tutor_id,
            internship_id=internship_id
        )
        db.session.add(new_log)
        db.session.commit()
        return new_log

    @staticmethod
    def get_attendanceLog_by_internship_id(internship_id):
        return AttendanceLogs.query.filter_by(internship_id=internship_id).all()

    @staticmethod
    def get_attendanceLog_by_tutor_id(tutor_id):
        return AttendanceLogs.query.filter_by(tutor_id=tutor_id).all()

    @staticmethod
    def update_attendanceLog(id, date=None, start_time=None, end_time=None, notes=None, register_signature=None, validation=None):
        log = AttendanceLogs.query.get(id)
        if not log:
            return None

        if date is not None:
            log.date = date
        if start_time is not None:
            log.start_time = start_time
        if end_time is not None:
            log.end_time = end_time
        if notes is not None:
            log.notes = notes
        if validation is not None:
            log.validation = validation
        if register_signature is not None:
            log.register_signature = register_signature

        db.session.commit()
        return log


    @staticmethod
    def delete_attendanceLog(id):
        log = AttendanceLogs.query.get(id)
        if not log:
            return None
    
        db.session.delete(log)
        db.session.commit()
        return log






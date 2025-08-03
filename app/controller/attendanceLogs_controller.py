from flask import request, jsonify
from app.service.attendanceLogs_service import AttendanceLogsService


class AttendanceLogsController:
    @staticmethod
    def get_all_attendance_logs():
        logs = AttendanceLogsService.get_all_attendance_logs()
        return jsonify([log.to_dict() for log in logs]), 200
    
    @staticmethod
    def get_attendance_log_by_id(id):
        logs = AttendanceLogsService.get_attendanceLog_by_id(id)
        return jsonify(logs.to_dict()), 200
    
    @staticmethod
    def save_attendance_log():
        data = request.get_json()
        log = AttendanceLogsService.save_attendanceLog(
            date=data["date"],                          # Estraggo manualmente la data altrimenti il metodo non funzionerebbe
            start_time=data["start_time"],              # Estraggo manualmente l'orario di inizio altrimenti il metodo non funzionerebbe
            end_time=data["end_time"],                  # Estraggo manualmente l'orario di fine altrimenti il metodo non funzionerebbe
            notes=data["notes"],                        # Estraggo manualmente le note altrimenti il metodo non funzionerebbe
            register_signature=data["register_signature"],    # Estraggo manualmente la firma di registrazione altrimenti il metodo non funzionerebbe
            tutor_id=data["tutor_id"],                  # Estraggo manualmente l'id del tutor altrimenti il metodo non funzionerebbe
            internship_id=data["internship_id"],        # Estraggo manualmente l'id dello stage altrimenti il metodo non funzionerebbe
            validation=data.get("validation", False)    # Estraggo manualmente la validazione altrimenti il metodo non funzionerebbe
        )
        return jsonify(log.to_dict()), 201
    
    @staticmethod
    def get_attendanceLog_by_internship_id(internship_id):
        log = AttendanceLogsService.get_attendanceLog_by_internship_id(internship_id)
        return jsonify([l.to_dict() for l in log]), 200

    
    @staticmethod
    def get_attendanceLog_by_tutor_id(tutor_id):
        log = AttendanceLogsService.get_attendanceLog_by_tutor_id(tutor_id)
        return jsonify([l.to_dict() for l in log]), 200

    
    @staticmethod
    def update_attendance_log(id):
        data = request.get_json()
        log = AttendanceLogsService.update_attendanceLog(
            id=id,
            date=data["date"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            notes=data["notes"],
            register_signature=data["register_signature"],
            validation=data.get("validation", False)
        )
        return jsonify(log.to_dict()), 200
    
    @staticmethod
    def delete_attendance_log(id):
        AttendanceLogsService.delete_attendanceLog(id)
        return jsonify({"message": "Attendance log deleted successfully"}), 200
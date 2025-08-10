from flask import jsonify, request
from app.service.interviews_Service import InterviewsService

class InterviewsController:
    @staticmethod
    def get_interview_by_id(interview_id):
        interview = InterviewsService.get_interview_by_id(interview_id)
        return jsonify(interview.to_dict()), 200

    @staticmethod
    def get_all_interviews():
        interviews = InterviewsService.get_all_interviews()
        return jsonify([inte.to_dict() for inte in interviews]), 200

    @staticmethod
    def save_interview():
        data = request.get_json()
        interview = InterviewsService.save_interview(
            date=data["date"],
            result=data["result"],
            note=data["note"],
            company_id=data["company_id"],
            student_id=data["student_id"]
        )
        return jsonify(interview.to_dict()), 201

    @staticmethod
    def update_interview(interview_id):
        data = request.get_json()
        interview = InterviewsService.update_interview(
            interview_id=interview_id,
            date=data.get("date"),
            result=data.get("result"),
            notes=data.get("notes"),
            company_id=data.get("company_id"),
            student_id=data.get("student_id")
        )
        return jsonify(interview.to_dict()), 200

    @staticmethod
    def delete_interview(interview_id):
        InterviewsService.delete_interview(interview_id)
        return jsonify({"message": "Interview deleted successfully"}), 200

    @staticmethod
    def get_interviews_by_student(student_id):
        interviews = InterviewsService.get_interviews_by_student(student_id)
        return jsonify([inte.to_dict() for inte in interviews]), 200

    @staticmethod
    def get_interviews_by_company(company_id):
        interviews = InterviewsService.get_interviews_by_company(company_id)
        return jsonify([inte.to_dict() for inte in interviews]), 200

    @staticmethod
    def get_interviews_by_date(date):
        interviews = InterviewsService.get_interviews_by_date(date)
        return jsonify([inte.to_dict() for inte in interviews]), 200

    @staticmethod
    def get_by_result(result_text):
        interviews = InterviewsService.get_by_result(result_text)
        return jsonify([inte.to_dict() for inte in interviews]), 200

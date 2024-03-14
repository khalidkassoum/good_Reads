
from infra.api_wrapper import ExamAPI

class ExamData:
    @staticmethod
    def get_exam_list():
        response = ExamAPI.get_exams()
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def get_upcoming_exam_list():
        response = ExamAPI.get_upcoming_exams()
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def get_exams_for_year(year):
        response = ExamAPI.get_exams_by_year(year)
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def get_exam_details_by_name(name):
        response = ExamAPI.get_exam_by_name(name)

        if response.status_code == 200:
            return response.json()

        data = response.json()
        if response.status_code == 200:
            return data

        return None

    @staticmethod
    def get_profession_list():
        response = ExamAPI.get_professions()
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def get_upcoming_exam_info():
        response = ExamAPI.get_upcoming_exam()
        if response.status_code == 200:
            return response.json()
        return None
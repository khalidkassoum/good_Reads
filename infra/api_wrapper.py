import requests
class ExamAPI:
    BASE_URL = "https://api.whenisthenextboardexam.com"

    @staticmethod
    def get_exams():
        return requests.get(f"{ExamAPI.BASE_URL}/exams")

    @staticmethod
    def get_upcoming_exams():
        return requests.get(f"{ExamAPI.BASE_URL}/exams/upcoming")

    @staticmethod
    def get_exams_by_year(year):
        return requests.get(f"{ExamAPI.BASE_URL}/exams/{year}")

    @staticmethod
    def get_upcoming_exam():
        return requests.get(f"{ExamAPI.BASE_URL}/exam/upcoming")

    @staticmethod
    def get_exam_by_name(name):
        return requests.get(f"{ExamAPI.BASE_URL}/exam/{name}")

    @staticmethod
    def get_professions():

        return requests.get(f"{ExamAPI.BASE_URL}/professions")

        return requests.get(f"{ExamAPI.BASE_URL}/professions")


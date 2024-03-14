# test_exams_api.py
import unittest



from infra.api_wrapper import ExamAPI
from logic.mylogic import ExamData
class test_exam(unittest.TestCase):

 def test_get_exams_status_code(self):

    response = ExamAPI.get_exams()

    response = ExamAPI.get_exams()
    if response.status_code == 200:
        print("Response:", response.json())  # Prints the JSON response
    else:
        print(f"Failed to fetch exams: {response.status_code}")

    assert response.status_code == 200

 def test_get_exams_response_format(self):

    exams = ExamData.get_exam_list()
    assert exams is not None, "Failed to get exam data"
    assert isinstance(exams, list), "Exams should be a list"

 def test_get_exams_content(self):

    exams = ExamData.get_exam_list()
    self.assertTrue(exams!=None), "Exam list is empty"

 # Add to test_exams_api.py
 def test_get_upcoming_exams_status_code(self):


     response = ExamAPI.get_upcoming_exams()

     response = ExamAPI.get_upcoming_exams()
     if response.status_code == 200:
         print("Response:", response.json())  # Prints the JSON response
     else:
         print(f"Failed to fetch exams: {response.status_code}")

     assert response.status_code == 200

 def test_get_upcoming_exams_response_format(self):

     upcoming_exams = ExamData.get_upcoming_exam_list()
     assert upcoming_exams is not None, "Failed to get upcoming exam data"
     assert isinstance(upcoming_exams, list), "Upcoming exams should be a list"

 def test_get_upcoming_exams_content(self):

     upcoming_exams = ExamData.get_upcoming_exam_list()
     self.assertTrue(upcoming_exams != None), "Exam list is empty"

 # test_exams_api.py update
 def test_get_exams_by_year_status_code(self,year=2023):
     response = ExamAPI.get_exams_by_year(year)
     assert response.status_code == 200

 def test_get_exams_by_year_response_format(self,year=2022):
     exams = ExamData.get_exams_for_year(year)
     assert exams is not None, "Failed to get exam data for the specified year"
     assert isinstance(exams, list), "Response format is not as expected; should be a list"

 def test_get_exams_by_year_content(self,year=2022):
     exams = ExamData.get_exams_for_year(year)
     assert exams, f"Exam list for year {year} is empty"

 def test_get_exams_by_name_status_code(self,name="Optometrists"):
     response = ExamAPI.get_exam_by_name(name)

     if response.status_code == 200:
         print("Response:", response.json())
     else:
         print(f"Failed to fetch exams: {response.status_code}")

     assert response.status_code == 200


 def test_get_exam_by_name(self):

     example_exam_name = "Veterinarians"
     exam_details = ExamData.get_exam_details_by_name(example_exam_name)
     assert exam_details is not None, f"Failed to get details for exam: {example_exam_name}"
     assert exam_details['name'] == example_exam_name, f"Exam details do not match for: {example_exam_name}"

 def test_get_professions_status_code(self):
     response = ExamAPI.get_professions()

     example_exam_name = "Optometrists"
     exam_details = ExamData.get_exam_details_by_name(example_exam_name)
     assert exam_details is not None, f"Failed to get details for exam: {example_exam_name}"
     assert 'name' == example_exam_name, f"Exam details do not match for: {example_exam_name}"

 def test_get_professions_status_code(self):
     response = ExamAPI.get_professions()
     if response.status_code == 200:
         print("Response:", response.json())  # Prints the JSON response
     else:
         print(f"Failed to fetch exams: {response.status_code}")

     assert response.status_code == 200

 def test_get_professions_content(self):
     profession_list = ExamData.get_profession_list()
     assert profession_list is not None, "Failed to get profession list"
     assert (profession_list, list), "Professions should be a list"
     assert len(profession_list) > 0, "Profession list is empty"



 def test_get_upcoming_exam_status_code(self):
     response = ExamAPI.get_upcoming_exam()

     if response.status_code == 200:
         print("Response:", response.json())  # Prints the JSON response
     else:
         print(f"Failed to fetch exams: {response.status_code}")

     assert response.status_code == 200, "Failed to fetch the upcoming exam data with status code 200."

 def test_get_upcoming_exam_content(self):
     upcoming_exam_info = ExamData.get_upcoming_exam_info()
     assert upcoming_exam_info is not None, "Failed to retrieve upcoming exam info."
     assert 'name' in upcoming_exam_info, "Upcoming exam info does not contain 'name'."
     assert 'dates' in upcoming_exam_info, "Upcoming exam info does not contain 'date'."

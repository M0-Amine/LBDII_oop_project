from typing import Union

Subject = type("Subject")
subject_id: int
student_id: int
assessment_type: str

class Attendance:
    total_minutes: int
    late_minutes: int
    day: int
    status: str
    
    def get_attendance_status() -> str:
        """ Converts late minutes to status and returns it """
    
class Assessment:
    assessment_type: str
    grade: int
    id: int
    weight: float
    
class Student:
    name: str
    gender: str
    id: int
    group: str
    subjects: list[Subject]
    attendance: dict[subject_id: int, list[Attendance]]
    assessments: dict[subject_id: int, list[Assessment]]
    
    def add_subject(subject: Subject) -> None:
        """ Internal to Subject Class. Adds Subject objects to subjects list """
    
class Subject:
    id: int
    name: str
    weights: dict[assessment_type: str, float]
    participants: list[Student]
    
    def add_student(student: Student) -> None:
        """ Adds Student object to participants list AND calls add_subject """
        
    def add_attendance(total_minutes: int, late_minutes: list[int]) -> None:
        """ Adds an Attendance object to each student in participants list """
        
    def add_assessment(assessment_type: str, grades: list[int]) -> None:
        """ Adds an Assessment object to each student in participants list """
    
    def change_weights(assessment_type: str, new_weight: int) -> None:
        """ Change the weight of the given assessment type """
    
    def modify_assessement_by_id(student: Union[Student, student_id: int], assessment_id: int, new_grade: int) -> None:
        """ Modifies the assessment's grade of a student given the student's id\student object and the assessment's id """
        
    def remove_assessment(assessment_id: int) -> None:
        """ Removes the specified assessment from the assessments dict of every student """
    
    def modify_attendance_by_id(student: Union[Student, student_id: int], attendance_id: int, new_late_minutes: int) -> None:
        """ Modifies the attendance of student """
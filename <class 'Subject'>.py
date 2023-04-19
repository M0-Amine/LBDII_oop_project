from typing import Union

Subject = type("Subject")
subject_id: int
student_id: int
assessment_type: str

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dic_delay = {range(0, 1): "Present", range(1, 6): "Late", range(6, 180): "Absent"}
assessment_types = ["TD", "TP", "Quizz", "Exam"]
genders = ["Male", "Female"]
groups = ["A", "B", "C", "D"]

class Attendance:
    
    def __init__(self, total_mintes: int, late_minutes: int, day: str) -> None:
        self.total_minutes = total_mintes
        self.late_minutes = late_minutes
        self.day = day
        self.status = self.get_attendance_status()
    
    def get_attendance_status(self) -> str:
        """ Converts late minutes to status and returns it """
        for range in dic_delay:
            if self.late_minutes in range:
                return dic_delay[range]
    
    # Getters and Setters:
    def get_total_minutes(self):
        return self.total_minutes

    def get_late_minutes(self):
        return self.late_minutes
    
    def get_day(self):
        return self.day
    
    def get_status(self):
        return self.status
    
    def set_total_minutes(self, totalmin: int):
        self.total_minutes = totalmin
        
        if totalmin < 0:
            raise ValueError("number of minutes cannot be negative")
            
    def set_late_minutes(self, latemin: int):
        self.late_minutes = latemin
        
        if latemin < 0:
            raise ValueError("number of minutes cannot be negative")
        
        if latemin > self.total_minutes:
            raise ValueError("late minutes should be less than or equal to the total minutes")
        
    def set_day(self, day: str):
        self.day = day
        
        if not day in days_of_week:
            raise ValueError("invalid day name")


class Assessment:
    
    def __init__(self, id: int, assesment_type: str, grade: int, weight: float) -> None:
        self.assessment_type = assesment_type
        self.grade = grade
        self.id = id
        self.weight = weight
        
    # Getters and setters:
    def get_type(self):
        return self.type
    
    def get_grade(self):
        return self.grade
    
    def set_type(self, type: str):
        
        if not type in assessment_types:
            raise ValueError("invalid assessment type")
        
        self.type = type
        
    def set_grade(self, grade: int):
        if not grade in range(0, 20):
            raise ValueError("invalid grade value, grade should be between 0 and 20")
        
        self.grade = grade
        
    def get_id(self):
        return self.id
    
    
class Student:
    
    def __init__(self, id: int, name: str, gender: str, group: str) -> None:
        self.name = name
        self.gender = gender
        self.id = id
        self.group = group
        self.subjects: list[Subject]
        self.attendances: dict[subject_id: int, list[Attendance]]
        self.assessments: dict[subject_id: int, list[Assessment]]
    
    def add_subject(self, subject: Subject) -> None:
        """ Internal to Subject Class. Adds Subject objects to subjects list """
        if not subject in self.subjects:
            self.subjects.append(subject)
            
    
    # Getters and Setters
    def get_name(self):
        return self.name
        
    def get_gender(self):
        return self.gender
        
    def get_group(self):
        return self.group
    
    def set_name(self, newName: str):
        if newName == "":
            raise ValueError("Invalid Name. Name cannot be empty.")
        self.name = newName
    
    def set_gender(self, newGend: str):
        if not newGend in genders:
            raise ValueError("Invalid gender. Gender must be either 'Female' or 'Male'.")        
        self.gender = newGend
        
    def set_group(self, newGroup):
        
        if not newGroup in groups:
            raise ValueError(f"Invalid group. Group must be one of {groups}.")       
        self.group = newGroup
        
    def get_attendance_day(self, subject_name, day):
        
        if not day in days_of_week:
            print(f"{self.name}'s {subject_name} attendance on {day}:\nNo attendance record found for {self.name} in {subject_name} on {day}.")
        
        elif not subject_name in self.subject_grades:
            print(f"subject {subject_name} not found for {self.name}.")
        
        else:
            for att in self.attendance[subject_name]:
                if att.get_day() == day:
                    print(f"{self.name}'s {subject_name} attendance for {day}:\n   - Total minutes: {att.get_total_minutes()}\n   - Late minutes: {att.get_late_minutes()}\n   - Attendance status: {att.get_attendance_status()}")
      
      
    # Display Info
    def print_info(self):
        print(f"Name: {self.name}\nGender: {self.gender}\nGroup: {self.group}")
        print("\nGrades:")
        for subject, assessments in self.subject_grades.items():
            print(f"{subject}:")
            for assessment_type in assessment_types:
                grades = [a.grade for a in assessments if a.type == assessment_type]
                if grades : print(f"    {assessment_type}: {grades}")
        
        print("\nAttendance:")
        for subject, records in self.attendance.items():
            print(f"{subject} Attendance:")
            for attendance in sorted(self.attendance[subject], key=lambda att: days_of_week.index(att.day)):
                print(f"  - {attendance.day}: {attendance.total_minutes} minutes (Late: {attendance.late_minutes} minutes)")
          
    
    
class Subject:
    
    def __init__(self, id: int, name: str) -> None:    
        self.id = id
        self.name = name
        self.weights: dict[assessment_type: str, float]
        self.participants: list[Student]
    
    def add_student(self, student: Student) -> None:  # this is an observer hh
        """ Adds Student object to participants list AND calls add_subject """
        if not student in self.participants:
            self.participants.append(student)
        if not self in student.subjects:
            student.subjects.append(self)
        
    def add_attendance(self, total_minutes: int, late_minutes: list[int], day: str) -> None:
        """ Adds an Attendance object to each student in participants list """
        for student, late_minute in enumerate(self.participants, late_minutes):
            student.attendances[self.id].append(Attendance(total_minutes, late_minute, day))
        
    def add_assessment(self, assessment_type: str, grades: list[int]) -> None:
        """ Adds an Assessment object to each student in participants list """
        for student, grade in enumerate(self.participants, grades):
            student.assessments[self.id].append(Assessment(assessment_type, grade))
    
    def change_weights(self, assessment_type: str, new_weight: int) -> None:
        """ Change the weight of the given assessment type """
        self.weights[assessment_type] = new_weight
    
    def modify_assessement_by_id(self, studentObj_or_id: Union[Student, int], assessment_id: int, new_grade: int) -> None:
        """ Modifies the assessment's grade of a student given the student's id\student object and the assessment's id """
        if type(studentObj_or_id) == Student:
            for assessment in studentObj_or_id.assessments[self.id]:
                if assessment.get_id() == assessment_id:
                    assessment.set_grade(new_grade)
                    
        elif type(studentObj_or_id) == int:
            for student in self.participants:
                if student.id == studentObj_or_id:
                    for assessment in student.assessments[self.id]:
                        if assessment.get_id() == assessment_id:
                            assessment.set_grade(new_grade)
        
    def remove_assessment(self, assessment_id: int) -> None:
        """ Removes the specified assessment from the assessments dict of every student """
        for student in self.participants:
            for assessment in student.assessments[self.id]:
                if assessment.id == assessment_id:
                    student.assessments[self.id].remove(assessment)
    
    def modify_attendance_by_id(self, studentObj_or_id: Union[Student, int], attendance_id: int, new_late_minutes: int) -> None:
        """ Modifies the attendance of student """
        if type(studentObj_or_id) == Student:
            for attendance in studentObj_or_id.attendances[self.id]:
                if attendance.id == attendance_id:
                    attendance.set_late_minutes(new_late_minutes)
                    
        elif type(studentObj_or_id) == int:
            for student in self.participants:
                if student.id == studentObj_or_id:
                    for attendance in student.attendances[self.id]:
                        if attendance.id == attendance_id:
                            attendance.set_late_minutes(new_late_minutes)
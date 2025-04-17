class Maven:
    def __init__(self,courseName:str,instructor:str):
        self.courseName=courseName
        self.instructor=instructor
        self.students=[]
        self.studentsWhoCompletedCourse=[]
        print(f"{courseName} instance created successfully!")
        
    def enroll_student(self,studentName:str):
        self.students.append(studentName)
        print(f"{studentName} added to list of students enrolled!")
        
    def get_students_number(self):
        
         while True:
            choice =  input(f"They are currently {len(self.students)} students enrolled in {self.courseName} course. Do you want to list them (y/n)?")
            
            
            if choice=="y":
                print(f"==Students==")
                for student in self.students:
                   
                    print()
                    print(student)
                    print()
                break
            elif choice == "n":
                print("Method exiting...")
                break
            else:
                print("Invalid key pressed!")
                
    def get_course_details(self):
        print("==Course Name==\n")
        print(self.courseName)
        print("\n ==Instructor==\n")
        print(self.instructor)
        print("\n == Students enrolled ==\n")
        if len(self.students)<1:
            print("No students enrolled")
        else:
            for student in self.students:
                print(f"{student}")
    def completed_course(self,studentName):
        if studentName in self.students:
            self.students.remove(studentName)
            self.studentsWhoCompletedCourse.append(studentName)
            print(f"{studentName} removed from enrolled list!")
        else:
            print(f"{studentName} not found in enrolled student list.")
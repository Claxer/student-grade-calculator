student_records = []


def get_grade(subject):
    while True:
        try:
            grade = float(input("Enter " + subject + " grade: "))

            if grade >= 0 and grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def get_attendance():
    while True:
        try:
            attendance = float(input("\nEnter attendance percentage: "))

            if attendance >= 0 and attendance <= 100:
                return attendance
            else:
                print("Attendance must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def get_letter_grade(average):
    if average >= 97:
        return "A+", "Outstanding!"

    elif average >= 93:
        return "A", "Excellent!"

    elif average >= 90:
        return "A-", "Excellent!"

    elif average >= 87:
        return "B+", "Very Good!"

    elif average >= 83:
        return "B", "Very Good!"

    elif average >= 80:
        return "B-", "Good!"

    elif average >= 77:
        return "C+", "Passed!"

    elif average >= 75:
        return "C", "Passed!"

    else:
        return "F", "Failed"


def get_performance_level(average):
    if average >= 95:
        return "Outstanding"

    elif average >= 90:
        return "Excellent"

    elif average >= 85:
        return "Very Good"

    elif average >= 80:
        return "Good"

    elif average >= 75:
        return "Satisfactory"

    else:
        return "Needs Improvement"


def get_gpa(average):
    if average >= 97:
        return 1.00

    elif average >= 93:
        return 1.25

    elif average >= 90:
        return 1.50

    elif average >= 87:
        return 1.75

    elif average >= 83:
        return 2.00

    elif average >= 80:
        return 2.25

    elif average >= 77:
        return 2.50

    elif average >= 75:
        return 3.00

    else:
        return 5.00


def get_attendance_status(attendance):
    if attendance >= 90:
        return "Excellent"

    elif attendance >= 80:
        return "Good"

    elif attendance >= 75:
        return "Satisfactory"

    else:
        return "Poor"


def display_subject_grades(subjects, grades):
    print("\n==============================")
    print("SUBJECT GRADES")
    print("==============================")

    for i in range(len(subjects)):
        print(subjects[i] + ":", grades[i])


def display_subject_performance(subjects, grades):
    print("\n==============================")
    print("SUBJECT PERFORMANCE")
    print("==============================")

    passed_subjects = 0
    failed_subjects = 0

    for i in range(len(subjects)):
        if grades[i] >= 75:
            print(subjects[i] + ":", grades[i], "- Passed")
            passed_subjects += 1
        else:
            print(subjects[i] + ":", grades[i], "- Failed")
            failed_subjects += 1

    print("\nPassed Subjects:", passed_subjects)
    print("Failed Subjects:", failed_subjects)

    return passed_subjects, failed_subjects


def display_grade_analysis(subjects, grades):
    print("\n==============================")
    print("GRADE ANALYSIS")
    print("==============================")

    highest_grade = max(grades)
    lowest_grade = min(grades)

    highest_subject = subjects[grades.index(highest_grade)]
    lowest_subject = subjects[grades.index(lowest_grade)]

    print("Highest Grade:", highest_grade)
    print("Highest Subject:", highest_subject)
    print("Lowest Grade:", lowest_grade)
    print("Lowest Subject:", lowest_subject)

    return highest_grade, lowest_grade, highest_subject, lowest_subject


def display_grade_summary(subjects, grades):
    print("\n==============================")
    print("GRADE SUMMARY")
    print("==============================")

    excellent_count = 0
    very_good_count = 0
    good_count = 0
    passed_count = 0
    failed_count = 0

    for i in range(len(subjects)):
        if grades[i] >= 90:
            level = "Excellent"
            excellent_count += 1

        elif grades[i] >= 85:
            level = "Very Good"
            very_good_count += 1

        elif grades[i] >= 80:
            level = "Good"
            good_count += 1

        elif grades[i] >= 75:
            level = "Passed"
            passed_count += 1

        else:
            level = "Failed"
            failed_count += 1

        print(subjects[i] + ":", grades[i], "-", level)

    print("\nGrade Distribution:")
    print("Excellent:", excellent_count)
    print("Very Good:", very_good_count)
    print("Good:", good_count)
    print("Passed:", passed_count)
    print("Failed:", failed_count)


def display_recognition(average):
    print("\n==============================")
    print("RECOGNITION")
    print("==============================")

    if average >= 95:
        print("Recognition: With High Honors")

    elif average >= 90:
        print("Recognition: With Honors")

    elif average >= 85:
        print("Recognition: Good Academic Performance")

    elif average >= 75:
        print("Recognition: Passed")

    else:
        print("Recognition: Needs Improvement")


def display_scholarship(average, attendance, failed_subjects):
    print("\n==============================")
    print("SCHOLARSHIP CHECK")
    print("==============================")

    if average >= 90 and attendance >= 90 and failed_subjects == 0:
        print("Scholarship Eligibility: Eligible")
        return True

    else:
        print("Scholarship Eligibility: Not Eligible")
        return False


def display_overall_status(average, failed_subjects):
    print("\n==============================")
    print("OVERALL STATUS")
    print("==============================")

    if failed_subjects == 0 and average >= 75:
        print("Overall Status: PASSED")
        print("All subjects passed.")
        return "PASSED"

    elif failed_subjects > 0:
        print("Overall Status: FAILED")
        print("Warning: Student has failed subject(s).")
        return "FAILED"

    else:
        print("Overall Status: FAILED")
        print("Warning: Overall average is below passing.")
        return "FAILED"


# NEW FEATURE
def display_gpa(average):
    print("\n==============================")
    print("GPA EQUIVALENT")
    print("==============================")

    gpa = get_gpa(average)

    print("Estimated GPA:", gpa)

    if gpa <= 1.50:
        print("GPA Description: Excellent Academic Performance")

    elif gpa <= 2.25:
        print("GPA Description: Good Academic Performance")

    elif gpa <= 3.00:
        print("GPA Description: Passing")

    else:
        print("GPA Description: Needs Improvement")

    return gpa


# NEW FEATURE
def display_academic_standing(average, failed_subjects, attendance):
    print("\n==============================")
    print("ACADEMIC STANDING")
    print("==============================")

    if average >= 90 and failed_subjects == 0 and attendance >= 90:
        standing = "Excellent Standing"

    elif average >= 85 and failed_subjects == 0:
        standing = "Good Standing"

    elif average >= 75 and failed_subjects == 0:
        standing = "Satisfactory Standing"

    else:
        standing = "Academic Improvement Needed"

    print("Academic Standing:", standing)

    return standing


# NEW FEATURE
def display_attendance(attendance):
    print("\n==============================")
    print("ATTENDANCE")
    print("==============================")

    status = get_attendance_status(attendance)

    print("Attendance:", attendance, "%")
    print("Attendance Status:", status)

    if attendance < 75:
        print("Warning: Attendance is below the passing requirement.")

    elif attendance < 80:
        print("Warning: Attendance needs improvement.")

    else:
        print("Attendance requirement is satisfactory.")


# NEW FEATURE
def display_recommendations(subjects, grades, average, attendance):
    print("\n==============================")
    print("STUDY RECOMMENDATIONS")
    print("==============================")

    recommendations = []

    for i in range(len(subjects)):
        if grades[i] < 75:
            recommendations.append(
                "Focus on " + subjects[i] + " because it is currently failing."
            )

        elif grades[i] < 80:
            recommendations.append(
                "Spend more study time on " + subjects[i] + "."
            )

    if attendance < 80:
        recommendations.append(
            "Improve attendance to avoid missing lessons and activities."
        )

    if average < 75:
        recommendations.append(
            "Create a regular study schedule to improve the overall average."
        )

    elif average < 85:
        recommendations.append(
            "Continue studying consistently to raise the overall average."
        )

    else:
        recommendations.append(
            "Maintain your current study habits and performance."
        )

    for recommendation in recommendations:
        print("-", recommendation)


# NEW FEATURE
def display_subject_improvement(subjects, grades):
    print("\n==============================")
    print("SUBJECT IMPROVEMENT NEEDED")
    print("==============================")

    found = False

    for i in range(len(subjects)):
        if grades[i] < 75:
            points_needed = 75 - grades[i]

            print(
                subjects[i],
                "needs",
                round(points_needed, 2),
                "more points to reach the passing grade."
            )

            found = True

    if found == False:
        print("No subject needs improvement to reach the passing grade.")


# NEW FEATURE
def save_student_record(name, student_id, average, letter_grade,
                        attendance, failed_subjects, gpa):
    record = {
        "name": name,
        "student_id": student_id,
        "average": average,
        "letter_grade": letter_grade,
        "attendance": attendance,
        "failed_subjects": failed_subjects,
        "gpa": gpa
    }

    student_records.append(record)


# NEW FEATURE
def view_student_records():
    print("\n==============================")
    print("SAVED STUDENT RECORDS")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    for i in range(len(student_records)):
        record = student_records[i]

        print("\nStudent Record #", i + 1)
        print("Name:", record["name"])
        print("Student ID:", record["student_id"])
        print("Average:", round(record["average"], 2))
        print("Letter Grade:", record["letter_grade"])
        print("Attendance:", record["attendance"], "%")
        print("Failed Subjects:", record["failed_subjects"])
        print("GPA:", record["gpa"])


# NEW FEATURE
def search_student():
    print("\n==============================")
    print("SEARCH STUDENT")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    search = input("Enter student name or ID: ").lower()

    found = False

    for record in student_records:
        if search in record["name"].lower() or search in record["student_id"].lower():
            print("\nStudent Found")
            print("------------------------------")
            print("Name:", record["name"])
            print("Student ID:", record["student_id"])
            print("Average:", round(record["average"], 2))
            print("Letter Grade:", record["letter_grade"])
            print("Attendance:", record["attendance"], "%")
            print("Failed Subjects:", record["failed_subjects"])
            print("GPA:", record["gpa"])

            found = True

    if found == False:
        print("Student record not found.")


# NEW FEATURE
def display_class_summary():
    print("\n==============================")
    print("CLASS SUMMARY")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    total_average = 0
    highest_average = student_records[0]["average"]
    lowest_average = student_records[0]["average"]

    highest_student = student_records[0]["name"]
    lowest_student = student_records[0]["name"]

    passed_students = 0
    failed_students = 0

    for record in student_records:
        total_average += record["average"]

        if record["average"] > highest_average:
            highest_average = record["average"]
            highest_student = record["name"]

        if record["average"] < lowest_average:
            lowest_average = record["average"]
            lowest_student = record["name"]

        if record["average"] >= 75 and record["failed_subjects"] == 0:
            passed_students += 1
        else:
            failed_students += 1

    class_average = total_average / len(student_records)

    print("Number of Students:", len(student_records))
    print("Class Average:", round(class_average, 2))
    print("Highest Student Average:", round(highest_average, 2))
    print("Highest Student:", highest_student)
    print("Lowest Student Average:", round(lowest_average, 2))
    print("Lowest Student:", lowest_student)
    print("Students Passed:", passed_students)
    print("Students Failed:", failed_students)


def calculate_student():
    print("\n== Student Grade Calculator ==")

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    subjects = [
        "Math",
        "English",
        "Science",
        "Filipino",
        "Computer",
        "Programming",
        "Database"
    ]

    grades = []

    print("\nEnter grades from 0 to 100.")

    for subject in subjects:
        grade = get_grade(subject)
        grades.append(grade)

    attendance = get_attendance()

    average = sum(grades) / len(grades)

    print("\n==============================")
    print("STUDENT INFORMATION")
    print("==============================")
    print("Student:", name)
    print("Student ID:", student_id)

    display_subject_grades(subjects, grades)

    print("\nAverage:", round(average, 2))
    print("Grade Percentage:", round(average, 2), "%")

    print("\n==============================")
    print("FINAL GRADE")
    print("==============================")

    letter_grade, remarks = get_letter_grade(average)

    print("Letter Grade:", letter_grade)
    print("Remarks:", remarks)

    passed_subjects, failed_subjects = display_subject_performance(
        subjects, grades
    )

    display_grade_analysis(subjects, grades)

    print("\n==============================")
    print("PERFORMANCE LEVEL")
    print("==============================")

    performance = get_performance_level(average)

    print("Performance Level:", performance)

    display_recognition(average)

    display_attendance(attendance)

    display_scholarship(
        average,
        attendance,
        failed_subjects
    )

    overall_status = display_overall_status(
        average,
        failed_subjects
    )

    display_grade_summary(subjects, grades)

    # NEW FEATURES
    gpa = display_gpa(average)

    academic_standing = display_academic_standing(
        average,
        failed_subjects,
        attendance
    )

    display_subject_improvement(
        subjects,
        grades
    )

    display_recommendations(
        subjects,
        grades,
        average,
        attendance
    )

    save_student_record(
        name,
        student_id,
        average,
        letter_grade,
        attendance,
        failed_subjects,
        gpa
    )

    print("\n==============================")
    print("CALCULATION COMPLETE")
    print("==============================")


def main():
    while True:
        print("\n===================================")
        print("     STUDENT GRADE CALCULATOR")
        print("===================================")
        print("1. Calculate Student Grade")
        print("2. View Student Records")
        print("3. Search Student")
        print("4. View Class Summary")
        print("5. Exit")
        print("===================================")

        choice = input("Choose an option: ")

        if choice == "1":
            calculate_student()

        elif choice == "2":
            view_student_records()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_class_summary()

        elif choice == "5":
            print("\nProgram Ended.")
            break

        else:
            print("\nInvalid choice. Please choose 1 to 5.")


main()

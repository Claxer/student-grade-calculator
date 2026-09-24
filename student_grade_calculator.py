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


def save_student_record(name, student_id, subjects, grades, average,
                        letter_grade, attendance, failed_subjects, gpa,
                        performance, standing):

    record = {
        "name": name,
        "student_id": student_id,
        "subjects": subjects,
        "grades": grades,
        "average": average,
        "letter_grade": letter_grade,
        "attendance": attendance,
        "failed_subjects": failed_subjects,
        "gpa": gpa,
        "performance": performance,
        "standing": standing
    }

    student_records.append(record)


def student_id_exists(student_id):
    for record in student_records:
        if record["student_id"].lower() == student_id.lower():
            return True

    return False


def get_unique_student_id():
    while True:
        student_id = input("Enter student ID: ").strip()

        if student_id == "":
            print("Student ID cannot be empty.")
        elif student_id_exists(student_id):
            print("That student ID already exists.")
        else:
            return student_id


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
        print("Performance:", record["performance"])
        print("Academic Standing:", record["standing"])


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
            print("Performance:", record["performance"])
            print("Academic Standing:", record["standing"])

            found = True

    if found == False:
        print("Student record not found.")


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
    pass_rate = (passed_students / len(student_records)) * 100

    print("Number of Students:", len(student_records))
    print("Class Average:", round(class_average, 2))
    print("Highest Student Average:", round(highest_average, 2))
    print("Highest Student:", highest_student)
    print("Lowest Student Average:", round(lowest_average, 2))
    print("Lowest Student:", lowest_student)
    print("Students Passed:", passed_students)
    print("Students Failed:", failed_students)
    print("Class Pass Rate:", round(pass_rate, 2), "%")


def view_student_details():
    print("\n==============================")
    print("DETAILED STUDENT REPORT")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    search = input("Enter student name or ID: ").lower()

    found = False

    for record in student_records:
        if search in record["name"].lower() or search in record["student_id"].lower():
            print("\n===================================")
            print("STUDENT REPORT")
            print("===================================")

            print("Name:", record["name"])
            print("Student ID:", record["student_id"])

            print("\nSUBJECTS")

            subjects = record["subjects"]
            grades = record["grades"]

            for i in range(len(subjects)):
                print(subjects[i], ":", grades[i])

            print("\nACADEMIC INFORMATION")
            print("Average:", round(record["average"], 2))
            print("Letter Grade:", record["letter_grade"])
            print("GPA:", record["gpa"])
            print("Performance:", record["performance"])
            print("Academic Standing:", record["standing"])

            print("\nATTENDANCE")
            print("Attendance:", record["attendance"], "%")
            print(
                "Attendance Status:",
                get_attendance_status(record["attendance"])
            )

            print("\nFAILED SUBJECTS:", record["failed_subjects"])

            found = True

    if found == False:
        print("Student record not found.")


def find_student():
    if len(student_records) == 0:
        print("No student records available.")
        return None

    search = input("Enter student name or ID: ").lower()

    for record in student_records:
        if search == record["name"].lower() or search == record["student_id"].lower():
            return record

    print("Student record not found.")
    return None


def edit_student_record():
    print("\n==============================")
    print("EDIT STUDENT RECORD")
    print("==============================")

    record = find_student()

    if record is None:
        return

    print("\nStudent Found")
    print("Name:", record["name"])
    print("Student ID:", record["student_id"])

    print("\nWhat would you like to edit?")
    print("1. Student Name")
    print("2. Student ID")
    print("3. Grades")
    print("4. Attendance")
    print("5. Cancel")

    choice = input("Choose an option: ")

    if choice == "1":
        new_name = input("Enter new name: ").strip()

        if new_name != "":
            record["name"] = new_name
            print("Student name updated.")
        else:
            print("Name cannot be empty.")

    elif choice == "2":
        new_id = input("Enter new student ID: ").strip()

        if new_id == "":
            print("Student ID cannot be empty.")
        elif new_id.lower() == record["student_id"].lower():
            print("Student ID unchanged.")
        elif student_id_exists(new_id):
            print("That student ID already exists.")
        else:
            record["student_id"] = new_id
            print("Student ID updated.")

    elif choice == "3":
        print("\nEnter new grades.")

        for i in range(len(record["subjects"])):
            record["grades"][i] = get_grade(record["subjects"][i])

        update_student_calculation(record)

        print("Grades updated.")

    elif choice == "4":
        record["attendance"] = get_attendance()

        update_student_calculation(record)

        print("Attendance updated.")

    elif choice == "5":
        print("Edit cancelled.")

    else:
        print("Invalid option.")


def update_student_calculation(record):
    grades = record["grades"]

    average = sum(grades) / len(grades)

    letter_grade, remarks = get_letter_grade(average)

    failed_subjects = 0

    for grade in grades:
        if grade < 75:
            failed_subjects += 1

    gpa = get_gpa(average)
    performance = get_performance_level(average)
    attendance = record["attendance"]

    if average >= 90 and failed_subjects == 0 and attendance >= 90:
        standing = "Excellent Standing"
    elif average >= 85 and failed_subjects == 0:
        standing = "Good Standing"
    elif average >= 75 and failed_subjects == 0:
        standing = "Satisfactory Standing"
    else:
        standing = "Academic Improvement Needed"

    record["average"] = average
    record["letter_grade"] = letter_grade
    record["failed_subjects"] = failed_subjects
    record["gpa"] = gpa
    record["performance"] = performance
    record["standing"] = standing


def delete_student_record():
    print("\n==============================")
    print("DELETE STUDENT RECORD")
    print("==============================")

    record = find_student()

    if record is None:
        return

    print("\nStudent Found")
    print("Name:", record["name"])
    print("Student ID:", record["student_id"])

    confirm = input(
        "Are you sure you want to delete this record? (yes/no): "
    ).lower()

    if confirm == "yes":
        student_records.remove(record)
        print("Student record deleted.")
    else:
        print("Delete cancelled.")


def rank_students():
    print("\n==============================")
    print("STUDENT RANKING")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    ranked_students = sorted(
        student_records,
        key=lambda record: record["average"],
        reverse=True
    )

    rank = 1

    for record in ranked_students:
        print(
            rank,
            ".",
            record["name"],
            "- Average:",
            round(record["average"], 2),
            "- GPA:",
            record["gpa"]
        )

        rank += 1


def display_honor_students():
    print("\n==============================")
    print("HONOR STUDENTS")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    found = False

    for record in student_records:
        if record["average"] >= 90 and record["failed_subjects"] == 0:
            print(
                record["name"],
                "- Average:",
                round(record["average"], 2),
                "- With Honors"
            )

            found = True

    if found == False:
        print("No students currently qualify for honors.")


def display_students_needing_improvement():
    print("\n==============================")
    print("STUDENTS NEEDING IMPROVEMENT")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    found = False

    for record in student_records:
        if record["average"] < 75 or record["failed_subjects"] > 0:
            print(
                record["name"],
                "- Average:",
                round(record["average"], 2),
                "- Failed Subjects:",
                record["failed_subjects"]
            )

            found = True

    if found == False:
        print("No students currently need academic improvement.")


def display_subject_statistics():
    print("\n==============================")
    print("SUBJECT STATISTICS")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    subjects = student_records[0]["subjects"]

    for i in range(len(subjects)):
        total = 0
        highest = 0
        lowest = 100
        passed = 0
        failed = 0

        for record in student_records:
            grade = record["grades"][i]

            total += grade

            if grade > highest:
                highest = grade

            if grade < lowest:
                lowest = grade

            if grade >= 75:
                passed += 1
            else:
                failed += 1

        subject_average = total / len(student_records)
        pass_percentage = (passed / len(student_records)) * 100

        print("\nSubject:", subjects[i])
        print("Average:", round(subject_average, 2))
        print("Highest Grade:", highest)
        print("Lowest Grade:", lowest)
        print("Passed:", passed)
        print("Failed:", failed)
        print("Pass Percentage:", round(pass_percentage, 2), "%")


def display_class_performance():
    print("\n==============================")
    print("CLASS PERFORMANCE")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    excellent = 0
    good = 0
    satisfactory = 0
    needs_improvement = 0

    for record in student_records:
        average = record["average"]

        if average >= 90:
            excellent += 1
        elif average >= 80:
            good += 1
        elif average >= 75:
            satisfactory += 1
        else:
            needs_improvement += 1

    print("Excellent:", excellent)
    print("Good:", good)
    print("Satisfactory:", satisfactory)
    print("Needs Improvement:", needs_improvement)


def clear_all_records():
    print("\n==============================")
    print("CLEAR ALL RECORDS")
    print("==============================")

    if len(student_records) == 0:
        print("There are no records to delete.")
        return

    print("Number of records:", len(student_records))

    confirm = input(
        "Are you sure you want to delete ALL records? (yes/no): "
    ).lower()

    if confirm == "yes":
        student_records.clear()
        print("All student records have been deleted.")
    else:
        print("Operation cancelled.")


# NEW FEATURE
def display_scholarship_students():
    print("\n==============================")
    print("SCHOLARSHIP STUDENTS")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    found = False

    for record in student_records:
        if (
            record["average"] >= 90
            and record["attendance"] >= 90
            and record["failed_subjects"] == 0
        ):
            print(
                record["name"],
                "- Average:",
                round(record["average"], 2),
                "- Attendance:",
                record["attendance"], "%"
            )

            found = True

    if found == False:
        print("No students are currently scholarship eligible.")


# NEW FEATURE
def display_failed_subject_report():
    print("\n==============================")
    print("FAILED SUBJECT REPORT")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    found = False

    for record in student_records:
        failed = False

        for i in range(len(record["subjects"])):
            if record["grades"][i] < 75:
                if failed == False:
                    print("\nStudent:", record["name"])
                    print("Student ID:", record["student_id"])
                    failed = True
                    found = True

                print(
                    record["subjects"][i],
                    ":",
                    record["grades"][i]
                )

    if found == False:
        print("No failed subjects found.")


# NEW FEATURE
def display_attendance_report():
    print("\n==============================")
    print("ATTENDANCE REPORT")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    for record in student_records:
        print(
            record["name"],
            "- Attendance:",
            record["attendance"],
            "%",
            "-",
            get_attendance_status(record["attendance"])
        )


# NEW FEATURE
def display_grade_distribution():
    print("\n==============================")
    print("CLASS GRADE DISTRIBUTION")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    grade_distribution = {
        "A+": 0,
        "A": 0,
        "A-": 0,
        "B+": 0,
        "B": 0,
        "B-": 0,
        "C+": 0,
        "C": 0,
        "F": 0
    }

    for record in student_records:
        letter_grade = record["letter_grade"]

        if letter_grade in grade_distribution:
            grade_distribution[letter_grade] += 1

    for grade in grade_distribution:
        print(grade, ":", grade_distribution[grade], "student(s)")


# NEW FEATURE
def display_dashboard():
    print("\n===================================")
    print("        CLASS DASHBOARD")
    print("===================================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    total_students = len(student_records)
    total_average = 0
    passed = 0
    failed = 0
    honors = 0
    scholarship = 0
    improvement = 0

    for record in student_records:
        total_average += record["average"]

        if record["average"] >= 75 and record["failed_subjects"] == 0:
            passed += 1
        else:
            failed += 1

        if record["average"] >= 90 and record["failed_subjects"] == 0:
            honors += 1

        if (
            record["average"] >= 90
            and record["attendance"] >= 90
            and record["failed_subjects"] == 0
        ):
            scholarship += 1

        if record["average"] < 75 or record["failed_subjects"] > 0:
            improvement += 1

    class_average = total_average / total_students

    print("Total Students:", total_students)
    print("Class Average:", round(class_average, 2))
    print("Passed Students:", passed)
    print("Failed Students:", failed)
    print("Honor Students:", honors)
    print("Scholarship Eligible:", scholarship)
    print("Needs Improvement:", improvement)


# NEW FEATURE
def sort_students():
    print("\n==============================")
    print("SORT STUDENTS")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    print("1. Name")
    print("2. Student ID")
    print("3. Average - Highest to Lowest")
    print("4. Average - Lowest to Highest")
    print("5. GPA")
    print("6. Attendance")

    choice = input("Choose sorting option: ")

    if choice == "1":
        sorted_students = sorted(
            student_records,
            key=lambda record: record["name"].lower()
        )
    elif choice == "2":
        sorted_students = sorted(
            student_records,
            key=lambda record: record["student_id"].lower()
        )
    elif choice == "3":
        sorted_students = sorted(
            student_records,
            key=lambda record: record["average"],
            reverse=True
        )
    elif choice == "4":
        sorted_students = sorted(
            student_records,
            key=lambda record: record["average"]
        )
    elif choice == "5":
        sorted_students = sorted(
            student_records,
            key=lambda record: record["gpa"]
        )
    elif choice == "6":
        sorted_students = sorted(
            student_records,
            key=lambda record: record["attendance"],
            reverse=True
        )
    else:
        print("Invalid option.")
        return

    print("\nSORTED STUDENTS")

    for i in range(len(sorted_students)):
        record = sorted_students[i]

        print(
            i + 1,
            ".",
            record["name"],
            "- Average:",
            round(record["average"], 2),
            "- GPA:",
            record["gpa"],
            "- Attendance:",
            record["attendance"], "%"
        )


# NEW FEATURE
def filter_students():
    print("\n==============================")
    print("FILTER STUDENTS")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    print("1. Passed Students")
    print("2. Failed Students")
    print("3. Honor Students")
    print("4. Scholarship Eligible")
    print("5. Needs Improvement")

    choice = input("Choose filter: ")

    found = False

    for record in student_records:
        show = False

        if choice == "1":
            if record["average"] >= 75 and record["failed_subjects"] == 0:
                show = True

        elif choice == "2":
            if record["average"] < 75 or record["failed_subjects"] > 0:
                show = True

        elif choice == "3":
            if record["average"] >= 90 and record["failed_subjects"] == 0:
                show = True

        elif choice == "4":
            if (
                record["average"] >= 90
                and record["attendance"] >= 90
                and record["failed_subjects"] == 0
            ):
                show = True

        elif choice == "5":
            if record["average"] < 75 or record["failed_subjects"] > 0:
                show = True

        else:
            print("Invalid option.")
            return

        if show:
            print(
                "\nName:",
                record["name"],
                "\nStudent ID:",
                record["student_id"],
                "\nAverage:",
                round(record["average"], 2),
                "\nGPA:",
                record["gpa"]
            )

            found = True

    if found == False:
        print("\nNo students matched the selected filter.")


# NEW FEATURE
def compare_students():
    print("\n==============================")
    print("COMPARE TWO STUDENTS")
    print("==============================")

    if len(student_records) < 2:
        print("At least two student records are required.")
        return

    print("\nFirst Student")
    student1 = find_student()

    if student1 is None:
        return

    print("\nSecond Student")
    student2 = find_student()

    if student2 is None:
        return

    print("\n===================================")
    print("STUDENT COMPARISON")
    print("===================================")

    print("\nName")
    print(student1["name"], "vs", student2["name"])

    print("\nAverage")
    print(
        round(student1["average"], 2),
        "vs",
        round(student2["average"], 2)
    )

    print("\nGPA")
    print(student1["gpa"], "vs", student2["gpa"])

    print("\nAttendance")
    print(
        student1["attendance"],
        "%",
        "vs",
        student2["attendance"],
        "%"
    )

    print("\nFailed Subjects")
    print(
        student1["failed_subjects"],
        "vs",
        student2["failed_subjects"]
    )

    print("\nSUBJECT COMPARISON")

    for i in range(len(student1["subjects"])):
        print(
            student1["subjects"][i],
            ":",
            student1["grades"][i],
            "vs",
            student2["grades"][i]
        )


# NEW FEATURE
def improvement_calculator():
    print("\n==============================")
    print("IMPROVEMENT CALCULATOR")
    print("==============================")

    record = find_student()

    if record is None:
        return

    print("\nStudent:", record["name"])
    print("Current Average:", round(record["average"], 2))

    targets = [75, 80, 85, 90, 95]

    print("\nPoints needed for each target:")

    for target in targets:
        if record["average"] >= target:
            print(target, "- Target already reached.")
        else:
            needed = target - record["average"]
            print(target, "- Needs", round(needed, 2), "more points.")


# NEW FEATURE
def add_student_record():
    print("\n==============================")
    print("ADD STUDENT RECORD")
    print("==============================")

    name = input("Enter student name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    student_id = get_unique_student_id()

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
        grades.append(get_grade(subject))

    attendance = get_attendance()

    average = sum(grades) / len(grades)

    letter_grade, remarks = get_letter_grade(average)

    failed_subjects = 0

    for grade in grades:
        if grade < 75:
            failed_subjects += 1

    gpa = get_gpa(average)
    performance = get_performance_level(average)

    if average >= 90 and failed_subjects == 0 and attendance >= 90:
        standing = "Excellent Standing"
    elif average >= 85 and failed_subjects == 0:
        standing = "Good Standing"
    elif average >= 75 and failed_subjects == 0:
        standing = "Satisfactory Standing"
    else:
        standing = "Academic Improvement Needed"

    save_student_record(
        name,
        student_id,
        subjects,
        grades,
        average,
        letter_grade,
        attendance,
        failed_subjects,
        gpa,
        performance,
        standing
    )

    print("\nStudent record successfully added.")


# NEW FEATURE
def export_student_report():
    print("\n==============================")
    print("EXPORT STUDENT REPORT")
    print("==============================")

    record = find_student()

    if record is None:
        return

    filename = record["name"].replace(" ", "_") + "_Report.txt"

    try:
        with open(filename, "w") as file:
            file.write("STUDENT GRADE REPORT\n")
            file.write("==============================\n")
            file.write("Name: " + record["name"] + "\n")
            file.write("Student ID: " + record["student_id"] + "\n\n")

            file.write("SUBJECT GRADES\n")
            file.write("------------------------------\n")

            for i in range(len(record["subjects"])):
                file.write(
                    record["subjects"][i]
                    + ": "
                    + str(record["grades"][i])
                    + "\n"
                )

            file.write("\nACADEMIC INFORMATION\n")
            file.write("------------------------------\n")
            file.write("Average: " + str(round(record["average"], 2)) + "\n")
            file.write("Letter Grade: " + record["letter_grade"] + "\n")
            file.write("GPA: " + str(record["gpa"]) + "\n")
            file.write("Performance: " + record["performance"] + "\n")
            file.write("Academic Standing: " + record["standing"] + "\n")

            file.write("\nATTENDANCE\n")
            file.write("------------------------------\n")
            file.write("Attendance: " + str(record["attendance"]) + "%\n")
            file.write(
                "Attendance Status: "
                + get_attendance_status(record["attendance"])
                + "\n"
            )

            file.write(
                "\nFailed Subjects: "
                + str(record["failed_subjects"])
                + "\n"
            )

        print("Report successfully exported.")
        print("File:", filename)

    except Exception as error:
        print("Unable to export report.")
        print("Error:", error)


# NEW FEATURE
def export_class_report():
    print("\n==============================")
    print("EXPORT CLASS REPORT")
    print("==============================")

    if len(student_records) == 0:
        print("No student records available.")
        return

    filename = "Class_Report.txt"

    try:
        total_average = 0
        passed = 0
        failed = 0

        with open(filename, "w") as file:
            file.write("CLASS GRADE REPORT\n")
            file.write("==============================\n\n")

            file.write(
                "Total Students: "
                + str(len(student_records))
                + "\n\n"
            )

            for record in student_records:
                total_average += record["average"]

                if record["average"] >= 75 and record["failed_subjects"] == 0:
                    passed += 1
                else:
                    failed += 1

                file.write("Student: " + record["name"] + "\n")
                file.write("Student ID: " + record["student_id"] + "\n")
                file.write(
                    "Average: "
                    + str(round(record["average"], 2))
                    + "\n"
                )
                file.write(
                    "Letter Grade: "
                    + record["letter_grade"]
                    + "\n"
                )
                file.write("GPA: " + str(record["gpa"]) + "\n")
                file.write(
                    "Attendance: "
                    + str(record["attendance"])
                    + "%\n"
                )
                file.write(
                    "Academic Standing: "
                    + record["standing"]
                    + "\n"
                )
                file.write("------------------------------\n")

            class_average = total_average / len(student_records)
            pass_rate = (passed / len(student_records)) * 100

            file.write("\nCLASS SUMMARY\n")
            file.write("==============================\n")
            file.write(
                "Class Average: "
                + str(round(class_average, 2))
                + "\n"
            )
            file.write("Passed Students: " + str(passed) + "\n")
            file.write("Failed Students: " + str(failed) + "\n")
            file.write(
                "Class Pass Rate: "
                + str(round(pass_rate, 2))
                + "%\n"
            )

        print("Class report successfully exported.")
        print("File:", filename)

    except Exception as error:
        print("Unable to export class report.")
        print("Error:", error)


def calculate_student():
    print("\n== Student Grade Calculator ==")

    name = input("Enter student name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    student_id = get_unique_student_id()

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
        subjects,
        grades
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
        subjects,
        grades,
        average,
        letter_grade,
        attendance,
        failed_subjects,
        gpa,
        performance,
        academic_standing
    )

    print("\n==============================")
    print("CALCULATION COMPLETE")
    print("==============================")


def main():
    while True:
        print("\n===================================")
        print("   STUDENT GRADE MANAGEMENT SYSTEM")
        print("===================================")

        print("1.  Calculate Student Grade")
        print("2.  Add Student Record")
        print("3.  View Student Records")
        print("4.  Search Student")
        print("5.  View Class Dashboard")
        print("6.  View Class Summary")
        print("7.  View Detailed Student Report")
        print("8.  Edit Student Record")
        print("9.  Delete Student Record")
        print("10. Rank Students")
        print("11. View Honor Students")
        print("12. Students Needing Improvement")
        print("13. Scholarship Students")
        print("14. Subject Statistics")
        print("15. Failed Subject Report")
        print("16. Attendance Report")
        print("17. Grade Distribution")
        print("18. Class Performance")
        print("19. Compare Two Students")
        print("20. Sort Students")
        print("21. Filter Students")
        print("22. Improvement Calculator")
        print("23. Export Student Report")
        print("24. Export Class Report")
        print("25. Clear All Records")
        print("26. Exit")

        print("===================================")

        choice = input("Choose an option: ")

        if choice == "1":
            calculate_student()

        elif choice == "2":
            add_student_record()

        elif choice == "3":
            view_student_records()

        elif choice == "4":
            search_student()

        elif choice == "5":
            display_dashboard()

        elif choice == "6":
            display_class_summary()

        elif choice == "7":
            view_student_details()

        elif choice == "8":
            edit_student_record()

        elif choice == "9":
            delete_student_record()

        elif choice == "10":
            rank_students()

        elif choice == "11":
            display_honor_students()

        elif choice == "12":
            display_students_needing_improvement()

        elif choice == "13":
            display_scholarship_students()

        elif choice == "14":
            display_subject_statistics()

        elif choice == "15":
            display_failed_subject_report()

        elif choice == "16":
            display_attendance_report()

        elif choice == "17":
            display_grade_distribution()

        elif choice == "18":
            display_class_performance()

        elif choice == "19":
            compare_students()

        elif choice == "20":
            sort_students()

        elif choice == "21":
            filter_students()

        elif choice == "22":
            improvement_calculator()

        elif choice == "23":
            export_student_report()

        elif choice == "24":
            export_class_report()

        elif choice == "25":
            clear_all_records()

        elif choice == "26":
            print("\nProgram Ended.")
            break

        else:
            print("\nInvalid choice. Please choose 1 to 26.")


main()

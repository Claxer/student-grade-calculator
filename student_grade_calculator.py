while True:
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
        while True:
            try:
                grade = float(input("Enter " + subject + " grade: "))

                if grade >= 0 and grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")
    while True:
        try:
            attendance = float(input("\nEnter attendance percentage: "))

            if attendance >= 0 and attendance <= 100:
                break
            else:
                print("Attendance must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    average = sum(grades) / len(grades)

    print("\n==============================")
    print("STUDENT INFORMATION")
    print("==============================")
    print("Student:", name)
    print("Student ID:", student_id)

    print("\n==============================")
    print("SUBJECT GRADES")
    print("==============================")

    for i in range(len(subjects)):
        print(subjects[i] + ":", grades[i])

    print("\nAverage:", round(average, 2))
    print("Grade Percentage:", round(average, 2), "%")

    print("\n==============================")
    print("FINAL GRADE")
    print("==============================")

    if average >= 97:
        letter_grade = "A+"
        remarks = "Outstanding!"

    elif average >= 93:
        letter_grade = "A"
        remarks = "Excellent!"

    elif average >= 90:
        letter_grade = "A-"
        remarks = "Excellent!"

    elif average >= 87:
        letter_grade = "B+"
        remarks = "Very Good!"

    elif average >= 83:
        letter_grade = "B"
        remarks = "Very Good!"

    elif average >= 80:
        letter_grade = "B-"
        remarks = "Good!"

    elif average >= 77:
        letter_grade = "C+"
        remarks = "Passed!"

    elif average >= 75:
        letter_grade = "C"
        remarks = "Passed!"

    else:
        letter_grade = "F"
        remarks = "Failed"

    print("Letter Grade:", letter_grade)
    print("Remarks:", remarks)

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

    print("\n==============================")
    print("PERFORMANCE LEVEL")
    print("==============================")

    if average >= 95:
        performance = "Outstanding"

    elif average >= 90:
        performance = "Excellent"

    elif average >= 85:
        performance = "Very Good"

    elif average >= 80:
        performance = "Good"

    elif average >= 75:
        performance = "Satisfactory"

    else:
        performance = "Needs Improvement"

    print("Performance Level:", performance)

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

    print("\n==============================")
    print("ATTENDANCE")
    print("==============================")

    print("Attendance:", attendance, "%")

    if attendance >= 90:
        print("Attendance Status: Excellent")

    elif attendance >= 80:
        print("Attendance Status: Good")

    elif attendance >= 75:
        print("Attendance Status: Satisfactory")

    else:
        print("Attendance Status: Poor")

    print("\n==============================")
    print("SCHOLARSHIP CHECK")
    print("==============================")

    if average >= 90 and attendance >= 90 and failed_subjects == 0:
        print("Scholarship Eligibility: Eligible")

    else:
        print("Scholarship Eligibility: Not Eligible")

    print("\n==============================")
    print("OVERALL STATUS")
    print("==============================")

    if failed_subjects == 0 and average >= 75:
        print("Overall Status: PASSED")
        print("All subjects passed.")

    elif failed_subjects > 0:
        print("Overall Status: FAILED")
        print("Warning: Student has failed subject(s).")

    else:
        print("Overall Status: FAILED")
        print("Warning: Overall average is below passing.")

    print("\n==============================")
    print("GRADE SUMMARY")
    print("==============================")

    for i in range(len(subjects)):
        if grades[i] >= 90:
            level = "Excellent"

        elif grades[i] >= 85:
            level = "Very Good"

        elif grades[i] >= 80:
            level = "Good"

        elif grades[i] >= 75:
            level = "Passed"

        else:
            level = "Failed"

        print(subjects[i] + ":", grades[i], "-", level)

    print("\n==============================")
    print("CALCULATION COMPLETE")
    print("==============================")

    again = input("Calculate another student? (yes/no): ").lower()

    if again != "yes":
        print("Program Ended.")
        break

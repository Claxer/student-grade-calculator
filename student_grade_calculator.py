while True:
    print("\n== Student Grade Calculator ==")

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    math = float(input("Enter Math grade: "))
    english = float(input("Enter English grade: "))
    science = float(input("Enter Science grade: "))
    filipino = float(input("Enter Filipino grade: "))
    computer = float(input("Enter Computer grade: "))

    subjects = ["Math", "English", "Science", "Filipino", "Computer"]
    grades = [math, english, science, filipino, computer]

    average = sum(grades) / len(grades)

    print("\n==============================")
    print("Student:", name)
    print("Student ID:", student_id)
    print("==============================")

    print("\nSubject Grades:")

    for i in range(len(subjects)):
        print(subjects[i] + ":", grades[i])

    print("\nAverage:", round(average, 2))

    if average >= 97:
        print("Grade: A+")
        print("Remarks: Outstanding!")

    elif average >= 93:
        print("Grade: A")
        print("Remarks: Excellent!")

    elif average >= 90:
        print("Grade: A-")
        print("Remarks: Excellent!")

    elif average >= 87:
        print("Grade: B+")
        print("Remarks: Very Good!")

    elif average >= 83:
        print("Grade: B")
        print("Remarks: Very Good!")

    elif average >= 80:
        print("Grade: B-")
        print("Remarks: Good!")

    elif average >= 77:
        print("Grade: C+")
        print("Remarks: Passed!")

    elif average >= 75:
        print("Grade: C")
        print("Remarks: Passed!")

    else:
        print("Grade: F")
        print("Remarks: Failed")

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

    highest_grade = max(grades)
    lowest_grade = min(grades)

    highest_subject = subjects[grades.index(highest_grade)]
    lowest_subject = subjects[grades.index(lowest_grade)]

    print("\nHighest Grade:", highest_grade)
    print("Highest Subject:", highest_subject)

    print("Lowest Grade:", lowest_grade)
    print("Lowest Subject:", lowest_subject)

    print("\n==============================")
    print("OVERALL PERFORMANCE")
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

    if failed_subjects == 0:
        print("Overall Status: All subjects passed")
    else:
        print("Overall Status: Has failed subject(s)")

    print("\nGrade Percentage:", round(average, 2), "%")

    print("\n==============================")

    again = input(
        "Calculate another student? (yes/no): "
    ).lower()

    if again != "yes":
        print("Program Ended.")
        break

while True:
    print("\n==Student Grade Calculator==")

    name = input("Enter student name: ")

    math = float(input("Enter Math grade: "))
    english = float(input("Enter English grade: "))
    science = float(input("Enter Science grade: "))

    average = (math + english + science) / 3

    print("\nStudent:", name)
    print("Average:", round(average, 2))

    if average >= 90:
        print("Grade: A")
        print("Remarks: Excellent!")

    elif average >= 80:
        print("Grade: B")
        print("Remarks: Very Good!")

    elif average >= 75:
        print("Grade: C")
        print("Remarks: Passed!")

    else:
        print("Grade: F")
        print("Remarks: Failed")

    again = input("\nCalculate another student? (yes/no): ").lower()

    if again != "yes":
        print("Program Ended.")
        break
